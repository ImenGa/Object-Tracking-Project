import cv2
video_path= "./Dataset/test_videos/001bad4e-2fa8f3b6.mp4"
cap = cv2.VideoCapture(video_path)

# Vérification si la vidéo a bien été ouverte
if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la vidéo.")
    exit()

while True:
    # Lecture  d'une frame de la vidéo
    ret, frame = cap.read()

    # Si la frame a été lue correctement, ret sera True
    if not ret:
        print("Fin de la vidéo ou erreur de lecture.")
        break

    # Affichage de la frame dans une fenêtre
    cv2.imshow('Video', frame)

    # Attendre 1 ms pour voir si une touche a été pressée. 'q' pour quitter.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libération de la capture et fermer toutes les fenêtres
cap.release()
cv2.destroyAllWindows()

# Vérification si la vidéo a bien été ouverte
if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la vidéo.")
    exit()

while True:
    # Lecture d'une frame de la vidéo
    ret, frame = cap.read()

    # Si la frame a été lue correctement, ret sera True
    if not ret:
        print("Fin de la vidéo ou erreur de lecture.")
        break

    # Affichage de la frame dans une fenêtre
    cv2.imshow('Video', frame)

    # Attendre 1 ms pour voir si une touche a été pressée. 'q' pour quitter.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libération de la capture et fermer toutes les fenêtres
cap.release()
cv2.destroyAllWindows()
