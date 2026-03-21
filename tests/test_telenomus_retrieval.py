"""
test_telenomus_retrieval.py — Prueba de Recuperación Vectorial (Retrieval)

Consulta al motor RAG un enunciado sobre control de plagas (`Telenomus podisi`)
para verificar si los documentos correctos aparecen en el Top-K resultados.
"""

import sys
import os

# Add root to pythonpath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.chat.rag import RAGEngine
from src.core.config.settings import settings

def test_retrieval():
    output = []
    output.append(f"--- TEST DE RECUPERACIÓN VECTORIAL ---")
    output.append(f"Query: 'como puedo combatir con Telenomus podisi en mi huerto?, dime los ingredientes activos que puedo utilizar'")
    output.append(f"Modelo Embeddings Configurado: {settings.default_embedding_model}")
    output.append("-" * 50)
    
    try:
        rag = RAGEngine()
        # Verificar dimensión del embedding
        test_vec = rag.embeddings.embed_query("test")
        output.append(f"Dimensión del vector generado: {len(test_vec)}")
        
        # Retrieval
        question = "como puedo combatir con Telenomus podisi en mi huerto?, dime los ingredientes activos que puedo utilizar"
        docs = rag.retrieve_context(question)
        
        output.append(f"\nDocumentos Recuperados ({len(docs)}):")
        found_target = False
        
        for i, doc in enumerate(docs):
            source_id = doc.metadata.get('source_id', 'N/A')
            title = doc.metadata.get('title', 'N/A')
            content_snippet = doc.page_content[:300].replace('\n', ' ')
            
            output.append(f"\n[{i+1}] ID: {source_id} | Título: {title}")
            output.append(f"    Snippet: {content_snippet}...")
            
            # Busqueda de terminos clave
            if "2403.05479" in str(source_id) or "Telenomus" in doc.page_content:
                found_target = True
                output.append(f"    --> ¡MATCH ENCONTRADO! (Telenomus o ID correcto)")
                
        if found_target:
            output.append("\n✅ ÉXITO: Se encontró información relevante sobre Telenomus.")
        else:
            output.append("\n⚠️ AVISO: No se encontró explícitamente el ID '2403.05479' o 'Telenomus' en los top results.")
            
    except Exception as e:
        output.append(f"\n❌ ERROR CRÍTICO: {e}")

    with open("tests/telenomus_results.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output))

if __name__ == "__main__":
    test_retrieval()
