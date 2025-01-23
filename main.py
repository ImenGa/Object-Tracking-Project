import shutil
import matplotlib.pyplot as plt
from ultralytics import YOLO

# Chemin vers le fichier .yaml et le dossier cible sur le Bureau
data_yaml_path = r"C:\Users\etudiant\Desktop\Object_Tracking\Object_Tracking.v1i.yolov8\data.yaml"
desktop_path = r"C:\Users\etudiant\Desktop\object_tracking_model"  

# Chargement du modèle YOLOv8 pré-entraîné
model = YOLO("yolov8n.pt") 

# Lancer l'entraînement
train_params = {
    "data": data_yaml_path,    # Chemin vers le fichier .yaml
    "epochs": 25,           # Nombre d'époques
    "imgsz": 640,             # Taille des images
    "batch": 16,              # Taille du batch
    "name": desktop_path,     # Sauvegarder les résultats sur le Bureau
    "workers": 4              # Nombre de threads pour le chargeent des données
}

print(f"Entraînement en cours... Les résultats seront sauvegardés dans : {desktop_path}")
model.train(**train_params)

# Déplacement des résultats vers le Bureau si nécessaire
source_path = f"runs/detect/{desktop_path.split('/')[-1]}"
shutil.move(source_path, desktop_path)
print(f"Résultats déplacés vers : {desktop_path}")

# Visualisation des graphes
results_png_path = f"{desktop_path}/results.png"  # Chemin du graphique des performances
try:
    img = plt.imread(results_png_path)  # Charger le graphique
    plt.figure(figsize=(10, 8))
    plt.imshow(img)
    plt.axis('off')
    plt.title("Courbes de performance YOLOv8")
    plt.show()
except FileNotFoundError:
    print(f"Graphique non trouvé à {results_png_path}. Vérifiez que l'entraînement s'est bien terminé.")

# Chemin vers le modèle final
best_model_path = f"{desktop_path}/weights/best.pt"
print(f"Modèle entraîné disponible ici : {best_model_path}")
