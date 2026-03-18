# 🧠 Modelos de Lenguaje aplicados a la Agricultura: Documentación y Arquitectura

Este documento proporciona una revisión a fondo del Trabajo de Fin de Máster (TFM) focalizado en erradicar y mitigar alucinaciones de Modelos de Lenguaje (LLM) aplicados a casos agronómicos, específicamente en consultas de fitosanidad y arándanos.

## Estructura Core del Proyecto

El código fuente del sistema reside mayoritariamente en `src/`, dividido de tal manera que las responsabilidades están fuertemente aisladas:

*   **`src/core/`**: Configuración fundamental, definición del proveedor, fábrica y parseo del registro de herramientas y capacidades del LLM de `model_registry.json`. Gestiona los wrappers de modelo (Gemini, OpenRouter, Ollama local).
*   **`src/chat/`**: Contiene la lógica del **RAG (V1)** puro, implementando cadenas Retriever y Augmenters clásicos con `LangChain`.
*   **`src/agent/`**: Posee el diseño del **Agente (V2)** construido con `LangGraph`. Define el Grafo de Decisión y el flujo asincrónico para determinar ciclos de auto-corrección basados en heurísticas o validaciones de calidad.
*   **`src/knowledge/`**: Se enfoca en Ingesta y Recuperación (`Retrieval`). Administra procesos como parseo de PDF/XLSX (vía loaders polimórficos) hacia Qdrant y la lógica de Text Splitting vectorizado (`nomic-embed-text` o equivalente d=768).
*   **`src/metrics/`**: Los validadores. Producen métricas duras como Relevancia, Faithfulness (fidelidad por LLM-as-a-judge) y **FactScore**, este último usado para contrastar la atomicidad de las sentencias del LLM contra el Vector DB.
*   **`eval/`** y **`reports/`**: Scripts síncronos y comparativos (Golden Dataset `question_bank_v1.csv`). Generan en `reports/*.md` comparaciones tabulares con datos empíricos de ejecución.

---

## Diagrama Funcional de Mitigación (Pipeline Global)

El siguiente gráfico de flujo dictamina cómo funcionan los V0, V1 y primordialmente el V2 (Agente Autónomo), delineando el proceso de autoevaluación (Rechazo de respuesta/Aceptación) integrado a nivel estructural del **TFM**.

```mermaid
graph TD
    User([Usuario Agrónomo]) -->|Consulta sobre Plagas| InputGateway
    InputGateway --> Router{Modo Elegido}

    %% V0
    Router -->|V0 - Baseline| LLM_Raw[LLM sin Contexto]
    LLM_Raw --> Response(Respuesta Bruta)
    Response -.->|Alucinación Probable| EndResponse([Fin UI])

    %% V1
    Router -->|V1 - RAG| RAG_System[Motor RAG]
    RAG_System --> VectorDB[(Qdrant DB)]
    VectorDB -->|Chunk Relevante| RAG_System
    RAG_System --> Synthesize[Sintetizar Respuesta]
    Synthesize --> EndResponse

    %% V2
    Router -->|V2 - Agente LangGraph| AgentInit[Clasificar Intención]
    AgentInit --> NodeRetrieve[Recuperar Contexto Vector DB]
    NodeRetrieve --> VectorDB
    NodeRetrieve --> NodeGenerate[Borrador Respuesta]
    
    NodeGenerate --> NodeEvaluate{Evaluar Fidelidad y FactScore}
    
    NodeEvaluate -->|Rechazado - Alucinación / Falso| NodeCorrect[Self-Correction Loop]
    NodeCorrect --> NodeGenerate
    
    NodeEvaluate -->|Aceptado - Factualmente Correcto| FinalAnswer[Respuesta Segura Confiable]
    FinalAnswer --> EndResponse
    
    subgraph Iteración de Reintento Agéntico (V2)
      NodeGenerate
      NodeEvaluate
      NodeCorrect
    end
```

### ¿Qué se Acepta y Qué se Rechaza (V2)?

El sistema dictamina la validación en el bloque **NodeEvaluate**.  
*   **Se acepta:** Si cada afirmación atómica (evaluada vía lógica paramétrica FactScore y Faithfulness) está apoyada explícitamente y al 100% por los fragmentos recuperados de la DB Vectorial.
*   **Se rechaza:** Si el Generador del RAG deduce tratamientos paralelos, sugiere cuotas que no están en el texto recatado, alucina compuestos químicos basados en conocimiento pre-entrenado, o contradice la normativa listada en el registro `corpus/registry.yaml` (SENASA/EPA, etc). Se fuerza entonces una nueva generación rectificada (Self-Correction Loop).

---

## Logros e Hitos del Plan (Estado: Finalizado Completamente)

Todas las implementaciones listadas en el `PLAN_HITOS_TFM.md` original han sido marcadas como cumplidas exitosamente:

1.  **Fundamentos Base:** Creación del protocolo de dataset `question_bank_v1` empírico y Setup Core (Hito 0-1).
2.  **Interacciones Clásicas:** Baseline chat (V0) evaluando el nivel primitivo (Hito 3).
3.  **Knowledge e Indexer RAG:** Extracción documental y volcado multivector en Docker/Qdrant resolviendo la RAG estático V1 (Hitos 5-8).
4.  **Métricas LLM-as-a-judge:** Incorporación del motor medidor de FactScore, Relevancia y Fidelidad usando LLM offline (Hito 10-11 y Worker RQ #13).
5.  **Grafo de Mitigación V2 y Reportes Finales:** La creación en robusta LangGraph de mitigación autocorrectiva, empacándolo finalmente bajo un ambiente Multi-Contenedor (Streamlit+Worker+Ollama+Qdrant+Redis) (Hitos 12-15).

**(Nota: El plan detallado `PLAN_HITOS_TFM.md` original ha sido auditado permanentemente y migrado a la carpeta de archivo `docs/PLAN_HITOS_TFM.md` tras cumplir los requerimientos operacionales).**
