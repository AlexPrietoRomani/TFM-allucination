# Guía de Ejecución del Proyecto (TFM-allucination)

Este documento detalla todas las formas posibles de ejecutar el proyecto. El sistema soporta dos modos de ejecución configurables vía la variable `EXECUTION_MODE` en el archivo `.env`:

| Modo | Infraestructura | Embeddings | LLM | Qdrant |
|------|----------------|------------|-----|--------|
| **`local`** | Docker local (On-Premise) | Ollama (`mxbai-embed-large`, 1024d) | Ollama (`qwen2.5:3b`) | Contenedor local |
| **`cloud`** | APIs en la nube | Gemini (3072d) **o Ollama (1024d)** | Gemini / OpenRouter | Qdrant Cloud |

---

## 📌 Prerrequisitos Comunes

*   **Python 3.10+**
*   **Gestor de paquetes `uv`** ([Documentación oficial](https://docs.astral.sh/uv/))
*   **Docker Desktop** (para servicios en contenedor)
*   Archivo `.env` configurado (copia de `.env.example`)

---

## ⚙️ Variable Maestra: `EXECUTION_MODE`

El archivo `.env` contiene la variable principal que dicta todo el comportamiento:

```env
# 'local' → Qdrant local + Ollama (100% sin internet)
# 'cloud' → Qdrant Cloud + Google Gemini / OpenRouter
EXECUTION_MODE=local
```

Cambiar esta variable **no requiere modificar código**. Toda la arquitectura (embeddings, LLM, base vectorial) se adapta automáticamente.

---

## 🏠 Opción 1: Ejecución Local (On-Premise) — 100% Offline

Ideal para desarrollo, privacidad total, o cuando no se dispone de cuota de APIs en la nube.

### 1a. Solo con Docker (Stack completo)

Levanta Qdrant, Ollama, Redis, la App y el Worker en contenedores:

```bash
# Asegurar que EXECUTION_MODE=local en .env
docker compose -f docker-compose.yml -f docker-compose.local.yml up -d --build
```

Luego, descarga los modelos de Ollama dentro del contenedor:

```bash
docker exec -it tfm-ollama ollama pull qwen2.5:3b
docker exec -it tfm-ollama ollama pull mxbai-embed-large
```

Indexa los documentos:

```bash
docker exec -it tfm-app uv run scripts/setup_and_ingest.py --skip-ollama
```

Accede a la UI: [http://localhost:8501](http://localhost:8501)

### 1b. Desarrollo Local (UI Local + Servicios Docker)

Si modificas el código fuente y quieres hot-reload de Streamlit:

```bash
# 1. Instalar dependencias
uv sync

# 2. Levantar solo los servicios pesados en Docker
docker compose -f docker-compose.yml -f docker-compose.local.yml up -d qdrant redis ollama

# 3. Descargar modelos en Ollama del host
ollama pull qwen2.5:3b
ollama pull mxbai-embed-large

# 4. Indexar el corpus
uv run scripts/setup_and_ingest.py

# 5. Lanzar Streamlit en local
uv run streamlit run app.py
```

---

## ☁️ Opción 2: Ejecución en la Nube (Cloud)

Requiere cuentas activas en **Qdrant Cloud** y **Google AI Studio** (o **OpenRouter**).

### Configuración del `.env`

```env
EXECUTION_MODE=cloud

# Qdrant Cloud
QDRANT_CLOUD_URL=https://tu-cluster.cloud.qdrant.io:6333
QDRANT_CLOUD_API_KEY=tu_api_key_qdrant

# Google Gemini (Embeddings + LLM)
GOOGLE_API_KEY=tu_clave_gemini

# OpenRouter (alternativa LLM)
OPENROUTER_API_KEY=tu_clave_openrouter
DEFAULT_PROVIDER=gemini

# Embeddings (Para evitar los rate limits de la capa gratuita de Gemini)
DEFAULT_EMBEDDING_PROVIDER=ollama
```

> **💡 TIP HÍBRIDO PRO:** Puedes usar `EXECUTION_MODE=cloud` para guardar todo en Qdrant Cloud y usar LLMs potentes por API, pero configurar `DEFAULT_EMBEDDING_PROVIDER=ollama`. Así, los embeddings se calculan localmente y **evitas por completo los rate limits** gratuitos de la API de Gemini al indexar.

> **⚠️ Las siguientes tres opciones (2a, 2b, 2c) son ALTERNATIVAS. Usa UNA u otra, no ambas al mismo tiempo.** Si la App en Docker y la App local corren en el mismo puerto (8501), entrarán en conflicto.

### 2a. Lanzar con Docker (solo App + Redis)

En modo cloud, **no es necesario levantar Qdrant ni Ollama** — esos servicios residen en la nube:

```bash
# 1. Levantar los contenedores (app + redis + worker)
docker compose up -d --build

# 2. Indexar el corpus (dentro del contenedor)
docker exec -it tfm-app uv run scripts/setup_and_ingest.py --skip-ollama

# 3. Abrir http://localhost:8501
```

### 2b. Lanzar localmente (sin Docker para la App)

Ideal para desarrollo con hot-reload:

```bash
# 1. Instalar dependencias
uv sync

# 2. Indexar el corpus (hacia Qdrant Cloud)
uv run scripts/setup_and_ingest.py --skip-ollama

# 3. Lanzar Streamlit
uv run streamlit run app.py
```

### 2c. Lanzar Híbrido (App Local + Qdrant Cloud + Ollama Embeddings)

Si configuraste `DEFAULT_EMBEDDING_PROVIDER=ollama` en `.env`, necesitas tener el contenedor de Ollama encendido:

```bash
# 1. Levantar solo Ollama localmente y Redis
docker compose -f docker-compose.yml -f docker-compose.local.yml up -d ollama redis

# 2. Indexar el corpus (Ollama genera los vectores -> Se guardan en Qdrant Cloud)
uv run scripts/setup_and_ingest.py

# 3. Lanzar Streamlit
uv run streamlit run app.py
```

> **⚠️ Importante sobre Rate Limits:** Si usas Gemini para embeddings (`DEFAULT_EMBEDDING_PROVIDER=gemini`), su API gratuita tiene un límite de peticiones por minuto (100 RPM) y por día (1500 RPD). El sistema implementa reintentos automáticos con *Exponential Backoff*, pero si el corpus es grande, es **muy recomendable** usar la opción 2c (Embeddings con Ollama).

---

## 📊 Opción 3: Scripts de Evaluación (Sin UI)

Asegúrate de tener los servicios (`qdrant`, `redis`) corriendo y los modelos disponibles según tu `EXECUTION_MODE`.

```bash
# Evaluación V0 vs V1
uv run eval/run_eval.py

# Evaluación V2 (Agente)
uv run eval/run_eval_v2.py

# Métricas de alucinación
uv run eval/run_metrics.py
uv run eval/run_factscore.py

# Reporte comparativo
uv run reports/generate_report.py --mode all
```

---

## 🔬 Opción 4: Matriz de Experimentos (FAISS vs Qdrant)

Para pruebas masivas iterando múltiples modelos de Embeddings, estrategias de chunking y bases de datos:

### 1. Construir la Matriz Vectorial
Este script leerá el corpus y generará bases de datos para todas las combinaciones posibles en `data/vector_matrix/faiss`.

```bash
uv run scripts/build_vector_matrix.py
```

### 2. Ejecutar la Evaluación Matricial
Calcula métricas de Fidelidad, Relevancia y Precisión para las permutaciones del banco de preguntas. Soporta filtros específicos y un modo **Skip (Continuar)** por defecto para ahorrar procesamiento.

```bash
# Ejecución estándar (procesará preguntas pendientes de los 6 generadores por defecto)
uv run eval/run_matrix_eval.py

# --limit N para correr solo N preguntas fijas (Prueba rápida)
uv run eval/run_matrix_eval.py --limit 1

# Filtrar permutación específica para inspección ágil
uv run eval/run_matrix_eval.py --embedding mxbai-embed-large --chunk-strategy 500 --db-motor faiss --generator deepseek-r1:8b

# Usar el flag --overwrite si deseas recalcular y forzar el reemplazo de filas en el JSONL
uv run eval/run_matrix_eval.py --overwrite
```

### 3. Visualizar en la UI (Matriz de Experimentos)
Los resultados se consolidan incrementalmente en `eval/results/Matrix/eval_results_matrix.jsonl`. Puedes interactuar con la pestaña **Matriz de Experimentos** en la UI (**http://localhost:8501**), donde podrás:
* **Lanzar pruebas en Background** e inspeccionar logs en tiempo real.
* **Filtrar gráficos de BoxPlots** por cualquier eje (`embedding`, `generator`, etc.).
* **Agrupar la Tabla de Resultados** para extraer promedios de metricas sobre arquitecturas.

---

## 🔧 Resumen de Comandos

| Escenario | Comando |
|-----------|---------|
| **Local completo (Docker)** | `docker compose -f docker-compose.yml -f docker-compose.local.yml up -d --build` |
| **Cloud completo (Docker)** | `docker compose up -d --build` |
| **Solo servicios locales** | `docker compose -f docker-compose.yml -f docker-compose.local.yml up -d qdrant redis ollama` |
| **UI local (desarrollo)** | `uv run streamlit run app.py` |
| **Indexar corpus** | `uv run scripts/setup_and_ingest.py` |
| **Sincronizar dependencias** | `uv sync` |

---

## 📝 Notas sobre Colecciones Qdrant

Para evitar colisiones de dimensionalidad de embeddings entre distintos proveedores, el sistema crea colecciones separadas según el modelo utilizado:

| Proveedor de Embedding | Colección Qdrant | Dimensión típica |
|-----------------------|-----------------|-------------------|
| `ollama` | `tfm_allucination_ollama` | 1024d (mxbai-embed-large) |
| `gemini` | `tfm_allucination_gemini` | 3072d (gemini-embedding-001) |

Si cambias de proveedor de embeddings en `.env`, debes re-indexar el corpus para la nueva colección:

```bash
uv run scripts/setup_and_ingest.py --force-reindex
```
