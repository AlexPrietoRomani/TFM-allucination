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

## 2. Dataset y Evaluación Matricial
- **Question Bank**: Banco de preguntas estandarizado ("Golden Dataset") con respuestas esperadas.
- **Escala de Evaluación**: Análisis matricial de **3,554 pruebas** individuales, cubriendo todas las combinaciones de componentes.
- **Potencia Estadística**: Mínimo de **32 ejecuciones por combinación** (N=32) para asegurar validez representativa y mitigar la varianza estocástica de los LLMs.
- **Fuentes**: 
  - Normativa SENASA (Perú) y SAG (Chile).
  - Manuales técnicos (MIP, Fungicidas).
  - Literatura científica reciente (2023-2025).

## 3. Métricas de Evaluación (RAGAS Framework)
Se emplea un enfoque de **"Cuádruple Capa"** basado en el framework RAGAS, evaluado mediante el paradigma **LLM-as-a-Judge**:

1.  **Fidelidad (Faithfulness)**: 
    -   Mide la alucinación extrínseca verificando si cada afirmación de la respuesta está soportada por el contexto.
    -   Fórmula: $|Afirmaciones \ Soportadas| / |Afirmaciones \ Totales|$.

2.  **Relevancia de la Respuesta (Answer Relevancy)**:
    -   Evalúa si la respuesta aborda directamente la intención del usuario sin divagaciones.
    -   Penaliza respuestas incompletas o redundantes.

3.  **Precisión del Contexto (Context Precision)**:
    -   Evalúa la calidad del *ranking* del motor de búsqueda (Retriever).
    -   Verifica si los fragmentos relevantes aparecen en las primeras posiciones.

4.  **Relevancia del Contexto (Context Relevance)**:
    -   Mide la relación señal-ruido del contexto inyectado.
    -   Calcula qué proporción del texto recuperado es útil para resolver la consulta.

5.  **Métricas Operativas y de Rendimiento**:
    -   **Latencia Segmentada**: Medición en segundos de Recuperación (`LATENCY_RETRIEVAL_SEG`), Generación (`LATENCY_GENERATION_SEG`) y Total.
    -   **Costo Estimado (`COST_EST`)**: Gasto proyectado en USD por cada inferencia y evaluación.

> [!NOTE]
> La métrica **FactScore** fue descartada del protocolo final debido a su alta redundancia con *Faithfulness* en dominios de conocimiento cerrado y su inestabilidad técnica en evaluaciones masivas.

## 4. Metodología de Validación Estadística
Para garantizar que las diferencias observadas entre modelos no sean fruto del azar, se aplica el siguiente pipeline estadístico (conforme a `statistical_results.md`):

1.  **Análisis de Métricas RAGAS (No Paramétricas)**:
    -   **Prueba de Kruskal-Wallis**: Identifica si existen diferencias significativas globales en calidad.
    -   **Post-hoc de Dunn**: Comparativa por pares con corrección de **FDR-BH (Benjamini-Hochberg)** para controlar falsos positivos.
2.  **Análisis de Rendimiento (Paramétricas)**:
    -   **ANOVA de una vía**: Para latencia y costo (variables continuas).
    -   **T-Test con corrección FDR-BH**: Para determinar equivalencia con el líder de rendimiento.
3.  **Análisis de Correlación de Pearson**:
    -   Identifica *trade-offs* entre latencia, costo y calidad (ej: ¿un aumento en latencia correlaciona con mejor *faithfulness*?).

## 5. Ejecución de Pruebas
Las pruebas se ejecutan de forma automatizada mediante la interfaz unificada (Tab "Reportes & Eval"):
- **Selección de Corpus**: `eval/question_bank_v1.csv`
- **Configuración**: Selección de versiones (V0/V1/V2) y proveedor LLM.
- **Reporting**: Generación automática de tablas comparativas y archivos Markdown para la memoria final.

## 6. Criterios de Éxito
Se establecen los siguientes umbrales y objetivos para considerar la arquitectura RAG como optimizada:

- **Fidelidad Académica**: Puntuación de **Faithfulness ≥ 0.8** en las combinaciones finales de producción.
- **Eficiencia Respuesta**: Latencia de generación total **≤ 15 segundos** (Media).
- **Consistencia Estadística**: El modelo agente (V2) debe mostrar una mejora **estadísticamente significativa** (p-value < 0.05) frente a la línea base (V0) en métricas de fidelidad.
- **Compromiso Costo-Calidad**: Las correlaciones de Pearson deben demostrar que el incremento en costo e infraestructura (ej. modelos de 20b vs 8b) produce un incremento marginal proporcional en la precisión (`Context Precision`).
