import os
from llama_cpp import Llama

MODEL_PATH = os.path.join("models", "model.gguf")

def load_model():
    try:
        print(f"Loading model from: {MODEL_PATH}")
        return Llama(
            model_path=MODEL_PATH,
            n_ctx=2048,  # Context window size
            n_threads=4,  # Number of CPU threads
            n_gpu_layers=33  # Number of layers to offload to GPU
        )
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

model_instance = load_model()