import cv2
import os

# Chemins des dossiers
videos_dir = "./Dataset/test_videos"  # Dossier contenant les vidéos à traiter
output_dir = "./Dataset/test_videos_frames"  # Dossier pour enregistrer les frames extraites

# Création le dossier de sortie s'il n'existe pas
os.makedirs(output_dir, exist_ok=True)

# Lister les fichiers vidéo dans le dossier "test_videos"
videos = [f for f in os.listdir(videos_dir) if f.endswith(".mp4")]  # Choisir les fichiers .mp4

# Limitation à 10 vidéos
videos = videos[:5]

# Extraction des frames de chaque vidéo
for video_file in videos:
    video_path = os.path.join(videos_dir, video_file)
    cap = cv2.VideoCapture(video_path)

    # Vérification que la vidéo a été correctement ouverte
    if not cap.isOpened():
        print(f"Impossible d'ouvrir la vidéo {video_file}")
        continue

    # Extraction et sauvegarder les frames
    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Fin de la vidéo

        # Sauvegarde de la frame dans le dossier de sortie
        frame_filename = f"{video_file}_frame_{frame_idx:04d}.jpg"
        frame_path = os.path.join(output_dir, frame_filename)
        cv2.imwrite(frame_path, frame)
        
        frame_idx += 1

    cap.release()
    print(f"Frames extraites de {video_file} et enregistrées dans {output_dir}")

print("Extraction des frames terminée.")
