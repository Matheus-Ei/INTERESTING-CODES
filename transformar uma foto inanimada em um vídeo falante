import cv2
import face_recognition
from moviepy.editor import *

def detect_faces(image_path):
    # Carrega a imagem usando a biblioteca face_recognition
    image = face_recognition.load_image_file(image_path)

    # Detecta as localizações dos rostos na imagem
    face_locations = face_recognition.face_locations(image)

    return face_locations

def create_talking_video(image_path, output_path, text):
    # Detecta os rostos na imagem
    face_locations = detect_faces(image_path)

    if len(face_locations) == 0:
        print("Nenhum rosto encontrado na imagem.")
        return

    # Carrega o vídeo do rosto falante
    video_clip = VideoFileClip("face_video.mp4")

    # Carrega a imagem de entrada
    image_clip = ImageClip(image_path)

    # Redimensiona a imagem para as dimensões do vídeo
    image_clip = image_clip.resize(height=video_clip.h)

    # Converte o texto em fala
    speech_clip = TextClip(text, fontsize=30, color='white', bg_color='black').set_duration(video_clip.duration)

    # Combina a imagem, o vídeo do rosto falante e o áudio do texto
    final_clip = CompositeVideoClip([image_clip, video_clip.set_audio(speech_clip.audio)])

    # Salva o vídeo final
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Define o caminho da imagem de entrada
input_image = "input.jpg"

# Define o caminho do vídeo de saída
output_video = "output.mp4"

# Define o texto a ser convertido em fala
text = "Olá, mundo!"

# Cria o vídeo animado com o rosto falante
create_talking_video(input_image, output_video, text)
