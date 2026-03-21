# 🧠 Modelos de Lenguaje aplicados a la Agricultura: Documentación y Arquitectura

Este documento proporciona una revisión a fondo del Trabajo de Fin de Máster (TFM) focalizado en erradicar y mitigar alucinaciones de Modelos de Lenguaje (LLM) aplicados a casos agronómicos, específicamente en consultas de fitosanidad y arándanos.

---

## 0. Pre-procesamiento del Corpus (Ingesta Estructurada)

Antes de que cualquier fase (V0, V1, V2) pueda operar, el corpus de documentos técnicos debe ser procesado e indexado. El problema central es que los PDFs del dominio agrícola (FRAC, IRAC, SENASA) son **altamente tabulares** — si se extraen con métodos tradicionales (`PyPDFLoader`), las relaciones semánticas entre columnas se pierden completamente.

### ¿Por qué es necesario?

| Método | Resultado para tablas FRAC/IRAC |
|--------|--------------------------------|
| **PyPDFLoader** (texto plano) | Mezcla columnas, pierde relación ingrediente → grupo → código |
| **Docling** (estructura) | Preserva tablas en Markdown con `\|col\|` syntax |
| **Docling + Flattening** | Transforma cada fila en oración natural enriquecida |

### Pipeline de Ingesta

```mermaid
graph TD
    classDef step fill:#2d3748,stroke:#4a5568,stroke-width:1.5px,color:#e2e8f0;
    classDef parser fill:#2c7a7b,stroke:#4fd1c5,stroke-width:1.5px,color:#fff;
    classDef db fill:#2b6cb0,stroke:#63b3ed,stroke-width:1.5px,color:#fff;

    subgraph "🤖 Fase 0: Corpus Pre-procesamiento"
        PDF([📄 PDF Raw]):::step --> Docling[Docling Parser]:::parser
        Docling --> MD[Markdown Estructurado]:::step
        MD --> Flatten[TableFlattener]:::parser
        YAML([📋 registry.yaml]):::step --> Meta[Inyección Metadatos]:::step
        Flatten --> Meta
        Meta --> Parsed["📂 corpus/parsed (*.md)"]:::step
    end

    subgraph "🔋 Fase 1: Matriz de Indexación"
        Parsed --> Chunks{Chunks: 500, 1000, Semantic}:::step
        Chunks --> Embed[nomic / mxbai / qwen3]:::db
        Embed --> DB{Motor DB}:::db
        DB -->|Local| FA[(FAISS Local)]:::db
        DB -->|Local / Cloud| QD[(Qdrant DB)]:::db
    end
```

### 📌 Flujo Ideal de Inferencia Visual (Llama-3.2-Vision)

Para enriquecer los documentos `.md` con descripciones de imágenes/gráficas, el pipeline conceptual diseñado es el siguiente:

1. **Extracción Determinista**: Docling lee el PDF. Todo el texto y las tablas se extraen directamente a Markdown de forma rápida y 100% fiel al documento original.
2. **Detección de Imágenes**: Cuando Docling encuentra un gráfico, un esquema de un insecto o una curva de degradación de pesticidas, extrae esa región específica como un archivo de imagen recortado.
3. **Inferencia Visual (Llama-3.2-Vision)**: Solo esa imagen recortada se envía a Ollama con Llama-3.2-Vision, acompañada del texto que estaba antes y después de la imagen en el PDF (para darle anclaje factual). El prompt sería: *"Describe este gráfico técnico basándote en el texto circundante"*.
4. **Fusión**: La descripción en texto que devuelve Llama-3.2-Vision sustituye la etiqueta `<!-- image -->` en el archivo Markdown final.

*Nota: Esto combina la precisión del OCR determinista para el texto y las tablas, con la comprensión semántica de Llama-3.2-Vision para interpretar diagramas visuales.*

### Componentes Clave

- **`src/knowledge/parsers.py`** — Contiene `DoclingParser`, `TableFlattener` e `ImageFilter`
- **`scripts/preprocess_corpus.py`** — Script orquestador ejecutable antes del setup
- **`corpus/parsed/`** — Directorio de salida con `.md` pre-procesados

### Ejemplo de Flattening

Una fila de tabla FRAC como:

| FRAC Code | Chemical Group | Active Ingredient | Comments |
|-----------|---------------|-------------------|----------|
| 11 | QoI | azoxystrobin | Resistance common |

Se transforma en:

