# Protocolo Experimental y Criterios de Éxito

## 1. Variantes Experimentales
- **V0: Chat Baseline**
  - Prompt directo al LLM.
  - Sin RAG.
  - Sin métricas de mitigación.
- **V1: Chat RAG**
  - Retrieval de chunks relevantes.
  - Prompt con contexto.
  - Citas obligatorias.
- **V2: RAG Agéntico con Mitigación**
  - Gating por incertidumbre (Semantic Entropy).
  - Verificación factual (FactScore).
  - Abstención activa ("No tengo suficiente información").

## 2. Dataset y Ground Truth
- **Question Bank**: 30-60 preguntas sobre "Manejo fitosanitario en arándano".
- **Ground Truth**: Respuesta ideal verificada para cada pregunta.

## 3. Métricas
- **Factualidad**: FactScore (proporción de afirmaciones atómicas soportadas).
- **Incertidumbre**: Entropía Semántica (consistencia entre generaciones estocásticas).
- **Operativas**: Latencia, Costo, Número de llamadas.
