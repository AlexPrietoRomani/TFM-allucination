# Análisis Estadístico de Sistemas RAG: Metodología

Este documento describe el rigor estadístico aplicado en la evaluación de la matriz del RAG, detallando el flujo de trabajo para comparar las distintas tecnologías (Arquitecturas, DBs Vectoriales, Embeddings, Chunking y Generadores) de manera justa.

Debido a que las métricas de los sistemas de recuperación y generación de lenguaje (como Ragas) **no suelen seguir distribuciones normales** y frecuentemente presentan asimetrías o límites duros (como en `0.0` y `1.0`), la utilización de pruebas estadísticas paramétricas como el ANOVA de un factor o el post-hoc de Tukey HSD es matemáticamente incorrecta.

Para subsanar esto, el script `statistical_analysis.py` implementa el siguiente _pipeline_ estadístico completamente **no paramétrico**:

---

## 1. Prueba Ómnibus: Kruskal-Wallis

**Propósito:** Determinar de forma global si hay diferencias significativas entre 3 o más grupos independientes.

**Proceso:**
* La prueba (implementada con `scipy.stats.kruskal`) clasifica todas las puntuaciones en rangos y comprueba si la distribución de rangos de algún grupo (por ejemplo, `faiss` vs `qdrant_local`) difiere significativamente de la distribución conjunta.
* **Hipótesis nula ($H_0$):** Todos los grupos de componentes provienen de la misma distribución (tienen medianas de desempeño similares).
* Si el **Valor-p (P-value) < 0.05**, rechazamos la hipótesis nula, lo que significa que **SÍ hay diferencia estadística validada** y podemos afirmar que al menos un componente/combinación es realmente superior o inferior al resto.

## 2. Pruebas Post-Hoc: Encontrando el "Líder"

Una vez que Kruskal-Wallis confirma que hay diferencias, necesitamos saber _específicamente entre cuáles_.

### A. Prueba de Dunn con Compact Letter Display (CLD)
Dado que Kruskal-Wallis clasifica las puntuaciones en rangos, el examen apropiado es la prueba post-hoc de Dunn (*Dunn, 1964*). Históricamente utilizada como el equivalente de Tukey para análisis no paramétricos. 

**Proceso:**
* Utilizando las tablas de Dunn (a través del paquete `scikit-posthocs`), la función genera una matriz cruzada comprobando la diferencia de rango medio contra _todos_.
* **Corrección de falsos descubrimientos:** Para evitar errores falsos-positivos al hacer muchas comparaciones iterativas, aplicamos la corrección FDR (False Discovery Rate) de **Benjamini-Hochberg (bh)** al cálculo del p-value.
* **Letters (CLD):** Un sistema recursivo asigna **Letras (a, b, c...)** a cada grupo:
    - Componentes que comparten la misma letra (ej. ambos tienen la 'a' o 'ab') **no son estadísticamente diferentes entre sí**.
    - Componentes puramente aislados (uno 'a', el otro 'b') afirman firmemente que el primero es objetivamente superior al segundo.
* **Referencia literaria:** 
  > Pohlert, T. (2016). *The Pairwise Multiple Comparison of Mean Ranks Package (PMCMR)*. R project.

### B. Mann-Whitney U (Comparación Uno a Uno vs. El Líder)
Con el fin de facilitar la lectura rápida del mejor componente posible para producción, se complementa con la clásica prueba _U de Mann-Whitney_.

**Proceso:**
* El script identifica inmediatamente el componente que obtuvo la **Media Absoluta Superior** llamándolo el `Líder`.
* Toma la muestra de datos crudos del líder y ejecuta simulaciones `mannwhitneyu(Leader, Otro)` para revisar contra el resto de contendientes.
* Si un "Otro modelo" obtuvo en apariencia peores datos pero el **p-value de Mann-Whitney ≥ 0.05**, se marca con un **"SÍ"** en `Stat_Equivalent_to_Best`. Significa que aunque su media técnica haya sido menor, en la práctica esa diferencia podría deberse a ruido del muestreo y por ende, es _Estadísticamente Equivalente al Líder_ y puede ser desplegado a producción si los costos son más bajos.

---

## ⚙️ Estructura del Resultado (`statistical_results.md`)
Cada vez que se ejecuta la prueba `uv run python eval/statistical_analysis.py`, el bloque genera lo siguiente de métrica por métrica:

1. El resultado global `P-value` (Kruskal-Wallis).
2. Un ranking por media real (`Count, Mean, Median`).
3. La columna **CLD (Dunn)** (`a`, `ab`, `c`...). Puedes encontrar aquí que si tienes herramientas tecnológicas similares, tendrán la misma letra.
4. La tabla de las combinaciones enteras que pelean por destronar o empatar al Pipeline "Líder" gracias al Mann-Whitney U.
