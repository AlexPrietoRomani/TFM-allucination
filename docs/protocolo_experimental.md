# Protocolo Experimental y Criterios de Éxito

## 1. Variantes Experimentales
- **V0: Chat Baseline (Control)**
  - Prompt directo al LLM (Zero-shot).
  - Sin acceso a documentación externa.
  - Representa el riesgo de usar LLMs "out-of-the-box".
- **V1: Chat RAG (Experimental)**
  - Recuperación Vectorial (Dense Retrieval) con Qdrant.
  - Inyección de contexto en prompt.
  - Citas obligatorias en respuesta.
- **V2: Agente RAG Autónomo (Mitigación Activa)**
  - Orquestación con **LangGraph**.
  - **Self-Correction Loop**: Verifica fidelidad (Faithfulness) antes de responder.
  - **Routing**: Clasifica intención (Query vs Chitchat) para optimizar recursos.
  - Reescritura iterativa si se detecta alucinación.

## 2. Dataset y Ground Truth
- **Question Bank**: 12 Preguntas "Gold Standard" de alta complejidad validadas manualmente.
- **Fuentes**: 
  - Normativa SENASA (Perú) y SAG (Chile).
  - Manuales técnicos (MIP, Fungicidas).
  - Papers científicos recientes (2023).

## 3. Métricas de Evaluación
Se usa un enfoque de "Triple Capa" (LLM-as-a-Judge):

1.  **Fidelidad (Faithfulness)**: 
    -   Métrica estilo DeepEval/G-Eval.
    -   Evalúa si la respuesta se deriva **exclusivamente** del contexto recuperado.
    -   Escala: 0.0 - 1.0.

2.  **Relevancia Contextual (Context Relevance)**:
    -   Evalúa si los documentos recuperados por el Retriever responden realmente a la pregunta del usuario.
    -   Detecta fallos en la etapa de Búsqueda Vectorial.

3.  **FactScore (Factualidad Atómica)**:
    -   Descompone la respuesta en afirmaciones atómicas (ej: "La dosis es 5ml").
    -   Verifica cada afirmación individualmente contra la evidencia.
    -   Score: % de afirmaciones soportadas.

4.  **Operativas**:
    -   Latencia (Tiempo de respuesta).
    -   Tasa de abstención (V2).

## 4. Ejecución de Pruebas
Las pruebas se ejecutan de forma automatizada mediante la interfaz unificada (Tab "Reportes & Eval"):
- **Selección de Corpus**: `eval/question_bank_v1.csv`
- **Configuración**: Selección de versiones (V0/V1/V2) y proveedor LLM.
- **Reporting**: Generación automática de tablas comparativas y archivos Markdown para la memoria final.

