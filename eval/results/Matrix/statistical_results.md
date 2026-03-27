# 📈 Informe de Análisis Estadístico del RAG
**Modelos objetivo:** deepseek-r1:8b, qwen2.5:3b, gpt-oss:20b
**Total de pruebas analizadas:** 3554

---
## 🛠️ Resumen de Metodología Aplicada
- **Métricas RAGAS ([0, 1]):** Pipeline No Paramétrico (Kruskal-Wallis → Dunn con corrección FDR-BH).
- **Métricas de Rendimiento (Latencia/Costo):** Pipeline Paramétrico (ANOVA de una vía → T-Test con corrección FDR-BH).
- **Interpretación CLD:** Componentes que comparten la misma letra (ej. 'a' y 'ab') son estadísticamente equivalentes.

---

## 🎯 Métrica: `LATENCY_RETRIEVAL_SEG`
> **Metodología:** PARAMÉTRICA (ANOVA)
> **Justificación:** Variable continua y sin límites fijos. Se asume normalidad por TLC (N=32).
> **Criterio de Éxito:** 🔽 **Menor es mejor** (Menor latencia/costo implica mayor eficiencia)

### 🔍 1. Análisis por Factor Individual (Univariante)
Determina si el cambio de un solo componente genera variaciones estadísticamente significativas.

#### 🔬 Factor: `Architecture`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |   Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|--------:|----------:|:---------------------|
| v0           |      96 | 0       |   0       | a                    |
| v1           |    1729 | 2.20687 |   2.04563 | b                    |
| v2           |    1729 | 2.29189 |   2.05207 | b                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| v1                      | 7.15348e-22 | No                     |
| v2                      | 1.95141e-23 | No                     |

#### 🔬 Factor: `Embedding`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente              |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:------------------------|--------:|---------:|----------:|:---------------------|
| N/A                     |      96 | 0        | 0         | a                    |
| mxbai-embed-large       |    1154 | 0.715985 | 0.0676435 | b                    |
| nomic-embed-text-v2-moe |    1152 | 1.1904   | 0.135564  | c                    |
| qwen3-embedding         |    1152 | 4.84443  | 4.70762   | d                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |      P-Value | Equivalente al Mejor   |
|:------------------------|-------------:|:-----------------------|
| mxbai-embed-large       | 1.84333e-13  | No                     |
| nomic-embed-text-v2-moe | 8.64134e-14  | No                     |
| qwen3-embedding         | 3.09345e-237 | No                     |

#### 🔬 Factor: `Chunk_strategy`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |   Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|--------:|----------:|:---------------------|
| N/A          |      96 | 0       |   0       | a                    |
| 1000         |    1152 | 2.23894 |   2.05416 | b                    |
| semantic     |    1154 | 2.24323 |   2.05513 | b                    |
| 500          |    1152 | 2.26599 |   2.04133 | b                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| 1000                    | 1.65009e-22 | No                     |
| semantic                | 5.14291e-22 | No                     |
| 500                     | 1.2649e-22  | No                     |

#### 🔬 Factor: `Db_motor`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |   Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|--------:|----------:|:---------------------|
| N/A          |      96 | 0       |   0       | a                    |
| faiss        |    1730 | 2.21325 |   2.02302 | b                    |
| qdrant_local |    1728 | 2.28556 |   2.07486 | b                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| faiss                   | 1.57074e-22 | No                     |
| qdrant_local            | 9.15869e-23 | No                     |

#### 🔬 Factor: `Generator`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente     |   Count |   Media |   Mediana | CLD (Agrupamiento)   |
|:---------------|--------:|--------:|----------:|:---------------------|
| deepseek-r1:8b |    1184 | 1.35774 |  0.107707 | a                    |
| qwen2.5:3b     |    1186 | 1.96286 |  0.11902  | b                    |
| gpt-oss:20b    |    1184 | 3.24565 |  3.26403  | c                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |      P-Value | Equivalente al Mejor   |
|:------------------------|-------------:|:-----------------------|
| qwen2.5:3b              | 7.17919e-10  | No                     |
| gpt-oss:20b             | 9.77349e-155 | No                     |

### 🧩 2. Análisis de Combinación Completa (Factorial)
- **ANOVA (Cross-tabulation):** P-Value = `0.000000`
- **Diferencias globales:** ✅ **SÍ**

**🚀 Top 5 Combinaciones Óptimas (según Media):**
| Combinación (Arquitectura | Embed | Chunk | DB | LLM)   |      Mean |    Median | Equivalencia   |
|:--------------------------------------------------------|----------:|----------:|:---------------|
| v0 | N/A | N/A | N/A | qwen2.5:3b                       | 0         | 0         | Líder          |
| v0 | N/A | N/A | N/A | deepseek-r1:8b                   | 0         | 0         | No             |
| v0 | N/A | N/A | N/A | gpt-oss:20b                      | 0         | 0         | No             |
| v1 | mxbai-embed-large | 1000 | faiss | deepseek-r1:8b  | 0.0273077 | 0.0268487 | No             |
| v2 | mxbai-embed-large | 1000 | faiss | deepseek-r1:8b  | 0.0275349 | 0.0258065 | No             |

**Otras combinaciones estadísticamente idénticas al líder:**
| Combinación                                                         |   p_value_vs_best |
|:--------------------------------------------------------------------|------------------:|
| v2 | mxbai-embed-large | 1000 | qdrant_local | deepseek-r1:8b       |         0.0561191 |
| v2 | nomic-embed-text-v2-moe | 1000 | qdrant_local | deepseek-r1:8b |         0.094671  |

---

