#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video Animado para Niños - La Caja de los Tesoros
Versión con estilo Cartoon Network
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

# Paleta de colores vibrantes al estilo Cartoon Network
COLORES = {
    "fondo": "#E8F4F8",      # Azul claro muy suave
    "ana_piel": "#FFD8B1",   # Piel clara
    "ana_cabello": "#FF6B8B",# Rosa coral
    "ana_ropa": "#FF6B6B",   # Rojo coral
    "luis_piel": "#FFD8B1",  # Piel clara
    "luis_cabello": "#4ECDC4",# Turquesa
    "luis_ropa": "#118AB2",  # Azul
    "caja": "#FFD166",       # Amarillo brillante
    "texto": "#2C3E50",      # Azul oscuro
    "acento1": "#FF6B6B",    # Rojo coral
    "acento2": "#6A0572",    # Púrpura
    "acento3": "#06D6A0",    # Verde menta
    "acento4": "#118AB2",    # Azul
    "acento5": "#F9C74F",    # Amarillo
}

# Función para convertir coordenadas a enteros
def int_pos(x, y):
    return int(x), int(y)

# Personajes y elementos (estilo Cartoon Network)
def dibujar_ana(draw, x, y, tamaño=1.0):
    """Dibuja a Ana en estilo Cartoon Network"""
    x, y = int_pos(x, y)
    
    # Cabello (forma exagerada, grande)
    draw.ellipse([x-40*tamaño, y-50*tamaño, x+40*tamaño, y-10*tamaño], 
                fill=COLORES["ana_cabello"], outline=COLORES["texto"], width=2)
    
    # Cara (forma ovalada, grande)
    draw.ellipse([x-35*tamaño, y-40*tamaño, x+35*tamaño, y+20*tamaño], 
                fill=COLORES["ana_piel"], outline=COLORES["texto"], width=2)
    
    # Ojos grandes (estilo cartoon)
    # Ojo izquierdo
    draw.ellipse([x-25*tamaño, y-20*tamaño, x-5*tamaño, y+5*tamaño], 
                fill="white", outline=COLORES["texto"], width=2)
    draw.ellipse([x-20*tamaño, y-15*tamaño, x-10*tamaño, y-5*tamaño], 
                fill=COLORES["texto"])
    
    # Ojo derecho
    draw.ellipse([x+5*tamaño, y-20*tamaño, x+25*tamaño, y+5*tamaño], 
                fill="white", outline=COLORES["texto"], width=2)
    draw.ellipse([x+10*tamaño, y-15*tamaño, x+20*tamaño, y-5*tamaño], 
                fill=COLORES["texto"])
    
    # Sonrisa grande y expresiva
    draw.arc([x-20*tamaño, y+5*tamaño, x+20*tamaño, y+25*tamaño], 
             start=0, end=180, fill=COLORES["texto"], width=3)
    
    # Vestido (forma triangular exagerada)
    draw.polygon([(x-30*tamaño, y+20*tamaño), (x+30*tamaño, y+20*tamaño), 
                 (x+15*tamaño, y+80*tamaño), (x-15*tamaño, y+80*tamaño)], 
                fill=COLORES["ana_ropa"], outline=COLORES["texto"], width=2)
    
    # Brazos (líneas curvas)
    draw.arc([x-50*tamaño, y+20*tamaño, x-10*tamaño, y+50*tamaño], 
             start=0, end=180, fill=COLORES["ana_piel"], width=3)
    draw.arc([x+10*tamaño, y+20*tamaño, x+50*tamaño, y+50*tamaño], 
             start=0, end=180, fill=COLORES["ana_piel"], width=3)
    
    # Piernas (cortas y gruesas)
    draw.line([x-10*tamaño, y+80*tamaño, x-15*tamaño, y+100*tamaño], 
              fill=COLORES["ana_piel"], width=4)
    draw.line([x+10*tamaño, y+80*tamaño, x+15*tamaño, y+100*tamaño], 
              fill=COLORES["ana_piel"], width=4)

