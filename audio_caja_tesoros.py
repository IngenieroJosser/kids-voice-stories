#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Audio Generator (MP3) – La Caja de los Tesoros
Versión mejorada con voces de alta calidad usando gTTS
"""

import os, time
from pathlib import Path
import numpy as np
from pydub import AudioSegment, effects
import librosa, soundfile as sf
from gtts import gTTS
from scipy import signal  # Importación añadida

# ====================== CONFIGURACIÓN RÁPIDA ======================
OUTPUT_MP3 = "La_Caja_de_los_Tesoros.mp3"
BG_MUSIC_FILE = "bg_music.mp3"
BG_TARGET_DBFS   = -23
VOICE_TARGET_DBFS= -16
MASTER_TARGET_DBFS= -14

# Configuración de voces (usando gTTS)
ANA_VOICE = "es"  # Español - voz femenina
LUIS_VOICE = "es"  # Español - voz masculina (usaremos el mismo idioma)
SLOW_SPEED = False  # Velocidad de habla

LEAD_IN_MS = 400
LEAD_OUT_MS = 600
# ================================================================

GUIION = [
    # Escena 1
    ("Ana", "¡Hola! Bienvenidos. Hoy vamos a aprender una actividad muy especial: La Caja de los Tesoros."),
    ("Luis", "¿La Caja de los Tesoros? Suena misterioso… ¿qué es exactamente?"),
    ("Ana", "Es una dinámica lúdica que ayuda a los niños a expresar emociones, fortalecer su identidad y resignificar experiencias."),
    
    # Escena 2
    ("Ana", "Los objetivos son tres: Uno, expresión emocional. Dos, narración y resignificación. Y tres, fortalecimiento de la identidad."),
    
    # Escena 3
    ("Luis", "Necesitarás: una caja por niño, materiales para decorar, objetos pequeños como botones o piedras, hojas y colores, y una bolsa con objetos variados."),
    
    # Escena 4
    ("Ana", "Primero, invita a los niños a decorar su caja. Será un lugar especial y seguro para guardar sus tesoros. Este paso simboliza la creación de un espacio seguro."),
    
    # Escena 5
    ("Luis", "Después explícales que cada uno tiene tesoros dentro de sí. Deben pensar en tres cosas importantes: un recuerdo feliz, una fortaleza personal y un sueño para el futuro."),
    ("Ana", "Pueden escribirlo o dibujarlo, y guardarlo en la caja."),
    
    # Escena 6
    ("Ana", "Luego, ofrece la bolsa con objetos variados y pide que cada niño elija uno que represente algo especial para él. No hay respuestas correctas o incorrectas."),
    
    # Escena 7
    ("Luis", "Quien lo desee puede compartir sus tesoros con el grupo. Pero nunca debe ser obligatorio."),
    ("Ana", "Cada niño se lleva su caja como recordatorio de que su historia también guarda momentos valiosos y esperanzas."),
    
    # Escena 8
    ("Ana", "Con esta actividad, los niños fortalecen su identidad, expresan sus emociones y resignifican experiencias."),
    ("Luis", "Recuerda siempre cuidar un ambiente de confianza y respeto."),
    
    # Escena 9
    ("Luis", "Ahora ya conoces la dinámica de La Caja de los Tesoros."),
    ("Ana", "Cada niño es único… y su tesoro también."),
]

def text_to_speech_gtts(text, outfile, lang="es", slow=False):
    """Convierte texto a voz usando gTTS (Google Text-to-Speech)"""
    try:
        tts = gTTS(text=text, lang=lang, slow=slow)
        tts.save(outfile)
        time.sleep(0.5)  # Pequeña pausa para evitar sobrecargar la API
        return True
    except Exception as e:
        print(f"Error con gTTS: {e}")
        # Fallback a un método alternativo si gTTS falla
        return False

def apply_voice_effects(in_wav, out_wav, pitch_shift=0, speed_change=1.0):
    """Aplica efectos de voz para hacerla más natural"""
    y, sr = librosa.load(in_wav, sr=None, mono=True)
    
    # Ajuste de tono (pitch)
    if pitch_shift != 0:
        y = librosa.effects.pitch_shift(y, sr=sr, n_steps=pitch_shift)
    
    # Ajuste de velocidad (sin cambiar el tono)
    if speed_change != 1.0:
        y = librosa.effects.time_stretch(y, rate=speed_change)
    
    # Ecualización suave para mejorar la claridad
    # Filtro paso banda para enfatizar frecuencias vocales
    b, a = signal.butter(4, [100, 5000], btype='bandpass', fs=sr)
    y = signal.filtfilt(b, a, y)
    
    # Normalización
    peak = np.max(np.abs(y)) + 1e-9
    if peak > 1.0:
        y = y / peak
    
    sf.write(out_wav, y, sr)

def synth_bg(duration_ms, sr=44100):
    """Genera música de fondo suave"""
    dur = duration_ms/1000.0
    t = np.linspace(0, dur, int(sr*dur), endpoint=False)
    
    # Crear una progresión de acordes más suave
    chords = [
        (261.63, 329.63, 392.00),  # Do-Mi-Sol
        (293.66, 369.99, 440.00),  # Re-Fa#-La
        (329.63, 415.30, 493.88),  # Mi-Sol#-Si
        (349.23, 440.00, 523.25),  # Fa-La-Do
    ]
    
    y = np.zeros_like(t)
    segment_len = len(t) // len(chords)
    
    for i, chord in enumerate(chords):
        start = i * segment_len
        end = (i + 1) * segment_len if i < len(chords) - 1 else len(t)
        
        for f in chord:
            # Usar envolvente suave para cada segmento
            envelope = np.ones(end - start)
            if i == 0:  # Fade in en el primer segmento
                envelope[:500] = np.linspace(0, 1, 500)
            if i == len(chords) - 1:  # Fade out en el último segmento
                envelope[-500:] = np.linspace(1, 0, 500)
                
            y[start:end] += 0.2 * np.sin(2 * np.pi * f * t[start:end]) * envelope
    
    # Reverb suave
    delay = int(0.15 * sr)
    echo = np.zeros_like(y)
    echo[delay:] = y[:-delay] * 0.3
    y = y + echo
    
    # Normalizar
    y = y / (np.max(np.abs(y)) + 1e-9)
    
    # Convertir a AudioSegment
    audio = (y * 32767).astype(np.int16).tobytes()
    seg = AudioSegment(data=audio, sample_width=2, frame_rate=sr, channels=1)
    seg = effects.normalize(seg, headroom=12.0)
    
    return seg

def main():
    tmp = Path("tmp_audio"); tmp.mkdir(exist_ok=True)
    pieces = []
    
    # Generar todas las voces primero
    for i, (who, line) in enumerate(GUIION, 1):
        raw = tmp/f"line_{i:02d}_{who}.mp3"
        processed = tmp/f"line_{i:02d}_{who}_processed.wav"
        
        print(f"Generando voz para {who}: {line[:50]}...")
        
        if who.lower() == "ana":
            # Usar gTTS para Ana
            success = text_to_speech_gtts(line, str(raw), lang=ANA_VOICE, slow=SLOW_SPEED)
            if success:
                # Convertir a WAV y aplicar efectos
                audio = AudioSegment.from_mp3(str(raw))
                audio.export(str(processed), format="wav")
                apply_voice_effects(str(processed), str(processed), pitch_shift=1, speed_change=1.0)
        else:
            # Usar gTTS para Luis
            success = text_to_speech_gtts(line, str(raw), lang=LUIS_VOICE, slow=SLOW_SPEED)
            if success:
                # Convertir a WAV y aplicar efectos
                audio = AudioSegment.from_mp3(str(raw))
                audio.export(str(processed), format="wav")
                apply_voice_effects(str(processed), str(processed), pitch_shift=-1, speed_change=1.0)
        
        # Cargar el audio procesado
        if os.path.exists(processed):
            pieces.append(AudioSegment.from_file(str(processed)))
        else:
            print(f"Error procesando línea {i}. Continuando...")
    
    # Concatenar todas las pistas de voz sin pausas
    if pieces:
        voices = sum(pieces, AudioSegment.silent(duration=0))
        voices = effects.normalize(voices)
        voices = voices.apply_gain(VOICE_TARGET_DBFS - voices.dBFS)
    else:
        print("No se generaron piezas de audio. Verifica tu conexión a Internet.")
        return

    total_ms = len(voices) + LEAD_IN_MS + LEAD_OUT_MS

    # Procesar música de fondo
    if os.path.exists(BG_MUSIC_FILE):
        bg = AudioSegment.from_file(BG_MUSIC_FILE)
        loops = int(np.ceil(total_ms/len(bg))) if len(bg)>0 else 1
        bg_full = AudioSegment.silent(0)
        for _ in range(loops):
            bg_full += bg
        bg_full = bg_full[:total_ms]
    else:
        bg_full = synth_bg(total_ms)

    # Mezclar voces y música de fondo
    bg_full = effects.normalize(bg_full, headroom=14.0)
    bg_full = bg_full.apply_gain(BG_TARGET_DBFS - bg_full.dBFS)

    master = AudioSegment.silent(LEAD_IN_MS) + voices + AudioSegment.silent(LEAD_OUT_MS)
    bg_full = bg_full[:len(master)]
    mixed = bg_full.overlay(master)
    mixed = effects.normalize(mixed, headroom=8.0)
    mixed = mixed.apply_gain(MASTER_TARGET_DBFS - mixed.dBFS)

    # Exportar el resultado final
    mixed.export(OUTPUT_MP3, format="mp3", bitrate="192k")
    print(f"¡Audio generado exitosamente! -> {OUTPUT_MP3}")

if __name__ == "__main__":
    main()