## 🎯 Métrica: `LATENCY_GENERATION_SEG`
> **Metodología:** PARAMÉTRICA (ANOVA)
> **Justificación:** Variable continua y sin límites fijos. Se asume normalidad por TLC (N=32).
> **Criterio de Éxito:** 🔽 **Menor es mejor** (Menor latencia/costo implica mayor eficiencia)

### 🔍 1. Análisis por Factor Individual (Univariante)
Determina si el cambio de un solo componente genera variaciones estadísticamente significativas.

#### 🔬 Factor: `Architecture`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|---------:|----------:|:---------------------|
| v1           |    1729 |  9.34829 |   7.92154 | a                    |
| v0           |      96 | 12.3127  |   9.35873 | a                    |
| v2           |    1729 | 22.5659  |  18.7521  | b                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| v0                      | 0.0952181   | Sí                     |
| v2                      | 1.79952e-68 | No                     |

#### 🔬 Factor: `Embedding`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente              |   Count |   Media |   Mediana | CLD (Agrupamiento)   |
|:------------------------|--------:|--------:|----------:|:---------------------|
| N/A                     |      96 | 12.3127 |   9.35873 | a                    |
| mxbai-embed-large       |    1154 | 12.9794 |  11.2155  | a                    |
| nomic-embed-text-v2-moe |    1152 | 15.1001 |  13.0111  | b                    |
| qwen3-embedding         |    1152 | 19.797  |  16.0606  | c                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |   P-Value | Equivalente al Mejor   |
|:------------------------|----------:|:-----------------------|
| mxbai-embed-large       | 0.728184  | Sí                     |
| nomic-embed-text-v2-moe | 0.167424  | Sí                     |
| qwen3-embedding         | 0.0103314 | No                     |

#### 🔬 Factor: `Chunk_strategy`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.133903`
- **¿Diferencia Significativa?:** ❌ **NO**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |   Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|--------:|----------:|:---------------------|
| N/A          |      96 | 12.3127 |   9.35873 | a                    |
| 500          |    1152 | 15.1461 |  12.8387  | a                    |
| 1000         |    1152 | 15.922  |  12.9041  | a                    |
| semantic     |    1154 | 16.8017 |  13.7392  | a                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |   P-Value | Equivalente al Mejor   |
|:------------------------|----------:|:-----------------------|
| 500                     | 0.0291888 | No                     |
| 1000                    | 0.142407  | Sí                     |
| semantic                | 0.129206  | Sí                     |

#### 🔬 Factor: `Db_motor`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.227475`
- **¿Diferencia Significativa?:** ❌ **NO**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |   Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|--------:|----------:|:---------------------|
| N/A          |      96 | 12.3127 |   9.35873 | a                    |
| faiss        |    1730 | 15.6842 |  12.8874  | a                    |
| qdrant_local |    1728 | 16.2303 |  13.3293  | a                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |   P-Value | Equivalente al Mejor   |
|:------------------------|----------:|:-----------------------|
| faiss                   | 0.0367072 | No                     |
| qdrant_local            | 0.174374  | Sí                     |

#### 🔬 Factor: `Generator`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente     |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:---------------|--------:|---------:|----------:|:---------------------|
| qwen2.5:3b     |    1186 |  6.09854 |   3.38559 | a                    |
| deepseek-r1:8b |    1184 | 14.9825  |  12.2718  | b                    |
| gpt-oss:20b    |    1184 | 26.5115  |  25.7286  | c                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| deepseek-r1:8b          | 7.20893e-19 | No                     |
| gpt-oss:20b             | 0           | No                     |

### 🧩 2. Análisis de Combinación Completa (Factorial)
- **ANOVA (Cross-tabulation):** P-Value = `0.000000`
- **Diferencias globales:** ✅ **SÍ**

**🚀 Top 5 Combinaciones Óptimas (según Media):**
| Combinación (Arquitectura | Embed | Chunk | DB | LLM)         |     Mean |   Median | Equivalencia   |
|:--------------------------------------------------------------|---------:|---------:|:---------------|
| v1 | mxbai-embed-large | 1000 | faiss | qwen2.5:3b            | 0.885062 | 0.719902 | Líder          |
| v1 | mxbai-embed-large | semantic | faiss | qwen2.5:3b        | 0.940612 | 0.743443 | Sí             |
| v1 | mxbai-embed-large | 1000 | qdrant_local | qwen2.5:3b     | 0.942318 | 0.725756 | Sí             |
| v1 | mxbai-embed-large | semantic | qdrant_local | qwen2.5:3b | 0.998716 | 0.779778 | Sí             |
| v1 | nomic-embed-text-v2-moe | semantic | faiss | qwen2.5:3b  | 1.02285  | 0.906705 | Sí             |

**Otras combinaciones estadísticamente idénticas al líder:**
| Combinación                                                         |   p_value_vs_best |
|:--------------------------------------------------------------------|------------------:|
| v1 | mxbai-embed-large | semantic | faiss | qwen2.5:3b              |          0.684327 |
| v1 | mxbai-embed-large | 1000 | qdrant_local | qwen2.5:3b           |          0.694895 |
| v1 | mxbai-embed-large | semantic | qdrant_local | qwen2.5:3b       |          0.409476 |
| v1 | nomic-embed-text-v2-moe | semantic | faiss | qwen2.5:3b        |          0.208625 |
| v1 | nomic-embed-text-v2-moe | semantic | qdrant_local | qwen2.5:3b |          0.147173 |

---