def dibujar_luis(draw, x, y, tamaño=1.0):
    """Dibuja a Luis en estilo Cartoon Network"""
    x, y = int_pos(x, y)
    
    # Cabello (despeinado, estilo cartoon)
    draw.ellipse([x-40*tamaño, y-60*tamaño, x+40*tamaño, y-20*tamaño], 
                fill=COLORES["luis_cabello"], outline=COLORES["texto"], width=2)
    
    # Picos de cabello (característico de cartoon)
    for i in range(3):
        offset = -30 + i * 30
        draw.polygon([(x+offset*tamaño, y-60*tamaño), 
                     (x+(offset-10)*tamaño, y-80*tamaño), 
                     (x+(offset+10)*tamaño, y-80*tamaño)], 
                    fill=COLORES["luis_cabello"], outline=COLORES["texto"], width=1)
    
    # Cara
    draw.ellipse([x-35*tamaño, y-40*tamaño, x+35*tamaño, y+20*tamaño], 
                fill=COLORES["luis_piel"], outline=COLORES["texto"], width=2)
    
    # Ojos grandes
    # Ojo izquierdo
    draw.ellipse([x-25*tamaño, y-20*tamaño, x-5*tamaño, y+5*tamaño], 
                fill="white", outline=COLORES["texto"], width=2)
    draw.ellipse([x-20*tamaño, y-15*tamaño, x-10*tamaño, y-5*tamaño], 
                fill=COLORES["texto"])
    
    # Ojo derecho
    draw.ellipse([x+5*tamaño, y-20*tamaño, x+25*tamaño, y+5*tamaño], 
                fill="white", outline=COLORES["texto"], width=2)
    draw.ellipse([x+10*tamaño, y-15*tamaño, x+20*tamaño, y-5*tamaño], 
                fill=COLORES["texto"])
    
    # Sonrisa grande
    draw.arc([x-20*tamaño, y+5*tamaño, x+20*tamaño, y+25*tamaño], 
             start=0, end=180, fill=COLORES["texto"], width=3)
    
    # Camiseta (rectangular con detalles)
    draw.rectangle([x-30*tamaño, y+20*tamaño, x+30*tamaño, y+70*tamaño], 
                  fill=COLORES["luis_ropa"], outline=COLORES["texto"], width=2)
    
    # Brazos (curvos y expresivos)
    draw.arc([x-50*tamaño, y+20*tamaño, x-10*tamaño, y+50*tamaño], 
             start=0, end=180, fill=COLORES["luis_piel"], width=4)
    draw.arc([x+10*tamaño, y+20*tamaño, x+50*tamaño, y+50*tamaño], 
             start=0, end=180, fill=COLORES["luis_piel"], width=4)
    
    # Piernas (cortas y gruesas)
    draw.line([x-15*tamaño, y+70*tamaño, x-20*tamaño, y+100*tamaño], 
              fill=COLORES["luis_piel"], width=5)
    draw.line([x+15*tamaño, y+70*tamaño, x+20*tamaño, y+100*tamaño], 
              fill=COLORES["luis_piel"], width=5)

def dibujar_caja(draw, x, y, tamaño=1.0, color=None):
    """Dibuja una caja de tesoros con estilo cartoon"""
    x, y = int_pos(x, y)
    color = color or COLORES["caja"]
    
    # Caja principal con perspectiva exagerada
    draw.polygon([(x-40*tamaño, y-20*tamaño), (x+40*tamaño, y-20*tamaño),
                 (x+30*tamaño, y+30*tamaño), (x-30*tamaño, y+30*tamaño)],
                fill=color, outline=COLORES["texto"], width=3)
    
    # Tapa de la caja
    draw.polygon([(x-40*tamaño, y-20*tamaño), (x-20*tamaño, y-40*tamaño),
                 (x+20*tamaño, y-40*tamaño), (x+40*tamaño, y-20*tamaño)],
                fill=color, outline=COLORES["texto"], width=3)
    
    # Brillo (efecto de tesoro) - más exagerado
    for i in range(8):
        rx = random.randint(int(x-30*tamaño), int(x+30*tamaño))
        ry = random.randint(int(y-15*tamaño), int(y+25*tamaño))
        r = random.randint(5, 12)
        draw.ellipse([rx-r, ry-r, rx+r, ry+r], fill="white")
        # Rayos de luz
        for j in range(4):
            angle = j * 90
            length = random.randint(10, 20)
            draw.line([rx, ry, 
                      rx + length * np.cos(np.radians(angle)),
                      ry + length * np.sin(np.radians(angle))],
                     fill="white", width=2)

