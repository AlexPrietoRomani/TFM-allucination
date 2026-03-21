"""
test_integrated_pipeline.py — Test de Integración para el Pipeline de Ingesta

Simula el flujo completo de preprocess_document() para un único documento de prueba:
PDF -> Docling (fórmulas + OCR) -> ImageFilter VLM -> TableFlattener -> Metadata.

Guarda el Markdown resultante en tests/outputs/ para revisión visual.

Uso:
    uv run python tests/test_integrated_pipeline.py
"""

import sys
from pathlib import Path

# Añadir la raíz del proyecto al PATH
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.knowledge.parsers import DoclingParser, ImageFilter
from scripts.preprocess_corpus import preprocess_document

def main():
    print("--- 🔬 Iniciando Test Integrado de Pipeline (Docling + VLM + Fórmulas) ---")
    
    doc_meta = {
        "id": "arxiv-2205.07723",
        "title": "Interpretable Machine Learning for Pest Prediction",
        "year": "2022",
        "language": "en"
    }

    # Inicializar componentes del repo oficial
    parser = DoclingParser()
    image_filter = ImageFilter() # Utiliza llama3.2-vision por defecto
    
    print("\n--- ⏳ Procesando documento con preprocess_document()... ---")
    
    result = preprocess_document(
        doc_meta=doc_meta,
        parser=parser,
        flatten_tables=True,
        image_filter=image_filter
    )
    
    if result:
        # Crear carpeta de outputs si no existe
        out_dir = Path("tests/outputs")
        out_dir.mkdir(exist_ok=True)
        
        output_path = out_dir / "arxiv-2205.07723_integrated.md"
        output_path.write_text(result, encoding="utf-8")
        print(f"\n✅ Éxito absoluto: Archivo procesado y guardado en:\n    -> {output_path.resolve()}")
    else:
        print("\n❌ Error: preprocess_document() devolvió None o falló.")

if __name__ == "__main__":
    main()