## 🎯 Métrica: `TOTAL_LATENCY_SEG`
> **Metodología:** PARAMÉTRICA (ANOVA)
> **Justificación:** Variable continua y sin límites fijos. Se asume normalidad por TLC (N=32).
> **Criterio de Éxito:** 🔽 **Menor es mejor** (Menor latencia/costo implica mayor eficiencia)

### 🔍 1. Análisis por Factor Individual (Univariante)
Determina si el cambio de un solo componente genera variaciones estadísticamente significativas.

#### 🔬 Factor: `Architecture`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |   Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|--------:|----------:|:---------------------|
| v1           |    1729 | 11.5552 |  10.7432  | a                    |
| v0           |      96 | 12.3127 |   9.35873 | a                    |
| v2           |    1729 | 24.8578 |  22.1654  | b                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| v0                      | 0.677407    | Sí                     |
| v2                      | 1.35464e-65 | No                     |

#### 🔬 Factor: `Embedding`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente              |   Count |   Media |   Mediana | CLD (Agrupamiento)   |
|:------------------------|--------:|--------:|----------:|:---------------------|
| N/A                     |      96 | 12.3127 |   9.35873 | a                    |
| mxbai-embed-large       |    1154 | 13.6954 |  11.495   | a                    |
| nomic-embed-text-v2-moe |    1152 | 16.2905 |  13.2024  | b                    |
| qwen3-embedding         |    1152 | 24.6414 |  20.4999  | c                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| mxbai-embed-large       | 0.480433    | Sí                     |
| nomic-embed-text-v2-moe | 0.0580115   | Sí                     |
| qwen3-embedding         | 2.50574e-05 | No                     |

#### 🔬 Factor: `Chunk_strategy`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.029945`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |   Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|--------:|----------:|:---------------------|
| N/A          |      96 | 12.3127 |   9.35873 | a                    |
| 500          |    1152 | 17.4121 |  14.9611  | b                    |
| 1000         |    1152 | 18.1609 |  15.1165  | ab                   |
| semantic     |    1154 | 19.045  |  16.0771  | ab                   |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |    P-Value | Equivalente al Mejor   |
|:------------------------|-----------:|:-----------------------|
| 500                     | 0.00029989 | No                     |
| 1000                    | 0.0199861  | No                     |
| semantic                | 0.0258645  | No                     |

#### 🔬 Factor: `Db_motor`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.035319`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |   Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|--------:|----------:|:---------------------|
| N/A          |      96 | 12.3127 |   9.35873 | a                    |
| faiss        |    1730 | 17.8975 |  15.4774  | b                    |
| qdrant_local |    1728 | 18.5159 |  15.2038  | ab                   |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |    P-Value | Equivalente al Mejor   |
|:------------------------|-----------:|:-----------------------|
| faiss                   | 0.00112065 | No                     |
| qdrant_local            | 0.0344742  | No                     |

#### 🔬 Factor: `Generator`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente     |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:---------------|--------:|---------:|----------:|:---------------------|
| qwen2.5:3b     |    1186 |  8.06141 |   3.47311 | a                    |
| deepseek-r1:8b |    1184 | 16.3402  |  13.2909  | b                    |
| gpt-oss:20b    |    1184 | 29.7571  |  29.0171  | c                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| deepseek-r1:8b          | 4.94478e-16 | No                     |
| gpt-oss:20b             | 0           | No                     |

### 🧩 2. Análisis de Combinación Completa (Factorial)
- **ANOVA (Cross-tabulation):** P-Value = `0.000000`
- **Diferencias globales:** ✅ **SÍ**

**🚀 Top 5 Combinaciones Óptimas (según Media):**
| Combinación (Arquitectura | Embed | Chunk | DB | LLM)         |     Mean |   Median | Equivalencia   |
|:--------------------------------------------------------------|---------:|---------:|:---------------|
| v1 | mxbai-embed-large | 1000 | faiss | qwen2.5:3b            | 0.913801 | 0.751718 | Líder          |
| v1 | mxbai-embed-large | semantic | faiss | qwen2.5:3b        | 0.975851 | 0.774701 | Sí             |
| v1 | mxbai-embed-large | 1000 | qdrant_local | qwen2.5:3b     | 1.00435  | 0.782384 | Sí             |
| v1 | mxbai-embed-large | semantic | qdrant_local | qwen2.5:3b | 1.07121  | 0.847835 | Sí             |
| v1 | nomic-embed-text-v2-moe | semantic | faiss | qwen2.5:3b  | 1.12113  | 1.01871  | Sí             |

**Otras combinaciones estadísticamente idénticas al líder:**
| Combinación                                                   |   p_value_vs_best |
|:--------------------------------------------------------------|------------------:|
| v1 | mxbai-embed-large | semantic | faiss | qwen2.5:3b        |         0.64946   |
| v1 | mxbai-embed-large | 1000 | qdrant_local | qwen2.5:3b     |         0.535472  |
| v1 | mxbai-embed-large | semantic | qdrant_local | qwen2.5:3b |         0.256481  |
| v1 | nomic-embed-text-v2-moe | semantic | faiss | qwen2.5:3b  |         0.0609243 |
| v1 | mxbai-embed-large | 1000 | qdrant_local | deepseek-r1:8b |         0.1832    |

---

## 🎯 Métrica: `COST_EST`
> **Metodología:** PARAMÉTRICA (ANOVA)
> **Justificación:** Variable continua y sin límites fijos. Se asume normalidad por TLC (N=32).
> **Criterio de Éxito:** 🔽 **Menor es mejor** (Menor latencia/costo implica mayor eficiencia)

### 🔍 1. Análisis por Factor Individual (Univariante)
Determina si el cambio de un solo componente genera variaciones estadísticamente significativas.