def dibujar_nino(draw, x, y, color_ropa, tamaño=1.0):
    """Dibuja un niño genérico en estilo cartoon"""
    x, y = int_pos(x, y)
    
    # Cabello (forma simple)
    draw.ellipse([x-25*tamaño, y-45*tamaño, x+25*tamaño, y-15*tamaño], 
                fill="#6A4C93", outline=COLORES["texto"], width=2)
    
    # Cabeza
    draw.ellipse([x-25*tamaño, y-35*tamaño, x+25*tamaño, y+15*tamaño], 
                fill="#FFD8B1", outline=COLORES["texto"], width=2)
    
    # Ojos grandes (estilo cartoon)
    draw.ellipse([x-15*tamaño, y-20*tamaño, x-5*tamaño, y-5*tamaño], 
                fill="white", outline=COLORES["texto"], width=2)
    draw.ellipse([x+5*tamaño, y-20*tamaño, x+15*tamaño, y-5*tamaño], 
                fill="white", outline=COLORES["texto"], width=2)
    
    # Pupilas
    draw.ellipse([x-10*tamaño, y-15*tamaño, x-8*tamaño, y-10*tamaño], fill=COLORES["texto"])
    draw.ellipse([x+8*tamaño, y-15*tamaño, x+10*tamaño, y-10*tamaño], fill=COLORES["texto"])
    
    # Sonrisa exagerada
    draw.arc([x-15*tamaño, y-5*tamaño, x+15*tamaño, y+15*tamaño], 
             start=0, end=180, fill=COLORES["texto"], width=3)
    
    # Ropa (estilo cartoon)
    draw.rectangle([x-20*tamaño, y+15*tamaño, x+20*tamaño, y+60*tamaño], 
                  fill=color_ropa, outline=COLORES["texto"], width=2)
    
    # Brazos (curvos)
    draw.arc([x-35*tamaño, y+20*tamaño, x-5*tamaño, y+40*tamaño], 
             start=0, end=180, fill="#FFD8B1", width=4)
    draw.arc([x+5*tamaño, y+20*tamaño, x+35*tamaño, y+40*tamaño], 
             start=0, end=180, fill="#FFD8B1", width=4)
    
    # Piernas (cortas y gruesas)
    draw.line([x-10*tamaño, y+60*tamaño, x-15*tamaño, y+80*tamaño], 
              fill="#FFD8B1", width=5)
    draw.line([x+10*tamaño, y+60*tamaño, x+15*tamaño, y+80*tamaño], 
              fill="#FFD8B1", width=5)