> *"Según FRAC Code List (2024), FRAC Code: 11, Chemical Group: QoI, Active Ingredient: azoxystrobin, Comments: Resistance common."*

Esta oración descriptiva captura la relación semántica completa, produciendo embeddings de alta calidad.

## 1. Visión General del Sistema y Arquitectura Core

El código fuente del sistema reside mayoritariamente en `src/`, dividido de tal manera que las responsabilidades están fuertemente aisladas:

*   **`src/core/`**: Configuración fundamental, definición del proveedor, fábrica y parseo del registro de herramientas y capacidades del LLM de `model_registry.json`. Gestiona los wrappers de modelo (Gemini, OpenRouter, Ollama local).
*   **`src/chat/`**: Contiene la lógica del **RAG (V1)** puro, implementando cadenas Retriever y Augmenters clásicos con `LangChain`.
*   **`src/agent/`**: Posee el diseño del **Agente (V2)** construido con `LangGraph`. Define el Grafo de Decisión y el flujo asincrónico para determinar ciclos de auto-corrección basados en heurísticas o validaciones de calidad.
*   **`src/knowledge/`**: Se enfoca en Ingesta y Recuperación (`Retrieval`). Administra procesos como parseo de PDF/XLSX hacia Qdrant y la lógica de Text Splitting vectorizado.
*   **`src/metrics/`**: Los validadores. Producen métricas duras como Relevancia, Faithfulness (fidelidad por LLM-as-a-judge) y **FactScore**, este último usado para contrastar la atomicidad de las sentencias del LLM contra el Vector DB.
*   **`eval/`** y **`reports/`**: Scripts síncronos y comparativos. Generan en `reports/*.md` comparaciones tabulares con datos empíricos de ejecución.

### Pipeline Global de Enrutamiento

El sistema evalúa la consulta del usuario y, dependiendo del modo seleccionado en la interfaz, enruta la petición hacia la fase correspondiente:

```mermaid
graph TD
    User([Usuario Agrónomo]) -->|Consulta sobre Plagas| InputGateway
    InputGateway --> Sidebar{Sidebar: Parámetros del Experimento}
    
    Sidebar -->|Selecciona| LLM[🧠 Modelo LLM]
    Sidebar -->|Selecciona| Embedding[🔋 Modelo Embedding]
    Sidebar -->|Selecciona| DB[(📂 Vector DB: Qdrant / FAISS)]:::db

    Sidebar --> Router{Selección de Pestaña/Modo}

    Router -->|Pestaña 1| FlowComp[Comparativa]
    Router -->|Pestaña 2| FlowV0[Fase V0: Baseline LLM]
    Router -->|Pestaña 3| FlowV1[Fase V1: RAG Estático]
    Router -->|Pestaña 4| FlowV2[Fase V2: Agente Autónomo]
    Router -->|Pestaña 5| FlowRep[Reportes & Eval]
    Router -->|Pestaña 6| FlowMatrix[Matriz de Experimentos]
    
    %% Indicación global de Métricas
    FlowV1 -.-> |Métricas calculadas Post-Gen| MetricsUI([📊 Métricas en Interfaz])
    FlowV2 -.-> |Métricas evaluadas In-Gen| MetricsUI
    FlowComp -.-> |Compara modelos y Métricas| MetricsUI
    FlowMatrix -.-> |Visualiza Benchmarks Cruzados| MetricsUI

    classDef db fill:#2b6cb0,stroke:#63b3ed,stroke-width:1.2px,color:#fff;
```

---

## 2. Fase V0: Baseline LLM (Sin Contexto)

La **Fase V0** representa la interacción pura con el Modelo de Lenguaje, sin conocimiento externo (Zero-Shot). El objetivo de esta fase es demostrar el estado de alucinación predeterminado de los modelos cuando enfrentan o desconocen escenarios locales específicos.

### Flujo de Ejecución V0

*   El usuario envía la consulta.
*   El modelo genera una respuesta basándose únicamente en sus pesos preentrenados.
*   **Métricas:** En esta vista no se calculan métricas complejas de validación estructurada durante el flujo, ya que sirve de punto de comparación puramente base. Se confía en la experimentación visual del usuario frente a V1 o V2.