#### 🔬 Factor: `Architecture`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |      Media |    Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|-----------:|-----------:|:---------------------|
| v1           |    1729 | 0.00481465 | 0.00447634 | a                    |
| v0           |      96 | 0.00513028 | 0.00389947 | a                    |
| v2           |    1729 | 0.0103574  | 0.0092356  | b                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| v0                      | 0.677407    | Sí                     |
| v2                      | 1.35464e-65 | No                     |

#### 🔬 Factor: `Embedding`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente              |   Count |      Media |    Mediana | CLD (Agrupamiento)   |
|:------------------------|--------:|-----------:|-----------:|:---------------------|
| N/A                     |      96 | 0.00513028 | 0.00389947 | a                    |
| mxbai-embed-large       |    1154 | 0.00570642 | 0.0047896  | a                    |
| nomic-embed-text-v2-moe |    1152 | 0.00678772 | 0.00550099 | b                    |
| qwen3-embedding         |    1152 | 0.0102672  | 0.00854163 | c                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| mxbai-embed-large       | 0.480433    | Sí                     |
| nomic-embed-text-v2-moe | 0.0580115   | Sí                     |
| qwen3-embedding         | 2.50574e-05 | No                     |

#### 🔬 Factor: `Chunk_strategy`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.029945`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |      Media |    Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|-----------:|-----------:|:---------------------|
| N/A          |      96 | 0.00513028 | 0.00389947 | a                    |
| 500          |    1152 | 0.00725505 | 0.00623378 | b                    |
| 1000         |    1152 | 0.00756705 | 0.00629856 | ab                   |
| semantic     |    1154 | 0.0079354  | 0.00669878 | ab                   |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |    P-Value | Equivalente al Mejor   |
|:------------------------|-----------:|:-----------------------|
| 500                     | 0.00029989 | No                     |
| 1000                    | 0.0199861  | No                     |
| semantic                | 0.0258645  | No                     |

#### 🔬 Factor: `Db_motor`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.035319`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |      Media |    Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|-----------:|-----------:|:---------------------|
| N/A          |      96 | 0.00513028 | 0.00389947 | a                    |
| faiss        |    1730 | 0.00745728 | 0.00644892 | b                    |
| qdrant_local |    1728 | 0.00771495 | 0.00633492 | ab                   |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |    P-Value | Equivalente al Mejor   |
|:------------------------|-----------:|:-----------------------|
| faiss                   | 0.00112065 | No                     |
| qdrant_local            | 0.0344742  | No                     |

#### 🔬 Factor: `Generator`
- **Prueba Ómnibus (ANOVA):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente     |   Count |      Media |    Mediana | CLD (Agrupamiento)   |
|:---------------|--------:|-----------:|-----------:|:---------------------|
| qwen2.5:3b     |    1186 | 0.00335892 | 0.00144713 | a                    |
| deepseek-r1:8b |    1184 | 0.00680842 | 0.00553788 | b                    |
| gpt-oss:20b    |    1184 | 0.0123988  | 0.0120905  | c                    |

**Análisis de Equivalencia (T-Test (FDR-BH)):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| deepseek-r1:8b          | 4.94478e-16 | No                     |
| gpt-oss:20b             | 0           | No                     |

### 🧩 2. Análisis de Combinación Completa (Factorial)
- **ANOVA (Cross-tabulation):** P-Value = `0.000000`
- **Diferencias globales:** ✅ **SÍ**

**🚀 Top 5 Combinaciones Óptimas (según Media):**
| Combinación (Arquitectura | Embed | Chunk | DB | LLM)         |        Mean |      Median | Equivalencia   |
|:--------------------------------------------------------------|------------:|------------:|:---------------|
| v1 | mxbai-embed-large | 1000 | faiss | qwen2.5:3b            | 0.000380751 | 0.000313216 | Líder          |
| v1 | mxbai-embed-large | semantic | faiss | qwen2.5:3b        | 0.000406604 | 0.000322792 | Sí             |
| v1 | mxbai-embed-large | 1000 | qdrant_local | qwen2.5:3b     | 0.000418478 | 0.000325993 | Sí             |
| v1 | mxbai-embed-large | semantic | qdrant_local | qwen2.5:3b | 0.000446337 | 0.000353265 | Sí             |
| v1 | nomic-embed-text-v2-moe | semantic | faiss | qwen2.5:3b  | 0.000467137 | 0.000424462 | Sí             |

**Otras combinaciones estadísticamente idénticas al líder:**
| Combinación                                                   |   p_value_vs_best |
|:--------------------------------------------------------------|------------------:|
| v1 | mxbai-embed-large | semantic | faiss | qwen2.5:3b        |         0.64946   |
| v1 | mxbai-embed-large | 1000 | qdrant_local | qwen2.5:3b     |         0.535472  |
| v1 | mxbai-embed-large | semantic | qdrant_local | qwen2.5:3b |         0.256481  |
| v1 | nomic-embed-text-v2-moe | semantic | faiss | qwen2.5:3b  |         0.0609243 |
| v1 | mxbai-embed-large | 1000 | qdrant_local | deepseek-r1:8b |         0.1832    |

---

## 🎯 Métrica: `FAITHFULNESS`
> **Metodología:** NO PARAMÉTRICA (Kruskal-Wallis)
> **Justificación:** Variable acotada en [0, 1] con distribuciones frecuentemente asimétricas.
> **Criterio de Éxito:** 🔼 **Mayor es mejor** (Mayor puntuación implica mayor calidad RAG)

### 🔍 1. Análisis por Factor Individual (Univariante)
Determina si el cambio de un solo componente genera variaciones estadísticamente significativas.