def crear_fondo_degradado(width, height):
    """Crea un fondo con degradado de colores"""
    base = Image.new('RGB', (width, height), COLORES["fondo"])
    draw = ImageDraw.Draw(base)
    
    # Dibujar formas decorativas en el fondo (estilo cartoon)
    formas_colores = [COLORES["acento1"], COLORES["acento2"], 
                      COLORES["acento3"], COLORES["acento4"], COLORES["acento5"]]
    
    for _ in range(25):
        x, y = random.randint(0, width), random.randint(0, height)
        r = random.randint(20, 80)
        color = random.choice(formas_colores)
        
        # Formas variadas (círculos, estrellas, etc.)
        forma = random.choice(["circulo", "estrella", "rectangulo"])
        
        if forma == "circulo":
            draw.ellipse([x-r, y-r, x+r, y+r], fill=color, outline=None)
        elif forma == "estrella":
            # Dibujar una estrella simple
            radio_externo = r
            radio_interno = r * 0.5
            puntos = []
            for i in range(10):
                angulo = np.pi/5 * i
                radio = radio_externo if i % 2 == 0 else radio_interno
                puntos.append((x + radio * np.cos(angulo), 
                              y + radio * np.sin(angulo)))
            draw.polygon(puntos, fill=color, outline=None)
        else:  # rectangulo
            w, h = random.randint(30, 100), random.randint(30, 100)
            rotacion = random.randint(0, 45)
            # Crear un rectángulo rotado
            rect = Image.new('RGBA', (w, h), color)
            rect_rot = rect.rotate(rotacion, expand=True)
            base.paste(rect_rot, (x - rect_rot.width//2, y - rect_rot.height//2), rect_rot)
    
    return base

def crear_imagen_escena(escena_num, texto_principal, texto_secundario=None, elementos=None):
    """Crea una imagen estática para una escena con elementos animados"""
    img = crear_fondo_degradado(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    # Intentar cargar fuentes más cartoon
    try:
        # Intentar con fuentes más divertidas
        titulo_font = ImageFont.truetype("comicbd.ttf", 60)  # Comic Sans Bold
    except:
        try:
            titulo_font = ImageFont.truetype("arialbd.ttf", 50)
        except:
            titulo_font = ImageFont.load_default()
    
    try:
        texto_font = ImageFont.truetype("comic.ttf", 36)  # Comic Sans regular
    except:
        try:
            texto_font = ImageFont.truetype("arial.ttf", 30)
        except:
            texto_font = ImageFont.load_default()
    
    # Dibujar texto principal con contorno
    bbox = draw.textbbox((0, 0), texto_principal, font=titulo_font)
    text_width = bbox[2] - bbox[0]
    
    # Texto con contorno (estilo cartoon)
    for dx, dy in [(-2,-2), (-2,2), (2,-2), (2,2)]:
        draw.text((WIDTH/2 + dx, 100 + dy), texto_principal, 
                 fill="white", font=titulo_font, anchor="mm")
    
    draw.text((WIDTH/2, 100), texto_principal, fill=COLORES["texto"], 
              font=titulo_font, anchor="mm")
    
    # Dibujar texto secundario si existe
    if texto_secundario:
        for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
            draw.text((WIDTH/2 + dx, 170 + dy), texto_secundario, 
                     fill="white", font=texto_font, anchor="mm")
        draw.text((WIDTH/2, 170), texto_secundario, fill=COLORES["texto"], 
                  font=texto_font, anchor="mm")
    
    # Dibujar elementos según la escena
    if escena_num == 1:
        # Escena 1: Introducción
        dibujar_ana(draw, WIDTH/2 - 200, HEIGHT/2 + 50, tamaño=1.2)
        dibujar_luis(draw, WIDTH/2 + 200, HEIGHT/2 + 50, tamaño=1.2)
        dibujar_caja(draw, WIDTH/2, HEIGHT/2 - 50, tamaño=1.8)
        
    elif escena_num == 2:
        # Escena 2: Objetivos
        objetivos = [
            "Expresión emocional",
            "Narración y resignificación", 
            "Fortalecimiento de la identidad"
        ]
        for i, objetivo in enumerate(objetivos):
            y_pos = HEIGHT/2 - 50 + i * 70
            # Dibujar viñetas con estilo cartoon
            draw.ellipse([WIDTH/2 - 200, y_pos-10, WIDTH/2 - 180, y_pos+10], 
                        fill=COLORES["acento1"])
            draw.text((WIDTH/2 - 170, y_pos), objetivo, fill=COLORES["texto"], 
                      font=texto_font, anchor="lm")
            
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
            y_pos = HEIGHT/2 - 100 + i * 50
            # Viñetas con diferentes colores
            color_viñeta = COLORES[f"acento{(i % 5) + 1}"]
            draw.ellipse([WIDTH/2 - 220, y_pos-8, WIDTH/2 - 200, y_pos+8], 
                        fill=color_viñeta)
            draw.text((WIDTH/2 - 190, y_pos), material, fill=COLORES["texto"], 
                      font=texto_font, anchor="lm")
            
    elif escena_num == 4:
        # Escena 4: Paso 1 - Decorar
        dibujar_nino(draw, WIDTH/2 - 150, HEIGHT/2 + 30, COLORES["acento1"], tamaño=1.1)
        dibujar_nino(draw, WIDTH/2 + 150, HEIGHT/2 + 30, COLORES["acento3"], tamaño=1.1)
        dibujar_caja(draw, WIDTH/2, HEIGHT/2 - 50, tamaño=1.5)
        draw.text((WIDTH/2, HEIGHT/2 + 120), "Crear un espacio seguro", 
                  fill=COLORES["texto"], font=texto_font, anchor="mm")
        
    elif escena_num == 5:
        # Escena 5: Paso 2 - Buscar tesoros
        tesoros = [
            "Recuerdo feliz",
            "Fortaleza personal", 
            "Sueño futuro"
        ]
        for i, tesoro in enumerate(tesoros):
            y_pos = HEIGHT/2 - 50 + i * 80
            # Dibujar cofres pequeños como viñetas
            dibujar_caja(draw, WIDTH/2 - 200, y_pos, tamaño=0.5, color=COLORES[f"acento{i+1}"])
            draw.text((WIDTH/2 - 170, y_pos), tesoro, fill=COLORES["texto"], 
                      font=texto_font, anchor="lm")
            
    elif escena_num == 6:
        # Escena 6: Paso 3 - Elegir objetos
        objetos = ["Piedra", "Botón", "Tela", "Hoja", "Foto"]
        for i, objeto in enumerate(objetos):
            x_pos = WIDTH/2 - 200 + i * 100
            dibujar_caja(draw, x_pos, HEIGHT/2 - 30, tamaño=0.8, color=COLORES[f"acento{i+1}"])
            draw.text((x_pos, HEIGHT/2 + 30), objeto, fill=COLORES["texto"], 
                      font=texto_font, anchor="mm")
            
    elif escena_num == 7:
        # Escena 7: Paso 4 - Compartir
        dibujar_nino(draw, WIDTH/2, HEIGHT/2 - 30, COLORES["acento2"], tamaño=1.2)
        dibujar_caja(draw, WIDTH/2, HEIGHT/2 + 50, tamaño=1.0)
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
            y_pos = HEIGHT/2 - 50 + i * 70
            # Dibujar estrellas como viñetas
            draw.regular_polygon((WIDTH/2 - 200, y_pos, 15), n_sides=5, 
                                fill=COLORES[f"acento{i+1}"], outline=COLORES["texto"])
            draw.text((WIDTH/2 - 170, y_pos), beneficio, fill=COLORES["texto"], 
                      font=texto_font, anchor="lm")
            
    elif escena_num == 9:
        # Escena 9: Cierre
        dibujar_caja(draw, WIDTH/2, HEIGHT/2 - 50, tamaño=2.0)
        
        # Texto con efecto cartoon
        for dx, dy in [(-3,-3), (-3,3), (3,-3), (3,3)]:
            draw.text((WIDTH/2 + dx, HEIGHT/2 - 120 + dy), "Cada niño es único…", 
                     fill="white", font=titulo_font, anchor="mm")
            draw.text((WIDTH/2 + dx, HEIGHT/2 - 60 + dy), "y su tesoro también", 
                     fill="white", font=texto_font, anchor="mm")
        
        draw.text((WIDTH/2, HEIGHT/2 - 120), "Cada niño es único…", 
                  fill=COLORES["texto"], font=titulo_font, anchor="mm")
        draw.text((WIDTH/2, HEIGHT/2 - 60), "y su tesoro también", 
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