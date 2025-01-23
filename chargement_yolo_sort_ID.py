
import sys
sys.path.append(r"C:\Users\etudiant\Desktop\Object_Tracking\sort")
import cv2
import numpy as np
from ultralytics import YOLO
from sort import Sort



# Chargement le modèle YOLOv8
model = YOLO(r"C:\Users\etudiant\Desktop\object_tracking_model\weights\best.pt")  # Remplacez par votre modèle

# Initialisation le tracker SORT
tracker = Sort()

# Ouverture de la vidéo ou la séquence d'images
video_path = r"C:\Users\etudiant\Desktop\Object_Tracking\Dataset\test_videos\001bad4e-2fa8f3b6.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    #  les détections avec YOLO
    results = model(frame)  # Résultats de YOLO

    # Extraction des boîtes de détection, avec [x1, y1, x2, y2, confidence]
    detections = []
    for det in results[0].boxes:
        x1, y1, x2, y2 = det.xyxy[0].tolist()
        confidence = det.conf[0].item()

        if confidence > 0.5:  # Seuil de confiance
            detections.append([x1, y1, x2, y2, confidence])

    # Conversion des détections en format que SORT attend
    detections = np.array(detections)

    # Application de  SORT pour obtenir les pistes
    tracks = tracker.update(detections)

    # Affichage des pistes
    for track in tracks:
        x1, y1, x2, y2, track_id = track
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, f'ID: {int(track_id)}', (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Affichage de  l'image avec les détections et le suivi
    cv2.imshow('Tracking', frame)

    # Quitter avec la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()