#### 🔬 Factor: `Architecture`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|---------:|----------:|:---------------------|
| v1           |    1729 | 0.708155 |       0.5 | a                    |
| v2           |    1729 | 0.701417 |       0.8 | a                    |
| v0           |      96 | 0        |       0   | b                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| v2                      | 0.705204    | Sí                     |
| v0                      | 2.47434e-65 | No                     |

#### 🔬 Factor: `Embedding`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente              |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:------------------------|--------:|---------:|----------:|:---------------------|
| nomic-embed-text-v2-moe |    1152 | 0.748307 |       0.9 | a                    |
| qwen3-embedding         |    1152 | 0.722309 |       0.8 | a                    |
| mxbai-embed-large       |    1154 | 0.643847 |       0.5 | b                    |
| N/A                     |      96 | 0        |       0   | c                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| qwen3-embedding         | 0.0938824   | Sí                     |
| mxbai-embed-large       | 2.42175e-12 | No                     |
| N/A                     | 3.33348e-64 | No                     |

#### 🔬 Factor: `Chunk_strategy`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|---------:|----------:|:---------------------|
| 1000         |    1152 | 0.707422 |       0.5 | a                    |
| semantic     |    1154 | 0.705199 |       0.5 | a                    |
| 500          |    1152 | 0.701736 |       0.5 | a                    |
| N/A          |      96 | 0        |       0   | b                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| semantic                | 0.924506    | Sí                     |
| 500                     | 0.701441    | Sí                     |
| N/A                     | 2.04747e-60 | No                     |

#### 🔬 Factor: `Db_motor`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|---------:|----------:|:---------------------|
| faiss        |    1730 | 0.70763  |       0.5 | a                    |
| qdrant_local |    1728 | 0.701939 |       0.5 | a                    |
| N/A          |      96 | 0        |       0   | b                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| qdrant_local            | 0.753088    | Sí                     |
| N/A                     | 3.74503e-63 | No                     |

#### 🔬 Factor: `Generator`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.004610`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente     |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:---------------|--------:|---------:|----------:|:---------------------|
| gpt-oss:20b    |    1184 | 0.701098 |       0.9 | a                    |
| deepseek-r1:8b |    1184 | 0.691512 |       0.5 | a                    |
| qwen2.5:3b     |    1186 | 0.664671 |       0.5 | b                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |    P-Value | Equivalente al Mejor   |
|:------------------------|-----------:|:-----------------------|
| deepseek-r1:8b          | 0.346104   | Sí                     |
| qwen2.5:3b              | 0.00142384 | No                     |

### 🧩 2. Análisis de Combinación Completa (Factorial)
- **Kruskal-Wallis (Combinatorio):** P-Value = `0.000000`
- **Diferencias globales:** ✅ **SÍ**

**🚀 Top 5 Combinaciones Óptimas (según Media):**
| Combinación (Arquitectura | Embed | Chunk | DB | LLM)                |     Mean |   Median | Equivalencia   |
|:---------------------------------------------------------------------|---------:|---------:|:---------------|
| v2 | nomic-embed-text-v2-moe | 1000 | faiss | gpt-oss:20b            | 0.84375  |     1    | Líder          |
| v2 | nomic-embed-text-v2-moe | 500 | qdrant_local | deepseek-r1:8b   | 0.834375 |     1    | Sí             |
| v1 | nomic-embed-text-v2-moe | semantic | qdrant_local | gpt-oss:20b | 0.834375 |     0.95 | Sí             |
| v2 | nomic-embed-text-v2-moe | 1000 | qdrant_local | gpt-oss:20b     | 0.83125  |     1    | Sí             |
| v1 | nomic-embed-text-v2-moe | 1000 | faiss | gpt-oss:20b            | 0.83125  |     1    | Sí             |

**Otras combinaciones estadísticamente idénticas al líder:**
| Combinación                                                          |   p_value_vs_best |
|:---------------------------------------------------------------------|------------------:|
| v2 | nomic-embed-text-v2-moe | 500 | qdrant_local | deepseek-r1:8b   |          0.758312 |
| v1 | nomic-embed-text-v2-moe | semantic | qdrant_local | gpt-oss:20b |          0.346197 |
| v2 | nomic-embed-text-v2-moe | 1000 | qdrant_local | gpt-oss:20b     |          0.623565 |
| v1 | nomic-embed-text-v2-moe | 1000 | faiss | gpt-oss:20b            |          0.777016 |
| v2 | qwen3-embedding | 1000 | faiss | gpt-oss:20b                    |          0.641104 |

---

## 🎯 Métrica: `RELEVANCE`
> **Metodología:** NO PARAMÉTRICA (Kruskal-Wallis)
> **Justificación:** Variable acotada en [0, 1] con distribuciones frecuentemente asimétricas.
> **Criterio de Éxito:** 🔼 **Mayor es mejor** (Mayor puntuación implica mayor calidad RAG)

### 🔍 1. Análisis por Factor Individual (Univariante)
Determina si el cambio de un solo componente genera variaciones estadísticamente significativas.

#### 🔬 Factor: `Architecture`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|---------:|----------:|:---------------------|
| v1           |    1729 | 0.680625 |       0.5 | a                    |
| v2           |    1729 | 0.674899 |       0.5 | a                    |
| v0           |      96 | 0        |       0   | b                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| v2                      | 0.694944    | Sí                     |
| v0                      | 4.16227e-56 | No                     |

