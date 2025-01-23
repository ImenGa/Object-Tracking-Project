import torch

if torch.cuda.is_available():
    print(f"CUDA disponible. Nom du GPU : {torch.cuda.get_device_name(0)}")
else:
    print("CUDA non disponible.")
