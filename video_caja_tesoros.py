#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video Animado para Niños - La Caja de los Tesoros
Versión corregida y mejorada
"""

import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random
from moviepy.editor import *

# Configuración
AUDIO_FILE = "La_Caja_de_los_Tesoros.mp3"
OUTPUT_VIDEO = "La_Caja_de_los_Tesoros_Video_Animado.mp4"
WIDTH, HEIGHT = 1280, 720
FPS = 24

# Paleta de colores vibrantes para niños
COLORES = {
    "fondo": "#E8F4F8",  # Azul claro muy suave
    "ana": "#FF6B8B",    # Rosa coral
    "luis": "#4ECDC4",   # Turquesa
    "caja": "#FFD166",   # Amarillo brillante
    "texto": "#2C3E50",  # Azul oscuro
    "acento1": "#FF6B6B",# Rojo coral
    "acento2": "#6A0572",# Púrpura
    "acento3": "#06D6A0",# Verde menta
    "acento4": "#118AB2",# Azul
    "acento5": "#F9C74F",# Amarillo
}

# Función para convertir coordenadas a enteros
def int_pos(x, y):
    return int(x), int(y)

# Personajes y elementos (dibujos simples estilo caricatura)
def dibujar_ana(draw, x, y, tamaño=1.0):
    """Dibuja a Ana (personaje femenino)"""
    x, y = int_pos(x, y)
    # Cabeza
    draw.ellipse([x-30*tamaño, y-40*tamaño, x+30*tamaño, y+20*tamaño], 
                fill=COLORES["ana"], outline=COLORES["texto"], width=2)
    
    # Ojos
    draw.ellipse([x-15*tamaño, y-25*tamaño, x-5*tamaño, y-15*tamaño], 
                fill="white", outline=COLORES["texto"], width=1)
    draw.ellipse([x+5*tamaño, y-25*tamaño, x+15*tamaño, y-15*tamaño], 
                fill="white", outline=COLORES["texto"], width=1)
    
    # Pupilas
    draw.ellipse([x-10*tamaño, y-20*tamaño, x-8*tamaño, y-18*tamaño], fill=COLORES["texto"])
    draw.ellipse([x+8*tamaño, y-20*tamaño, x+10*tamaño, y-18*tamaño], fill=COLORES["texto"])
    
    # Sonrisa
    draw.arc([x-15*tamaño, y-15*tamaño, x+15*tamaño, y+5*tamaño], 
             start=0, end=180, fill=COLORES["texto"], width=2)
    
    # Vestido
    draw.polygon([(x-25*tamaño, y+20*tamaño), (x+25*tamaño, y+20*tamaño), 
                 (x+20*tamaño, y+60*tamaño), (x-20*tamaño, y+60*tamaño)], 
                fill=COLORES["acento1"], outline=COLORES["texto"], width=2)
    
    # Brazos
    draw.line([x-25*tamaño, y+30*tamaño, x-40*tamaño, y+20*tamaño], 
              fill=COLORES["ana"], width=3)
    draw.line([x+25*tamaño, y+30*tamaño, x+40*tamaño, y+20*tamaño], 
              fill=COLORES["ana"], width=3)
    
    # Piernas
    draw.line([x-10*tamaño, y+60*tamaño, x-15*tamaño, y+80*tamaño], 
              fill=COLORES["ana"], width=3)
    draw.line([x+10*tamaño, y+60*tamaño, x+15*tamaño, y+80*tamaño], 
              fill=COLORES["ana"], width=3)

def dibujar_luis(draw, x, y, tamaño=1.0):
    """Dibuja a Luis (personaje masculino)"""
    x, y = int_pos(x, y)
    # Cabeza
    draw.ellipse([x-30*tamaño, y-40*tamaño, x+30*tamaño, y+20*tamaño], 
                fill=COLORES["luis"], outline=COLORES["texto"], width=2)
    
    # Ojos
    draw.ellipse([x-15*tamaño, y-25*tamaño, x-5*tamaño, y-15*tamaño], 
                fill="white", outline=COLORES["texto"], width=1)
    draw.ellipse([x+5*tamaño, y-25*tamaño, x+15*tamaño, y-15*tamaño], 
                fill="white", outline=COLORES["texto"], width=1)
    
    # Pupilas
    draw.ellipse([x-10*tamaño, y-20*tamaño, x-8*tamaño, y-18*tamaño], fill=COLORES["texto"])
    draw.ellipse([x+8*tamaño, y-20*tamaño, x+10*tamaño, y-18*tamaño], fill=COLORES["texto"])
    
    # Sonrisa
    draw.arc([x-15*tamaño, y-15*tamaño, x+15*tamaño, y+5*tamaño], 
             start=0, end=180, fill=COLORES["texto"], width=2)
    
    # Camisa
    draw.polygon([(x-25*tamaño, y+20*tamaño), (x+25*tamaño, y+20*tamaño), 
                 (x+20*tamaño, y+60*tamaño), (x-20*tamaño, y+60*tamaño)], 
                fill=COLORES["acento4"], outline=COLORES["texto"], width=2)
    
    # Brazos
    draw.line([x-25*tamaño, y+30*tamaño, x-40*tamaño, y+20*tamaño], 
              fill=COLORES["luis"], width=3)
    draw.line([x+25*tamaño, y+30*tamaño, x+40*tamaño, y+20*tamaño], 
              fill=COLORES["luis"], width=3)
    
    # Piernas
    draw.line([x-10*tamaño, y+60*tamaño, x-15*tamaño, y+80*tamaño], 
              fill=COLORES["luis"], width=3)
    draw.line([x+10*tamaño, y+60*tamaño, x+15*tamaño, y+80*tamaño], 
              fill=COLORES["luis"], width=3)

def dibujar_caja(draw, x, y, tamaño=1.0, color=None):
    """Dibuja una caja de tesoros"""
    x, y = int_pos(x, y)
    color = color or COLORES["caja"]
    
    # Caja principal
    draw.rectangle([x-40*tamaño, y-30*tamaño, x+40*tamaño, y+30*tamaño], 
                  fill=color, outline=COLORES["texto"], width=2)
    
    # Líneas para efecto 3D
    draw.line([x-40*tamaño, y-30*tamaño, x-20*tamaño, y-40*tamaño], 
              fill=COLORES["texto"], width=2)
    draw.line([x+40*tamaño, y-30*tamaño, x+20*tamaño, y-40*tamaño], 
              fill=COLORES["texto"], width=2)
    draw.line([x-20*tamaño, y-40*tamaño, x+20*tamaño, y-40*tamaño], 
              fill=COLORES["texto"], width=2)
    
    # Brillo (efecto de tesoro) - CORREGIDO: usar enteros
    for i in range(5):
        rx = random.randint(int(x-30), int(x+30))
        ry = random.randint(int(y-20), int(y+20))
        r = random.randint(3, 8)
        draw.ellipse([rx-r, ry-r, rx+r, ry+r], fill="white")

def dibujar_nino(draw, x, y, color_ropa, tamaño=1.0):
    """Dibuja un niño genérico"""
    x, y = int_pos(x, y)
    # Cabeza
    draw.ellipse([x-25*tamaño, y-35*tamaño, x+25*tamaño, y+15*tamaño], 
                fill="#FFD8B1", outline=COLORES["texto"], width=2)
    
    # Ojos
    draw.ellipse([x-12*tamaño, y-20*tamaño, x-5*tamaño, y-13*tamaño], 
                fill="white", outline=COLORES["texto"], width=1)
    draw.ellipse([x+5*tamaño, y-20*tamaño, x+12*tamaño, y-13*tamaño], 
                fill="white", outline=COLORES["texto"], width=1)
    
    # Pupilas
    draw.ellipse([x-8*tamaño, y-16*tamaño, x-6*tamaño, y-14*tamaño], fill=COLORES["texto"])
    draw.ellipse([x+6*tamaño, y-16*tamaño, x+8*tamaño, y-14*tamaño], fill=COLORES["texto"])
    
    # Sonrisa
    draw.arc([x-10*tamaño, y-10*tamaño, x+10*tamaño, y+5*tamaño], 
             start=0, end=180, fill=COLORES["texto"], width=2)
    
    # Ropa
    draw.polygon([(x-20*tamaño, y+15*tamaño), (x+20*tamaño, y+15*tamaño), 
                 (x+15*tamaño, y+50*tamaño), (x-15*tamaño, y+50*tamaño)], 
                fill=color_ropa, outline=COLORES["texto"], width=2)
    
    # Brazos
    draw.line([x-20*tamaño, y+25*tamaño, x-35*tamaño, y+15*tamaño], 
              fill="#FFD8B1", width=3)
    draw.line([x+20*tamaño, y+25*tamaño, x+35*tamaño, y+15*tamaño], 
              fill="#FFD8B1", width=3)
    
    # Piernas
    draw.line([x-8*tamaño, y+50*tamaño, x-12*tamaño, y+65*tamaño], 
              fill="#FFD8B1", width=3)
    draw.line([x+8*tamaño, y+50*tamaño, x+12*tamaño, y+65*tamaño], 
              fill="#FFD8B1", width=3)

def crear_fondo_degradado(width, height):
    """Crea un fondo con degradado de colores"""
    base = Image.new('RGB', (width, height), COLORES["fondo"])
    draw = ImageDraw.Draw(base)
    
    # Dibujar formas decorativas en el fondo
    for _ in range(20):
        x, y = random.randint(0, width), random.randint(0, height)
        r = random.randint(10, 50)
        color = random.choice([COLORES["acento1"], COLORES["acento2"], 
                              COLORES["acento3"], COLORES["acento4"], COLORES["acento5"]])
        draw.ellipse([x-r, y-r, x+r, y+r], fill=color, outline=None)
    
    return base

def crear_imagen_escena(escena_num, texto_principal, texto_secundario=None, elementos=None):
    """Crea una imagen estática para una escena con elementos animados"""
    img = crear_fondo_degradado(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    # Intentar cargar fuentes
    try:
        titulo_font = ImageFont.truetype("arialbd.ttf", 50)
        texto_font = ImageFont.truetype("arial.ttf", 30)
    except:
        titulo_font = ImageFont.load_default()
        texto_font = ImageFont.load_default()
    
    # Dibujar texto principal
    draw.text((WIDTH/2, 100), texto_principal, fill=COLORES["texto"], 
              font=titulo_font, anchor="mm")
    
    # Dibujar texto secundario si existe
    if texto_secundario:
        draw.text((WIDTH/2, 160), texto_secundario, fill=COLORES["texto"], 
                  font=texto_font, anchor="mm")
    
    # Dibujar elementos según la escena
    if escena_num == 1:
        # Escena 1: Introducción
        dibujar_ana(draw, WIDTH/2 - 200, HEIGHT/2)
        dibujar_luis(draw, WIDTH/2 + 200, HEIGHT/2)
        dibujar_caja(draw, WIDTH/2, HEIGHT/2, tamaño=1.5)
        
    elif escena_num == 2:
        # Escena 2: Objetivos
        objetivos = [
            "Expresión emocional",
            "Narración y resignificación", 
            "Fortalecimiento de la identidad"
        ]
        for i, objetivo in enumerate(objetivos):
            y_pos = HEIGHT/2 - 50 + i * 60
            draw.text((WIDTH/2, y_pos), f"• {objetivo}", fill=COLORES["texto"], 
                      font=texto_font, anchor="mm")
            
    elif escena_num == 3:
        # Escena 3: Materiales
        materiales = [
            "Caja por niño",
            "Materiales para decorar", 
            "Objetos pequeños",
            "Hojas y colores", 
            "Bolsa de objetos"
        ]
        for i, material in enumerate(materiales):
            y_pos = HEIGHT/2 - 100 + i * 40
            draw.text((WIDTH/2, y_pos), f"• {material}", fill=COLORES["texto"], 
                      font=texto_font, anchor="mm")
            
    elif escena_num == 4:
        # Escena 4: Paso 1 - Decorar
        dibujar_nino(draw, WIDTH/2 - 150, HEIGHT/2, COLORES["acento1"])
        dibujar_nino(draw, WIDTH/2 + 150, HEIGHT/2, COLORES["acento3"])
        dibujar_caja(draw, WIDTH/2, HEIGHT/2, tamaño=1.2)
        draw.text((WIDTH/2, HEIGHT/2 + 100), "Crear un espacio seguro", 
                  fill=COLORES["texto"], font=texto_font, anchor="mm")
        
    elif escena_num == 5:
        # Escena 5: Paso 2 - Buscar tesoros
        tesoros = [
            "Recuerdo feliz",
            "Fortaleza personal", 
            "Sueño futuro"
        ]
        for i, tesoro in enumerate(tesoros):
            y_pos = HEIGHT/2 - 50 + i * 60
            draw.text((WIDTH/2, y_pos), f"• {tesoro}", fill=COLORES["texto"], 
                      font=texto_font, anchor="mm")
            
    elif escena_num == 6:
        # Escena 6: Paso 3 - Elegir objetos
        objetos = ["Piedra", "Botón", "Tela", "Hoja"]
        for i, objeto in enumerate(objetos):
            x_pos = WIDTH/2 - 150 + i * 100
            dibujar_caja(draw, x_pos, HEIGHT/2, tamaño=0.7, color=COLORES[f"acento{i+1}"])
            draw.text((x_pos, HEIGHT/2 + 50), objeto, fill=COLORES["texto"], 
                      font=texto_font, anchor="mm")
            
    elif escena_num == 7:
        # Escena 7: Paso 4 - Compartir
        dibujar_nino(draw, WIDTH/2, HEIGHT/2 - 50, COLORES["acento2"])
        dibujar_caja(draw, WIDTH/2, HEIGHT/2 + 50, tamaño=0.8)
        draw.text((WIDTH/2, HEIGHT/2 + 120), "Nunca debe ser obligatorio", 
                  fill=COLORES["texto"], font=texto_font, anchor="mm")
        
    elif escena_num == 8:
        # Escena 8: Beneficios
        beneficios = [
            "Fortalecimiento de la identidad",
            "Expresión de emociones", 
            "Resignificación de experiencias"
        ]
        for i, beneficio in enumerate(beneficios):
            y_pos = HEIGHT/2 - 50 + i * 60
            draw.text((WIDTH/2, y_pos), f"• {beneficio}", fill=COLORES["texto"], 
                      font=texto_font, anchor="mm")
            
    elif escena_num == 9:
        # Escena 9: Cierre
        dibujar_caja(draw, WIDTH/2, HEIGHT/2, tamaño=1.5)
        draw.text((WIDTH/2, HEIGHT/2 - 100), "Cada niño es único…", 
                  fill=COLORES["texto"], font=titulo_font, anchor="mm")
        draw.text((WIDTH/2, HEIGHT/2 - 50), "y su tesoro también", 
                  fill=COLORES["texto"], font=texto_font, anchor="mm")
    
    # Guardar imagen
    img_path = f"escena_{escena_num}.png"
    img.save(img_path)
    return img_path

def crear_video_simple():
    """Crea el video con animaciones y transiciones"""
    print("Iniciando creación de video animado...")
    
    # Verificar archivo de audio
    if not os.path.exists(AUDIO_FILE):
        print(f"Error: No se encuentra el archivo de audio '{AUDIO_FILE}'")
        return False
    
    # Cargar audio
    try:
        audio = AudioFileClip(AUDIO_FILE)
        duracion_audio = audio.duration
        print(f"Duración del audio: {duracion_audio:.2f} segundos")
    except Exception as e:
        print(f"Error al cargar el audio: {e}")
        return False
    
    # Definir escenas
    escenas = [
        {
            "numero": 1,
            "titulo": "¡La Caja de los Tesoros!",
            "subtitulo": "Una dinámica para expresión emocional"
        },
        {
            "numero": 2,
            "titulo": "Objetivos",
            "subtitulo": None
        },
        {
            "numero": 3,
            "titulo": "Materiales necesarios",
            "subtitulo": None
        },
        {
            "numero": 4,
            "titulo": "Paso 1: Decorar la caja",
            "subtitulo": "Crear un espacio seguro"
        },
        {
            "numero": 5,
            "titulo": "Paso 2: Buscar tesoros interiores",
            "subtitulo": None
        },
        {
            "numero": 6,
            "titulo": "Paso 3: Elegir objetos significativos",
            "subtitulo": "No hay respuestas correctas o incorrectas"
        },
        {
            "numero": 7,
            "titulo": "Paso 4: Compartir (opcional)",
            "subtitulo": "Nunca debe ser obligatorio"
        },
        {
            "numero": 8,
            "titulo": "Beneficios",
            "subtitulo": None
        },
        {
            "numero": 9,
            "titulo": "Cada niño es único…",
            "subtitulo": "y su tesoro también"
        }
    ]
    
    # Calcular duración por escena
    duracion_por_escena = duracion_audio / len(escenas)
    print(f"Duración por escena: {duracion_por_escena:.2f} segundos")
    
    # Crear imágenes para cada escena
    print("Creando imágenes para las escenas...")
    clips = []
    
    for escena in escenas:
        print(f"Creando escena {escena['numero']}: {escena['titulo']}")
        
        # Crear imagen estática para la escena
        img_path = crear_imagen_escena(
            escena["numero"], 
            escena["titulo"], 
            escena["subtitulo"]
        )
        
        # Crear clip con animaciones simples
        clip = ImageClip(img_path).set_duration(duracion_por_escena)
        
        # Añadir efectos de animación simples (sin resize problemático)
        clip = clip.fadein(1).fadeout(1)
        
        clips.append(clip)
    
    # Unir todas las escenas
    print("Uniendo todas las escenas...")
    video = concatenate_videoclips(clips, method="compose")
    
    # Agregar audio
    print("Agregando audio...")
    video = video.set_audio(audio)
    
    # Exportar video
    print("Exportando video...")
    try:
        video.write_videofile(
            OUTPUT_VIDEO,
            fps=FPS,
            codec='libx264',
            audio_codec='aac',
            threads=4,
            preset='medium',
            verbose=False,
            logger=None
        )
        print(f"¡Video animado creado exitosamente!: {OUTPUT_VIDEO}")
    except Exception as e:
        print(f"Error al exportar el video: {e}")
        return False
    
    # Limpiar archivos temporales
    print("Limpiando archivos temporales...")
    for i in range(1, 10):
        try:
            os.remove(f"escena_{i}.png")
        except:
            pass
    
    return True

if __name__ == "__main__":
    # Verificar dependencias
    try:
        from moviepy.editor import *
        from PIL import Image, ImageDraw, ImageFont
        import numpy as np
        
        if crear_video_simple():
            print("¡Proceso completado exitosamente!")
            print(f"El video se ha guardado como: {OUTPUT_VIDEO}")
        else:
            print("Error en la creación del video")
            
    except ImportError as e:
        print(f"Error: {e}")
        print("Asegúrate de tener instaladas las dependencias:")
        print("pip install moviepy pillow numpy")