#### 🔬 Factor: `Embedding`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente              |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:------------------------|--------:|---------:|----------:|:---------------------|
| qwen3-embedding         |    1152 | 0.803299 |       1   | a                    |
| nomic-embed-text-v2-moe |    1152 | 0.779688 |       1   | a                    |
| mxbai-embed-large       |    1154 | 0.450693 |       0.5 | b                    |
| N/A                     |      96 | 0        |       0   | c                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |      P-Value | Equivalente al Mejor   |
|:------------------------|-------------:|:-----------------------|
| nomic-embed-text-v2-moe | 0.0385244    | No                     |
| mxbai-embed-large       | 4.03908e-109 | No                     |
| N/A                     | 2.09863e-75  | No                     |

#### 🔬 Factor: `Chunk_strategy`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|---------:|----------:|:---------------------|
| semantic     |    1154 | 0.688648 |       0.5 | a                    |
| 500          |    1152 | 0.683681 |       0.5 | a                    |
| 1000         |    1152 | 0.660937 |       0.5 | b                    |
| N/A          |      96 | 0        |       0   | c                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| 500                     | 0.813127    | Sí                     |
| 1000                    | 0.0247164   | No                     |
| N/A                     | 1.41801e-54 | No                     |

#### 🔬 Factor: `Db_motor`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|---------:|----------:|:---------------------|
| faiss        |    1730 | 0.678844 |       0.5 | a                    |
| qdrant_local |    1728 | 0.676678 |       0.5 | a                    |
| N/A          |      96 | 0        |       0   | b                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| qdrant_local            | 0.847956    | Sí                     |
| N/A                     | 6.92828e-56 | No                     |

#### 🔬 Factor: `Generator`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.937533`
- **¿Diferencia Significativa?:** ❌ **NO**

**Ranking de Rendimiento con CLD:**
| Componente     |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:---------------|--------:|---------:|----------:|:---------------------|
| deepseek-r1:8b |    1184 | 0.661149 |       0.5 | a                    |
| gpt-oss:20b    |    1184 | 0.658699 |       0.5 | a                    |
| qwen2.5:3b     |    1186 | 0.658516 |       0.5 | a                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |   P-Value | Equivalente al Mejor   |
|:------------------------|----------:|:-----------------------|
| gpt-oss:20b             |  0.865892 | Sí                     |
| qwen2.5:3b              |  0.718087 | Sí                     |

### 🧩 2. Análisis de Combinación Completa (Factorial)
- **Kruskal-Wallis (Combinatorio):** P-Value = `0.000000`
- **Diferencias globales:** ✅ **SÍ**

**🚀 Top 5 Combinaciones Óptimas (según Media):**
| Combinación (Arquitectura | Embed | Chunk | DB | LLM)       |   Mean |   Median | Equivalencia   |
|:------------------------------------------------------------|-------:|---------:|:---------------|
| v2 | qwen3-embedding | 500 | qdrant_local | qwen2.5:3b      |  0.875 |        1 | Líder          |
| v1 | qwen3-embedding | semantic | qdrant_local | qwen2.5:3b |  0.875 |        1 | Sí             |
| v2 | qwen3-embedding | 500 | qdrant_local | deepseek-r1:8b  |  0.875 |        1 | Sí             |
| v1 | nomic-embed-text-v2-moe | 1000 | faiss | gpt-oss:20b   |  0.875 |        1 | Sí             |
| v1 | qwen3-embedding | 500 | faiss | gpt-oss:20b            |  0.875 |        1 | Sí             |

**Otras combinaciones estadísticamente idénticas al líder:**
| Combinación                                                 |   p_value_vs_best |
|:------------------------------------------------------------|------------------:|
| v1 | qwen3-embedding | semantic | qdrant_local | qwen2.5:3b |          1        |
| v2 | qwen3-embedding | 500 | qdrant_local | deepseek-r1:8b  |          1        |
| v1 | nomic-embed-text-v2-moe | 1000 | faiss | gpt-oss:20b   |          0.833699 |
| v1 | qwen3-embedding | 500 | faiss | gpt-oss:20b            |          1        |
| v1 | qwen3-embedding | 1000 | faiss | deepseek-r1:8b        |          0.785603 |

---

## 🎯 Métrica: `CONTEXT_PRECISION`
> **Metodología:** NO PARAMÉTRICA (Kruskal-Wallis)
> **Justificación:** Variable acotada en [0, 1] con distribuciones frecuentemente asimétricas.
> **Criterio de Éxito:** 🔼 **Mayor es mejor** (Mayor puntuación implica mayor calidad RAG)

### 🔍 1. Análisis por Factor Individual (Univariante)
Determina si el cambio de un solo componente genera variaciones estadísticamente significativas.

#### 🔬 Factor: `Architecture`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|---------:|----------:|:---------------------|
| v1           |    1729 | 0.66043  |      0.75 | a                    |
| v2           |    1729 | 0.653968 |      0.7  | a                    |
| v0           |      96 | 0        |      0    | b                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| v2                      | 0.506193    | Sí                     |
| v0                      | 4.81061e-52 | No                     |

#### 🔬 Factor: `Embedding`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente              |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:------------------------|--------:|---------:|----------:|:---------------------|
| nomic-embed-text-v2-moe |    1152 | 0.770752 |    0.8667 | a                    |
| qwen3-embedding         |    1152 | 0.737099 |    0.8042 | b                    |
| mxbai-embed-large       |    1154 | 0.464081 |    0.45   | c                    |
| N/A                     |      96 | 0        |    0      | d                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |      P-Value | Equivalente al Mejor   |
|:------------------------|-------------:|:-----------------------|
| qwen3-embedding         | 0.000116114  | No                     |
| mxbai-embed-large       | 4.93622e-103 | No                     |
| N/A                     | 1.55544e-57  | No                     |

