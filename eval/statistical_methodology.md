# Análisis Estadístico de Sistemas RAG: Metodología

Este documento describe el rigor estadístico aplicado en la evaluación de la matriz del RAG, detallando el flujo de trabajo para comparar las distintas tecnologías (Arquitecturas, DBs Vectoriales, Embeddings, Chunking y Generadores) de manera justa.

El pipeline estadístico implementado en `run_matrix_eval.py` diferencia dos familias de variables:

- **Variables no paramétricas** (métricas RAGAS acotadas en [0, 1]): `faithfulness_score`, `relevance_score`, `context_precision_score`, `answer_relevancy_score`. Estas métricas no siguen distribuciones normales y frecuentemente presentan asimetrías o límites duros en `0.0` y `1.0`, por lo que se aplica un pipeline **no paramétrico** (Kruskal-Wallis → Dunn → Mann-Whitney U).

- **Variables paramétricas** (continuas, sin límites fijos): `latency_retrieval_seg`, `latency_generation_seg`, `total_latency_seg`, `cost_est`. Son variables de tiempo y costo cuyos valores son continuos y sin techo artificial, por lo que se aplica un pipeline **paramétrico** (ANOVA de un factor → T-Test con corrección FDR → T-Test pareado).

---

## 1. Pipeline No Paramétrico (Métricas RAGAS)

### 1.1. Prueba Ómnibus: Kruskal-Wallis

**Propósito:** Determinar de forma global si hay diferencias significativas entre 3 o más grupos independientes.

**Proceso:**
* La prueba (implementada con `scipy.stats.kruskal`) clasifica todas las puntuaciones en rangos y comprueba si la distribución de rangos de algún grupo (por ejemplo, `faiss` vs `qdrant_local`) difiere significativamente de la distribución conjunta.
* **Hipótesis nula ($H_0$):** Todos los grupos de componentes provienen de la misma distribución (tienen medianas de desempeño similares).
* Si el **Valor-p (P-value) < 0.05**, rechazamos la hipótesis nula, lo que significa que **SÍ hay diferencia estadística validada** y podemos afirmar que al menos un componente/combinación es realmente superior o inferior al resto.

### 1.2. Pruebas Post-Hoc No Paramétricas

#### A. Prueba de Dunn con Compact Letter Display (CLD)
Dado que Kruskal-Wallis clasifica las puntuaciones en rangos, el examen apropiado es la prueba post-hoc de Dunn (*Dunn, 1964*). Históricamente utilizada como el equivalente de Tukey para análisis no paramétricos. 

**Proceso:**
* Utilizando las tablas de Dunn (a través del paquete `scikit-posthocs`), la función genera una matriz cruzada comprobando la diferencia de rango medio contra _todos_.
* **Corrección de falsos descubrimientos:** Para evitar errores falsos-positivos al hacer muchas comparaciones iterativas, aplicamos la corrección FDR (False Discovery Rate) de **Benjamini-Hochberg (bh)** al cálculo del p-value.
* **Letters (CLD):** Un sistema recursivo asigna **Letras (a, b, c...)** a cada grupo:
    - Componentes que comparten la misma letra (ej. ambos tienen la 'a' o 'ab') **no son estadísticamente diferentes entre sí**.
    - Componentes puramente aislados (uno 'a', el otro 'b') afirman firmemente que el primero es objetivamente superior al segundo.
* **Referencia literaria:** 
  > Pohlert, T. (2016). *The Pairwise Multiple Comparison of Mean Ranks Package (PMCMR)*. R project.

#### B. Mann-Whitney U (Comparación Uno a Uno vs. El Líder)
Con el fin de facilitar la lectura rápida del mejor componente posible para producción, se complementa con la clásica prueba _U de Mann-Whitney_.

