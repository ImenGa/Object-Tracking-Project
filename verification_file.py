import pandas as pd
import os

# Chargement des annotations
annotations_file = "./Dataset/mot_labels.csv"
labels = pd.read_csv(annotations_file, low_memory=False)

# Vérification des colonnes disponibles
print("Colonnes disponibles :", labels.columns)

# Filtrage pour une vidéo spécifique
video_name = "000d4f89-3bcbe37a" 
video_labels = labels.query(f'videoName == "{video_name}"')

# Création de la colonne 'video_frame'
fps = 30  # Ajuste en fonction de tes données réelles
video_labels["video_frame"] = (video_labels["frameIndex"] // fps).astype("int")
print(video_labels[["frameIndex", "video_frame"]].head())

# Vérification des frames disponibles
images_dir = "./Dataset/images"
frames = os.listdir(images_dir)
print(f"Frames disponibles ({len(frames)}):", frames[:10])

# Comparaison avec les frames annotées
frame_to_check = video_labels["video_frame"].iloc[0]  
print(f"Frame annotée pour vérifier : {frame_to_check}")