#### 🔬 Factor: `Chunk_strategy`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|---------:|----------:|:---------------------|
| 500          |    1152 | 0.678638 |    0.7556 | a                    |
| semantic     |    1154 | 0.660883 |    0.7    | a                    |
| 1000         |    1152 | 0.632069 |    0.7    | b                    |
| N/A          |      96 | 0        |    0      | c                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| semantic                | 0.214992    | Sí                     |
| 1000                    | 0.00197149  | No                     |
| N/A                     | 1.67319e-50 | No                     |

#### 🔬 Factor: `Db_motor`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|---------:|----------:|:---------------------|
| faiss        |    1730 | 0.661204 |       0.7 | a                    |
| qdrant_local |    1728 | 0.65319  |       0.7 | a                    |
| N/A          |      96 | 0        |       0   | b                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| qdrant_local            | 0.442034    | Sí                     |
| N/A                     | 4.53583e-52 | No                     |

#### 🔬 Factor: `Generator`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.852358`
- **¿Diferencia Significativa?:** ❌ **NO**

**Ranking de Rendimiento con CLD:**
| Componente     |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:---------------|--------:|---------:|----------:|:---------------------|
| gpt-oss:20b    |    1184 | 0.643433 |       0.7 | a                    |
| deepseek-r1:8b |    1184 | 0.639017 |       0.7 | a                    |
| qwen2.5:3b     |    1186 | 0.635897 |       0.7 | a                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |   P-Value | Equivalente al Mejor   |
|:------------------------|----------:|:-----------------------|
| deepseek-r1:8b          |  0.815016 | Sí                     |
| qwen2.5:3b              |  0.564916 | Sí                     |

### 🧩 2. Análisis de Combinación Completa (Factorial)
- **Kruskal-Wallis (Combinatorio):** P-Value = `0.000000`
- **Diferencias globales:** ✅ **SÍ**

**🚀 Top 5 Combinaciones Óptimas (según Media):**
| Combinación (Arquitectura | Embed | Chunk | DB | LLM)               |     Mean |   Median | Equivalencia   |
|:--------------------------------------------------------------------|---------:|---------:|:---------------|
| v2 | nomic-embed-text-v2-moe | semantic | qdrant_local | qwen2.5:3b | 0.851128 |  1       | Líder          |
| v2 | nomic-embed-text-v2-moe | 500 | qdrant_local | gpt-oss:20b     | 0.846144 |  0.93335 | Sí             |
| v1 | nomic-embed-text-v2-moe | semantic | faiss | qwen2.5:3b        | 0.838156 |  0.9167  | Sí             |
| v1 | qwen3-embedding | 500 | faiss | deepseek-r1:8b                 | 0.835856 |  0.8771  | Sí             |
| v1 | qwen3-embedding | 500 | qdrant_local | gpt-oss:20b             | 0.832947 |  0.8771  | Sí             |

**Otras combinaciones estadísticamente idénticas al líder:**
| Combinación                                                        |   p_value_vs_best |
|:-------------------------------------------------------------------|------------------:|
| v2 | nomic-embed-text-v2-moe | 500 | qdrant_local | gpt-oss:20b    |          0.369187 |
| v1 | nomic-embed-text-v2-moe | semantic | faiss | qwen2.5:3b       |          0.401537 |
| v1 | qwen3-embedding | 500 | faiss | deepseek-r1:8b                |          0.318002 |
| v1 | qwen3-embedding | 500 | qdrant_local | gpt-oss:20b            |          0.184666 |
| v2 | nomic-embed-text-v2-moe | 500 | qdrant_local | deepseek-r1:8b |          0.576716 |

---

## 🎯 Métrica: `ANSWER_RELEVANCY`
> **Metodología:** NO PARAMÉTRICA (Kruskal-Wallis)
> **Justificación:** Variable acotada en [0, 1] con distribuciones frecuentemente asimétricas.
> **Criterio de Éxito:** 🔼 **Mayor es mejor** (Mayor puntuación implica mayor calidad RAG)

### 🔍 1. Análisis por Factor Individual (Univariante)
Determina si el cambio de un solo componente genera variaciones estadísticamente significativas.

#### 🔬 Factor: `Architecture`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000650`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|---------:|----------:|:---------------------|
| v0           |      96 | 0.628125 |       0.5 | a                    |
| v2           |    1728 | 0.532928 |       0.5 | b                    |
| v1           |    1729 | 0.50428  |       0.5 | c                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| v2                      | 0.0152103   | No                     |
| v1                      | 0.000797148 | No                     |

#### 🔬 Factor: `Embedding`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente              |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:------------------------|--------:|---------:|----------:|:---------------------|
| N/A                     |      96 | 0.628125 |       0.5 | a                    |
| nomic-embed-text-v2-moe |    1152 | 0.599306 |       0.5 | a                    |
| qwen3-embedding         |    1152 | 0.581684 |       0.5 | a                    |
| mxbai-embed-large       |    1153 | 0.374935 |       0.5 | b                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| nomic-embed-text-v2-moe | 0.651097    | Sí                     |
| qwen3-embedding         | 0.324435    | Sí                     |
| mxbai-embed-large       | 6.03606e-13 | No                     |