**Proceso:**
* El script identifica inmediatamente el componente que obtuvo la **Media Absoluta Superior** llamándolo el `Líder`.
* Toma la muestra de datos crudos del líder y ejecuta simulaciones `mannwhitneyu(Leader, Otro)` para revisar contra el resto de contendientes.
* Si un "Otro modelo" obtuvo en apariencia peores datos pero el **p-value de Mann-Whitney ≥ 0.05**, se marca con un **"SÍ"** en `Stat_Equivalent_to_Best`. Significa que aunque su media técnica haya sido menor, en la práctica esa diferencia podría deberse a ruido del muestreo y por ende, es _Estadísticamente Equivalente al Líder_ y puede ser desplegado a producción si los costos son más bajos.

---

## 2. Pipeline Paramétrico (Latencia y Costo)

### 2.1. Prueba Ómnibus: Análisis de Varianza de una vía (ANOVA)

**Propósito:** Determinar si existen diferencias significativas en las medias de latencia o costo entre 3 o más grupos de componentes RAG.

**Justificación:** A diferencia de las métricas RAGAS ([0, 1]), las variables de latencia (`latency_retrieval_seg`, `latency_generation_seg`, `total_latency_seg`) y costo estimado (`cost_est`) son **variables continuas** sin límites artificiales. Aunque pueden presentar cierta asimetría, el ANOVA de un factor es robusto frente a desviaciones moderadas de la normalidad cuando los tamaños muestrales son iguales o grandes (n ≥ 30 por grupo). En nuestro caso, cada combinación contiene 32 muestras, lo que garantiza la validez del supuesto por el **Teorema del Límite Central** (Fisher, 1925).

**Proceso:**
* La prueba (implementada con `scipy.stats.f_oneway`) calcula el estadístico F, que compara la variabilidad *entre* grupos con la variabilidad *dentro* de los grupos.
* **Hipótesis nula ($H_0$):** Todas las medias poblacionales de los grupos son iguales ($\mu_1 = \mu_2 = ... = \mu_k$).
* Si el **Valor-p (P-value) < 0.05**, rechazamos $H_0$, confirmando que al menos un componente exhibe una latencia o costo significativamente distinto al resto.

### 2.2. Pruebas Post-Hoc Paramétricas

#### A. T-Test pareado con corrección FDR (Benjamini-Hochberg) y CLD

**¿Por qué T-Test con FDR en lugar de Tukey HSD?**

La prueba de Tukey HSD (Honestly Significant Difference) es la elección clásica tras un ANOVA significativo. Sin embargo, su implementación en `scikit-posthocs` (`sp.posthoc_tukey`) requiere la construcción de una matriz de distribución estudentizada del rango (*Studentized Range Distribution*), cuya complejidad computacional escala cuadráticamente con el número de grupos. En nuestro diseño factorial completo, las combinaciones de la matriz (Arquitectura × Embedding × Chunking × DB × Generador) generan **decenas de grupos únicos**, lo que produce una sobrecarga computacional inviable para Tukey.

La alternativa adoptada es el **T-Test de Student para muestras independientes** (`sp.posthoc_ttest`) con corrección de **Benjamini-Hochberg (FDR)** para comparaciones múltiples. Este enfoque:

1. **Rendimiento computacional:** Ejecuta comparaciones en tiempo lineal respecto al número de pares, permitiendo procesar cientos de combinaciones en segundos.
2. **Control de error estadístico:** La corrección FDR de Benjamini-Hochberg (1995) controla la proporción esperada de falsos positivos entre todos los descubrimientos significativos, lo cual es más potente (menos conservador) que las correcciones clásicas tipo Bonferroni, manteniendo una tasa de error aceptable.
3. **Equivalencia formal:** Bajo supuestos de normalidad (validados por el Teorema del Límite Central) y homocedasticidad, el T-Test pareado con corrección FDR produce inferencias estadísticas equivalentes a Tukey HSD con mayor escalabilidad.

**Proceso:**
* Se ejecuta `sp.posthoc_ttest()` con `p_adjust='fdr_bh'` para obtener la matriz de p-values ajustados.
* Se aplica el mismo algoritmo de **Compact Letter Display (CLD)** descrito para el pipeline no paramétrico, asignando letras de agrupamiento homogéneo.
* **Interpretación invertida:** Para latencia y costo, el **"mejor"** es el grupo con la **media más baja** (menor latencia = mayor eficiencia). El ranking se ordena de forma ascendente.

