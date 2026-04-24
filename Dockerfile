# ────────────────────────────────────────────────────────────────────────────
# TFM-Allucination  ·  Multi-stage Dockerfile
# ────────────────────────────────────────────────────────────────────────────
FROM python:3.11-slim AS base

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalar uv (gestor de paquetes ultra-rápido)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# ── Etapa de dependencias (cacheable) ────────────────────────────────────
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# ── Etapa de aplicación ─────────────────────────────────────────────────
COPY src/ src/
COPY app.py .
COPY corpus/registry.yaml corpus/registry.yaml
COPY eval/ eval/
COPY reports/ reports/
COPY services/ services/
COPY scripts/ scripts/

# Crear directorio para corpus/raw (será montado o llenado)
RUN mkdir -p corpus/raw

# Puerto de Streamlit
EXPOSE 8501

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Comando por defecto: Streamlit
CMD ["uv", "run", "streamlit", "run", "app.py", \
    "--server.address=0.0.0.0", \
    "--server.port=8501", \
    "--server.headless=true"]
