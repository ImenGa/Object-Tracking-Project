import pandas as pd
import matplotlib.pyplot as plt

def afficher_courbes_performance_csv(fichier_csv):
    # Lecture des données depuis le fichier CSV
    try:
        data = pd.read_csv(fichier_csv)
        
        # Vérification si les colonnes attendues existent dans le fichier CSV
        if 'epoch' in data.columns and 'metrics/precision(B)' in data.columns and 'metrics/recall(B)' in data.columns and \
           'metrics/mAP50(B)' in data.columns and 'metrics/mAP50-95(B)' in data.columns and \
           'train/box_loss' in data.columns and 'val/box_loss' in data.columns:
            
            # Extractionles valeurs des différentes colonnes
            epochs = data['epoch']
            train_loss = data['train/box_loss']  # Utilisation de la perte d'entraînement
            val_loss = data['val/box_loss']  # Utilisation de la perte de validation
            precision = data['metrics/precision(B)']
            recall = data['metrics/recall(B)']
            mAP_50 = data['metrics/mAP50(B)']
            mAP_50_95 = data['metrics/mAP50-95(B)']
            
            # Tracage les courbes de performance
            plt.figure(figsize=(14, 10))

            # Tracage de la courbe de la perte d'entraînement (train loss) et de validation (val loss)
            plt.subplot(2, 2, 1)
            plt.plot(epochs, train_loss, label="Train Loss", color='blue')
            plt.plot(epochs, val_loss, label="Validation Loss", color='orange')
            plt.xlabel("Epoch")
            plt.ylabel("Loss")
            plt.title("Train & Validation Loss")
            plt.legend()
            plt.grid(True)

            # Tracage de la courbe de la précision
            plt.subplot(2, 2, 2)
            plt.plot(epochs, precision, label="Precision", color='green')
            plt.xlabel("Epoch")
            plt.ylabel("Precision")
            plt.title("Precision")
            plt.grid(True)

            # Tracage de la courbe du Recall
            plt.subplot(2, 2, 3)
            plt.plot(epochs, recall, label="Recall", color='red')
            plt.xlabel("Epoch")
            plt.ylabel("Recall")
            plt.title("Recall")
            plt.grid(True)

            # Tracage de la courbe du mAP
            plt.subplot(2, 2, 4)
            plt.plot(epochs, mAP_50, label="mAP @ 50", color='blue')
            plt.plot(epochs, mAP_50_95, label="mAP @ 50-95", color='orange')
            plt.xlabel("Epoch")
            plt.ylabel("mAP")
            plt.title("mAP (mean Average Precision)")
            plt.legend()
            plt.grid(True)

            # Affichage les courbes
            plt.tight_layout()
            plt.show()

        else:
            print("Le fichier CSV ne contient pas les colonnes nécessaires pour afficher les courbes.")
    
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV : {e}")

# Remplacez ce chemin par le fichier CSV généré lors de l'entraînement
fichier_csv = r"C:\Users\etudiant\Desktop\object_tracking_model4\results.csv"
afficher_courbes_performance_csv(fichier_csv)