#### B. T-Test de Student (Comparación Uno a Uno vs. El Líder)
Análogo al Mann-Whitney U del pipeline no paramétrico, se utiliza el **T-Test para muestras independientes** (`scipy.stats.ttest_ind`) para comparar cada grupo contra el líder (el de menor latencia/costo medio).

* Si el **p-value ≥ 0.05**, el grupo es marcado como **"SÍ"** en `Stat_Equivalent_to_Best`, indicando que su diferencia de rendimiento en términos de tiempo/costo no es estadísticamente significativa.

---

## ⚙️ Estructura del Resultado (`statistical_results.md`)
Cada vez que se ejecuta el análisis estadístico `uv run python eval/statistical_analysis.py`, el bloque genera lo siguiente de métrica por métrica:

1. El resultado global `P-value` (Kruskal-Wallis para RAGAS, ANOVA para latencia/costo).
2. Un ranking por media real (`Count, Mean, Median`).
3. La columna **CLD** (`a`, `ab`, `c`...). Puedes encontrar aquí que si tienes herramientas tecnológicas similares, tendrán la misma letra.
4. La tabla de las combinaciones enteras que pelean por destronar o empatar al Pipeline "Líder" gracias al Mann-Whitney U (RAGAS) o T-Test (latencia/costo).

---

## 📚 Bibliografía

### Métricas No Paramétricas (RAGAS)

1. **Kruskal-Wallis (1952)**: Kruskal, W. H., & Wallis, W. A. (1952). *Use of ranks in one-criterion variance analysis*. Journal of the American Statistical Association, 47(260), 583–621. [DOI: 10.1080/01621459.1952.10483441](https://doi.org/10.1080/01621459.1952.10483441)
2. **Dunn (1964)**: Dunn, O. J. (1964). *Multiple comparisons using rank sums*. Technometrics, 6(3), 241–252. [DOI: 10.1080/00401706.1964.10490181](https://doi.org/10.1080/00401706.1964.10490181)
3. **Mann-Whitney U (1947)**: Mann, H. B., & Whitney, D. R. (1947). *On a test of whether one of two random variables is stochastically larger than the other*. The Annals of Mathematical Statistics, 18(1), 50–60. [DOI: 10.1214/aoms/1177730491](https://doi.org/10.1214/aoms/1177730491)
4. **Pohlert (2014)**: Pohlert, T. (2014). *The Pairwise Multiple Comparison of Mean Ranks Package (PMCMR)*. R package documentation. [Documentación en CRAN](https://CRAN.R-project.org/package=PMCMR). (Base metodológica para el cálculo de comparaciones múltiples y niveles de significancia).
5. **Eshel (2010)**: Eshel, G. (2010). *Rank-Based Nonparametric Statistical Tests*. Bard College. [Material de Curso/Notas Técnicas]. (Referencia para la lógica de ranking y el algoritmo de Compact Letter Display (CLD) en contextos no paramétricos).

### Métricas Paramétricas (Latencia y Costo)

1. **Fisher (1925)**: Fisher, R. A. (1925). *Statistical Methods for Research Workers*. Edinburgh: Oliver & Boyd. [DOI: 10.1038/116815a0](https://doi.org/10.1038/116815a0). (Obra fundacional del ANOVA de un factor y el estadístico F).
2. **Student [Gosset] (1908)**: Student [W. S. Gosset]. (1908). *The Probable Error of a Mean*. Biometrika, 6(1), 1–25. [DOI: 10.1093/biomet/6.1.1](https://doi.org/10.1093/biomet/6.1.1). (Origen del T-Test para comparación de medias).
3. **Benjamini-Hochberg (1995)**: Benjamini, Y., & Hochberg, Y. (1995). *Controlling the false discovery rate: A practical and powerful approach to multiple testing*. Journal of the Royal Statistical Society: Series B (Methodological), 57(1), 289–300. [DOI: 10.1111/j.2517-6161.1995.tb02031.x](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x). (Fundamental para la corrección FDR en comparaciones múltiples de ambas familias).
