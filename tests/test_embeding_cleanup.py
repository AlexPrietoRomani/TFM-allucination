import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from langchain_ollama import OllamaEmbeddings
from src.core.config.settings import settings

def test_string(embeddings, name, text):
    try:
        embeddings.embed_query(text)
        print(f"✅ {name}: ÉXITO")
    except Exception as e:
        print(f"❌ {name}: FALLO ({e})")

def main():
    print("Iniciando Pruebas de Limpieza multilingual-e5-large...")
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text-v2-moe",
        base_url=settings.ollama_base_url
    )

    # Fragmento 1: Con <!-- image -->
    frag1_original = "<!-- image --> \n\n ## Blueberry Integrated Management Guide"
    frag1_cleaned = frag1_original.replace("<!-- image -->", "")

    # Fragmento 130: Con temperaturas..
    frag130_original = "spray or when temperatures are above 85 o F. Burning of foliage may occur during periods of warm temperatures.."
    frag130_cleaned = frag130_original.replace("..", ".")

    # Fragmento 957: Con weeds..
    frag957_original = "for containers and small in-ground operations. Control a wide array of annual broadleaf and grass weeds.."
    frag957_cleaned = frag957_original.replace("..", ".")

    print("\n--- Pruebas de <!-- image --> ---")
    test_string(embeddings, "Frag 1 Original", frag1_original)
    test_string(embeddings, "Frag 1 Limpiado", frag1_cleaned)

    print("\n--- Pruebas de Doble Punto '..' ---")
    test_string(embeddings, "Frag 130 Original", frag130_original)
    test_string(embeddings, "Frag 130 Limpiado (.. -> .)", frag130_cleaned)

    test_string(embeddings, "Frag 957 Original", frag957_original)
    test_string(embeddings, "Frag 957 Limpiado (.. -> .)", frag957_cleaned)

if __name__ == "__main__":
    main()
