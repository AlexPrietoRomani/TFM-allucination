import torch

print("--- Diagnóstico de Aceleración ---")
print(f"Versión de PyTorch: {torch.__version__}")
print(f"¿CUDA detectado por PyTorch?: {'✅ SÍ' if torch.cuda.is_available() else '❌ NO'}")

if torch.cuda.is_available():
    print(f"GPU Activa: {torch.cuda.get_device_name(0)}")