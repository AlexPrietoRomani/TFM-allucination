# Documentación de Métricas Implementadas

Este documento detalla las métricas utilizadas en el TFM para evaluar la calidad, fidelidad y relevancia de las respuestas generadas por los modelos LLM (V1 y V2).

## 1. Fidelidad (Faithfulness)

La **Fidelidad** mide si la respuesta generada se deriva puramente del contexto proporcionado (RAG), sin inventar información (alucinaciones). No evalúa si la respuesta es verdadera en el mundo real, sino si es consistente con los documentos recuperados.

### Metodología (LLM-as-a-Judge)

Se utiliza un LLM evaluador (Juez) que recibe:
1.  El **Contexto Recuperado** (fragmentos de documentos).
2.  La **Respuesta Generada**.

El Juez descompone la respuesta en afirmaciones y verifica cada una contra el contexto.

### Fórmula

$$
\text{Faithfulness} = \frac{|C_{soportadas}|}{|C_{total}|}
$$

Donde:
*   $C_{total}$ es el conjunto de todas las afirmaciones extraídas de la respuesta.
*   $C_{soportadas}$ es el subconjunto de afirmaciones que están explícitamente respaldadas por el contexto.

**Rango:** $[0.0, 1.0]$  
**Implementación:** `src/metrics/faithfulness.py`

---

## 2. Relevancia del Contexto (Context Relevance)

Esta métrica evalúa la calidad del sistema de recuperación (Retrieval). Mide qué proporción del contexto recuperado es realmente útil para responder la pregunta del usuario. Un puntaje bajo indica que se está "ensuciando" el contexto con información irrelevante (ruido).

### Fórmula

$$
\text{Context Relevance} = \frac{|S_{relevantes}|}{|S_{total}|}
$$

Donde:
*   $S_{total}$ son todas las oraciones o fragmentos en el contexto recuperado.
*   $S_{relevantes}$ son aquellas oraciones necesarias para responder la pregunta.

**Rango:** $[0.0, 1.0]$  
**Implementación:** `src/metrics/context_relevance.py`

---

## 3. FactScore (Factualidad Atómica)

**FactScore** es una métrica más granular diseñada para descomponer una respuesta larga en una serie de "hechos atómicos" y verificar cada uno individualmente. Es especialmente útil para detectar alucinaciones sutiles en respuestas complejas.

### Proceso de Cálculo

1.  **Extracción de Hechos Atómicos:**
    Un modelo lingüista ($M_{extract}$) procesa la respuesta $R$ y genera una lista de hechos atómicos $A = \{a_1, a_2, ..., a_n\}$.
    *Ejemplo:* "El arándano requiere pH 4.5 y suelo arenoso" $\rightarrow$ ["Requiere pH 4.5", "Requiere suelo arenoso"].

2.  **Verificación de Hechos:**
    Cada hecho atómico $a_i$ se verifica contra la base de conocimiento $K$ (el contexto recuperado) usando un modelo verificador ($M_{verify}$).
    
    $$
    V(a_i, K) = \begin{cases} 
    1 & \text{si } K \text{ soporta } a_i \\
    0 & \text{si no}
    \end{cases}
    $$

3.  **Cálculo Final:**

$$
\text{FactScore}(R) = \frac{1}{|A|} \sum_{i=1}^{|A|} V(a_i, K)
$$

**Rango:** $[0.0, 1.0]$ (Representa el porcentaje de hechos verdaderos).  
**Implementación:** `src/metrics/factscore.py` y `services/worker/tasks.py` (Versión asíncrona).

---

---

## 4. Precisión del Contexto (Context Precision)

**Context Precision** evalúa si los fragmentos de información relevante recuperados por el sistema RAG están posicionados en los primeros lugares de la lista de contexto. Es una medida basada en el orden (Ranking-aware).

### Metodología

1. El Juez analiza el fragmento $k$ y dictamina si es útil ($1$) o no ($0$).
2. Se calcula el **Average Precision (AP)**:

$$
\text{Context Precision} = \frac{1}{|S_{relevantes}|} \sum_{k=1}^{|S|} (\text{Precision}@k \times rel_k)
$$

Donde $\text{Precision}@k$ es la proporción de fragmentos relevantes hasta la posición $k$, y $rel_k \in \{0, 1\}$.

**Rango:** $[0.0, 1.0]$  
**Implementación:** `src/metrics/context_precision.py`

---

## 5. Relevancia de la Respuesta (Answer Relevancy)

Evalúa si la respuesta del asistente ataca directamente la pregunta del usuario sin incluir información irrelevante o evasivas. Se calcula mediante una rúbrica de calificación cualitativa de $0.0$ a $1.0$ ejecutada por el modelo Juez.

**Rango:** $[0.0, 1.0]$  
**Implementación:** `src/metrics/answer_relevancy.py`

---

## Comparativa de Versiones

| Métrica | V0 (Baseline) | V1 (RAG) | V2 (Agente) |
| :--- | :---: | :---: | :---: |
| **Latencia** | Baja | Media | Alta |
| **Fidelidad** | N/A | Medida post-gen | **Optimizada** |
| **Context Precision** | N/A | **Crítica para Matriz** | Crítica |
| **Answer Relevancy** | Alta | Varía | Alta |

---

*Referencia Técnica:* Las definiciones están alineadas con la literatura reciente sobre evaluación de RAG (RAGAS, DeepEval) y el concepto de FactScore (Min et al., 2023). El Juez robusto es `llama3.1` para evitar Sesgo de Confirmación.