```mermaid
graph TD
    %% Estilos Neutros y no chillones
    classDef step fill:#2d3748,stroke:#4a5568,stroke-width:2px,color:#e2e8f0;
    classDef llm fill:#2b6cb0,stroke:#63b3ed,stroke-width:2px,color:#fff;
    classDef alert fill:#c53030,stroke:#fc8181,stroke-width:1px,color:#fff,stroke-dasharray: 4;

    Init([Inicio V0]):::step --> Input[Captura de Pregunta]:::step
    Input --> PromptFormatter[Formateador de Prompt Básico]:::step
    PromptFormatter --> LLM_Raw[Petición al LLM]:::llm
    LLM_Raw --> Response(Respuesta Bruta generada):::step
    Response -.->|Alucinación Potencial| EndResponse([Fin V0]):::alert
```

---

## 3. Fase V1: RAG Estático (Retrieval-Augmented Generation)

La **Fase V1** integra un sistema de Búsqueda Vectorial Semántica. Antes de enviar el prompt al LLM, examina la base de datos (Qdrant) iterando hasta hallar los "chunks" (fragmentos) más correlacionados a la consulta agronómica.

### Flujo y Cálculo de Métricas en V1

*   Se formatea un prompt estricto prohibiendo el uso de conocimiento general y exigiendo soporte textual (referencia).
*   **Aparición de las Métricas:** Las métricas de Fidelidad (*Faithfulness*), Relevancia y *FactScore* se evalúan de forma síncrona **después** de generar la respuesta total al usuario. Sirven como instrumento de reporte pasivo, ilustrando al operario cuán fiable fue el RAG en esa respuesta, pero **no detienen ni autocorrigen** alucinaciones pre-entregas.

```mermaid
graph TD
    %% Estilos elegantes y profesionales
    classDef step fill:#2d3748,stroke:#4a5568,stroke-width:2px,color:#e2e8f0;
    classDef db fill:#2c7a7b,stroke:#4fd1c5,stroke-width:2px,color:#fff;
    classDef metrics fill:#6b46c1,stroke:#b794f4,stroke-width:2px,color:#fff;

    Init([Inicio V1]):::step --> Query[Captura de Pregunta]:::step
    Query --> Embed[Generar Embeddings de Pregunta]:::step
    Embed --> VectorDB[(Qdrant DB)]:::db
    VectorDB -->|Top K Chunks| RetrievedContext[Contexto Recuperado]:::step
    RetrievedContext --> Synthesize[Sintetizar Respuesta]:::step
    
    Synthesize --> LLM_Gen[Generación de Respuesta RAG]:::step
    LLM_Gen --> UI_Render(Mostrar Respuesta en UI):::step
    
    %% Flujo paralelo/posterior para Métricas
    UI_Render --> |1. Activa Cálculo manual| MetricCalc[Calcular Métricas Síncronas]:::metrics
    MetricCalc --> |2. Procesa Score| ShowMetrics(Mostrar Relevancia y FactScore):::metrics
    ShowMetrics --> EndResponse([Fin V1]):::step
```

---

## 4. Fase V2: Agente Autónomo (LangGraph) con Autocorrección

La **Fase V2** es el verdadero nivel cognitivo. Implanta un "Agente Cíclico" programado para desconfiar de sí mismo. Transforma las **métricas en reglas de enrutamiento interno** actuando como un supervisor autocrítico (AI self-reflection).

### Flujo y Evaluación Interna (NodeEvaluate) en V2

*   El Agente primero clasifica si la "Intención" del usuario es charlar o requiere una evaluación de la DB vectorizada.
*   Tras intentar un boceto/borrador de respuesta, entra en **`NodeEvaluate`**.
*   **Uso Activo de Métricas:** A diferencia de V1, V2 re-promptea al juez LLM midiendo el *Faithfulness*. Si la puntuación ("Score") detectada es inferior al umbral, se toma la "Razón de Alucinación" devuelta y se activa la transición **Self-Correction Loop**.
*   Se rechaza si el LLM extrajo dosis erróneas, productos cruzados o métodos inconexos con los documentos, propiciando un nuevo intento (hasta un límite de retries máximo). Sólo avanza y muestra al usuario si su pureza es validada.