#### 🔬 Factor: `Chunk_strategy`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.024251`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|---------:|----------:|:---------------------|
| N/A          |      96 | 0.628125 |       0.5 | a                    |
| semantic     |    1153 | 0.525325 |       0.5 | b                    |
| 1000         |    1152 | 0.517882 |       0.5 | b                    |
| 500          |    1152 | 0.512587 |       0.5 | b                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |    P-Value | Equivalente al Mejor   |
|:------------------------|-----------:|:-----------------------|
| semantic                | 0.0085229  | No                     |
| 1000                    | 0.00537718 | No                     |
| 500                     | 0.00159801 | No                     |

#### 🔬 Factor: `Db_motor`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.010301`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente   |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:-------------|--------:|---------:|----------:|:---------------------|
| N/A          |      96 | 0.628125 |       0.5 | a                    |
| faiss        |    1729 | 0.522961 |       0.5 | b                    |
| qdrant_local |    1728 | 0.514236 |       0.5 | b                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |    P-Value | Equivalente al Mejor   |
|:------------------------|-----------:|:-----------------------|
| faiss                   | 0.0064193  | No                     |
| qdrant_local            | 0.00225526 | No                     |

#### 🔬 Factor: `Generator`
- **Prueba Ómnibus (Kruskal-Wallis):** P-Value = `0.000000`
- **¿Diferencia Significativa?:** ✅ **SÍ**

**Ranking de Rendimiento con CLD:**
| Componente     |   Count |    Media |   Mediana | CLD (Agrupamiento)   |
|:---------------|--------:|---------:|----------:|:---------------------|
| gpt-oss:20b    |    1184 | 0.614611 |       0.5 | a                    |
| deepseek-r1:8b |    1183 | 0.508876 |       0.5 | b                    |
| qwen2.5:3b     |    1186 | 0.441315 |       0.5 | c                    |

**Análisis de Equivalencia (Mann-Whitney U):**
| Comparativa vs. Líder   |     P-Value | Equivalente al Mejor   |
|:------------------------|------------:|:-----------------------|
| deepseek-r1:8b          | 4.41261e-14 | No                     |
| qwen2.5:3b              | 3.88588e-34 | No                     |

### 🧩 2. Análisis de Combinación Completa (Factorial)
- **Kruskal-Wallis (Combinatorio):** P-Value = `0.000000`
- **Diferencias globales:** ✅ **SÍ**

**🚀 Top 5 Combinaciones Óptimas (según Media):**
| Combinación (Arquitectura | Embed | Chunk | DB | LLM)            |    Mean |   Median | Equivalencia   |
|:-----------------------------------------------------------------|--------:|---------:|:---------------|
| v2 | nomic-embed-text-v2-moe | 1000 | faiss | gpt-oss:20b        | 0.84375 |        1 | Líder          |
| v0 | N/A | N/A | N/A | gpt-oss:20b                               | 0.83125 |        1 | Sí             |
| v2 | nomic-embed-text-v2-moe | 1000 | qdrant_local | gpt-oss:20b | 0.8125  |        1 | Sí             |
| v2 | nomic-embed-text-v2-moe | semantic | faiss | gpt-oss:20b    | 0.75    |        1 | Sí             |
| v1 | qwen3-embedding | 1000 | faiss | gpt-oss:20b                | 0.73125 |        1 | Sí             |

**Otras combinaciones estadísticamente idénticas al líder:**
| Combinación                                                      |   p_value_vs_best |
|:-----------------------------------------------------------------|------------------:|
| v0 | N/A | N/A | N/A | gpt-oss:20b                               |         0.492815  |
| v2 | nomic-embed-text-v2-moe | 1000 | qdrant_local | gpt-oss:20b |         0.735966  |
| v2 | nomic-embed-text-v2-moe | semantic | faiss | gpt-oss:20b    |         0.406859  |
| v1 | qwen3-embedding | 1000 | faiss | gpt-oss:20b                |         0.217215  |
| v2 | qwen3-embedding | 1000 | qdrant_local | gpt-oss:20b         |         0.0991791 |

---

## 🔗 3. Análisis de Correlación Inter-Métrica
Este análisis identifica cómo se relacionan las métricas entre sí (ej. ¿a mayor latencia, mayor calidad?).

**Matriz de Correlación de Pearson (Tendencias Lineales):**

|                         |   latency_retrieval_seg |   latency_generation_seg |   total_latency_seg |   cost_est |   faithfulness_score |   relevance_score |   context_precision_score |   answer_relevancy_score |
|:------------------------|------------------------:|-------------------------:|--------------------:|-----------:|---------------------:|------------------:|--------------------------:|-------------------------:|
| latency_retrieval_seg   |                   1     |                    0.241 |               0.33  |      0.33  |                0.11  |             0.285 |                     0.222 |                    0.18  |
| latency_generation_seg  |                   0.241 |                    1     |               0.996 |      0.996 |                0.003 |             0.061 |                     0.044 |                    0.114 |
| total_latency_seg       |                   0.33  |                    0.996 |               1     |      1     |                0.013 |             0.087 |                     0.065 |                    0.128 |
| cost_est                |                   0.33  |                    0.996 |               1     |      1     |                0.013 |             0.087 |                     0.065 |                    0.128 |
| faithfulness_score      |                   0.11  |                    0.003 |               0.013 |      0.013 |                1     |             0.272 |                     0.255 |                    0.218 |
| relevance_score         |                   0.285 |                    0.061 |               0.087 |      0.087 |                0.272 |             1     |                     0.529 |                    0.296 |
| context_precision_score |                   0.222 |                    0.044 |               0.065 |      0.065 |                0.255 |             0.529 |                     1     |                    0.266 |
| answer_relevancy_score  |                   0.18  |                    0.114 |               0.128 |      0.128 |                0.218 |             0.296 |                     0.266 |                    1     |

---
