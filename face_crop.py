import face_recognition
from PIL import Image
import os

def crop_faces_in_folder(input_folder, output_folder):
    
    os.makedirs(output_folder, exist_ok=True)
    
    
    for filename in os.listdir(input_folder):
        
        input_image_path = os.path.join(input_folder, filename)
        
        # Controlla se il file è un'immagine supportata
        if input_image_path.endswith(('.jpg', '.jpeg')):
            # Esegui il crop delle facce per l'immagine attuale
            crop_faces(input_image_path, output_folder)

def crop_faces(image_path, output_folder):
  
    image = face_recognition.load_image_file(image_path)

    # Trova i volti nell'immagine
    face_locations = face_recognition.face_locations(image)

    # Crop e salva le facce come nuove immagini
    for i, face_location in enumerate(face_locations):
        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save(os.path.join(output_folder, f"{os.path.splitext(os.path.basename(image_path))[0]}_face_{i}.jpg"))

# Percorso della cartella di input
input_folder = "prova"

# Cartella di output per le facce croppate
output_folder = "cartella_di_output"

# Esegui il crop delle facce per ogni foto nella cartella di input
crop_faces_in_folder(input_folder, output_folder)

