import subprocess
import os

# Dossier contenant les vidéos .mov
video_dir = r"C:\Users\etudiant\Desktop\Object_Tracking\Dataset\videos"
output_dir = r"C:\Users\etudiant\Desktop\Object_Tracking\Dataset\videos_mp4"

# Création du dossier de sortie 
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Liste les vidéos .mov
videos = [f for f in os.listdir(video_dir) if f.endswith(".mov")]

# Spécification du chemin complet de ffmpeg
ffmpeg_path = r"C:\Users\etudiant\Downloads\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe"  

# Convertion de chaque vidéo
for video in videos:
    input_path = os.path.join(video_dir, video)
    output_path = os.path.join(output_dir, video.replace(".mov", ".mp4"))

    # Commande pour convertir la vidéo
    command = [ffmpeg_path, "-i", input_path, "-vcodec", "libx264", "-acodec", "aac", output_path]

    # Exécution de la commande
    try:
        subprocess.run(command, check=True)
        print(f"Conversion réussie : {video}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la conversion de {video}: {e}")