```mermaid
graph TD
    %% Estilos Profesionales
    classDef step fill:#2d3748,stroke:#4a5568,stroke-width:2px,color:#e2e8f0;
    classDef db fill:#2c7a7b,stroke:#4fd1c5,stroke-width:2px,color:#fff;
    classDef metrics fill:#6b46c1,stroke:#b794f4,stroke-width:2px,color:#fff;
    classDef warning fill:#c05621,stroke:#f6ad55,stroke-width:2px,color:#fff;

    Init([Inicio V2]):::step --> AgentInit[Clasificar Intención]:::step
    
    AgentInit -->|Charla/Saludo| ChitChat[Respuesta ChitChat]:::step
    ChitChat --> EndResponse([Fin UI]):::step
    
    AgentInit -->|Consulta Técnica| NodeRetrieve[Recuperar Contexto Vector DB]:::step
    NodeRetrieve --> VectorDB[(Qdrant)]:::db
    VectorDB -.-> NodeRetrieve
    
    NodeRetrieve --> NodeGenerate[Generar Borrador Respuesta]:::step
    
    %% NodeEvaluate define el loop
    NodeGenerate --> NodeEvaluate{Calcular Faithfulness y FactScore Interno}:::metrics
    
    NodeEvaluate -->|Rechazado - Alucinación / Falso| NodeCorrect[Extraer Crítica y Self-Correction Loop]:::warning
    NodeCorrect --> |Re-intento| NodeGenerate
    
    NodeEvaluate -->|Aceptado - Factualmente Correcto| FinalAnswer[Liberar Respuesta Segura Textual]:::step
    FinalAnswer --> EndResponse
    
    subgraph Self_Reflection ["Iteración de Reintento Agéntico (Self-Reflection)"]
      NodeGenerate
      NodeEvaluate
      NodeCorrect
    end
```

---

## 5. Matriz de Experimentos y Evaluaciones Cruzadas

Para dar validez científica al TFM, se incluye un módulo de **Evaluación Cruzada (Matriz de Experimentos)** que aísla variables y mide el impacto de la precisión de recuperación vs el razonamiento del LLM.

### Arquitectura de la Matriz

*   **Variables de Entrada:**
    *   *Slicing:* 3 modelos de embeddings × 3 estrategias de chunking × 2 motores DB (FAISS y Qdrant local).
*   **Orquestación:** `eval/run_matrix_eval.py` itera permutaciones, inyecta el `vector_store` configurado en `RAGEngine` y computa las métricas de Calidad de Contexto y Fidelidad.
*   **Telemetría:** Mide y desglosa el tiempo de espera por llamada a base de datos vs. llamadas de inferencia LLM.

```mermaid
graph TD
    classDef step fill:#2d3748,stroke:#4a5568,stroke-width:1.5px,color:#e2e8f0;
    classDef metrics fill:#6b46c1,stroke:#b794f4,stroke-width:1.5px,color:#fff;
    classDef file fill:#2b6cb0,stroke:#63b3ed,stroke-width:1.5px,color:#fff;

    Params([🧬 Combinaciones: 3 Embeddings × 3 Chunks × 2 Motores DB]) --> Build[🔨 build_vector_matrix.py]:::step
    Build --> Index[(📂 Índices FAISS / Colecciones Qdrant)]:::step
    Index --> Eval[⚖️ run_matrix_eval.py]:::step
    Eval --> Juez[🤖 LLM-as-a-judge local]:::metrics
    Eval --> JSON([📄 Resultados JSONL + Telemetría]):::file
    JSON --> UI([🖥️ App.py: Pestaña Matriz - Dashboard]):::step
```

---

## Logros e Hitos del Plan (Estado: Finalizado Completamente)

Todas las implementaciones listadas en el `PLAN_HITOS_TFM.md` original han sido marcadas como cumplidas exitosamente:

1.  **Fundamentos Base:** Creación del protocolo de dataset empírico y Setup Core (Hito 0-1).
2.  **Interacciones Clásicas:** Baseline chat (V0) evaluando el nivel primitivo (Hito 3).
3.  **Knowledge e Indexer RAG:** Extracción documental y volcado multivector en Docker/Qdrant resolviendo la RAG estático V1 (Hitos 5-8).
4.  **Métricas LLM-as-a-judge:** Incorporación del motor medidor de FactScore, Relevancia y Fidelidad usando LLM offline.
5.  **Grafo de Mitigación V2 y Reportes Finales:** La creación en robusta LangGraph de mitigación autocorrectiva, empacándolo finalmente bajo un ambiente Multi-Contenedor (Streamlit+Worker+Ollama+Qdrant+Redis).

*(Nota: El plan detallado `PLAN_HITOS_TFM.md` original ha sido auditado permanentemente y migrado a la carpeta de archivo `docs/PLAN_HITOS_TFM.md` tras cumplir los requerimientos operacionales).*
