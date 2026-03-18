#!/usr/bin/env python3
"""
setup_and_ingest.py — Script de configuración inicial del proyecto TFM.

Este script automatiza TODO el proceso de primera ejecución:
  1. Verifica que los servicios Docker (Qdrant, Ollama) estén activos.
  2. Descarga el modelo LLM en Ollama si no existe.
  3. Descarga el modelo de Embeddings en Ollama si no existe.
  4. Verifica que existan documentos en corpus/raw/.
  5. Indexa los documentos en Qdrant usando el registry.yaml.

Uso:
  uv run scripts/setup_and_ingest.py
  uv run scripts/setup_and_ingest.py --skip-ollama     # Si usas Gemini/OpenRouter
  uv run scripts/setup_and_ingest.py --model qwen2.5:7b # Modelo Ollama diferente
"""

import argparse
import os
import sys
import time
import requests
from pathlib import Path

# Asegurar que el directorio raíz del proyecto esté en sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
os.chdir(PROJECT_ROOT)

from src.core.config.settings import settings

# Colores para terminal
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def status(msg, ok=True):
    icon = f"{GREEN}✓{RESET}" if ok else f"{RED}✗{RESET}"
    print(f"  {icon} {msg}")

def header(msg):
    print(f"\n{CYAN}{BOLD}{'═' * 60}{RESET}")
    print(f"{CYAN}{BOLD}  {msg}{RESET}")
    print(f"{CYAN}{BOLD}{'═' * 60}{RESET}")


def check_qdrant() -> bool:
    """Verifica que Qdrant esté activo mediante el cliente oficial."""
    try:
        from src.knowledge.indexer import get_qdrant_client
        client = get_qdrant_client()
        client.get_collections()
        return True
    except Exception:
        return False


def check_ollama(url: str) -> bool:
    """Verifica que Ollama esté activo."""
    try:
        r = requests.get(url, timeout=5)
        return r.status_code == 200
    except Exception:
        return False


def ollama_has_model(url: str, model_name: str) -> bool:
    """Verifica si un modelo ya está descargado en Ollama."""
    try:
        r = requests.get(f"{url}/api/tags", timeout=10)
        if r.status_code == 200:
            models = r.json().get("models", [])
            # Busca coincidencia parcial (ej: 'qwen2.5:3b' en 'qwen2.5:3b-instruct')
            for m in models:
                if m.get("name", "").startswith(model_name.split(":")[0]):
                    return True
        return False
    except Exception:
        return False


def ollama_pull_model(url: str, model_name: str) -> bool:
    """Descarga un modelo en Ollama (puede tardar varios minutos)."""
    print(f"\n  {YELLOW}⬇ Descargando modelo '{model_name}' en Ollama...{RESET}")
    print(f"  {YELLOW}  (Esto puede tardar varios minutos según tu conexión){RESET}")
    try:
        r = requests.post(
            f"{url}/api/pull",
            json={"name": model_name, "stream": False},
            timeout=1200  # 20 minutos máximo para embeddings grandes/modelos
        )
        if r.status_code == 200:
            return True
        else:
            print(f"  {RED}  Error descarga: {r.text}{RESET}")
            return False
    except requests.exceptions.Timeout:
        print(f"  {RED}  Timeout: El modelo es muy grande o la conexión es lenta.{RESET}")
        print(f"  {YELLOW}  Intenta manualmente: ollama pull {model_name}{RESET}")
        return False
    except Exception as e:
        print(f"  {RED}  Error: {e}{RESET}")
        return False


def count_corpus_files() -> tuple:
    """Cuenta archivos en corpus/raw/."""
    raw_dir = Path("corpus/raw")
    if not raw_dir.exists():
        return 0, []
    files = list(raw_dir.glob("*.*"))
    pdfs = [f for f in files if f.suffix.lower() == ".pdf"]
    return len(files), pdfs


def run_indexer():
    """Ejecuta el indexador de documentos."""
    print(f"\n  {YELLOW}📚 Indexando documentos en Qdrant...{RESET}")
    try:
        from src.knowledge.indexer import index_documents
        index_documents()
        return True
    except Exception as e:
        print(f"  {RED}  Error durante indexación: {e}{RESET}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Setup inicial del TFM")
    parser.add_argument("--qdrant-url", default=settings.active_qdrant_url,
                        help="URL de Qdrant")
    parser.add_argument("--ollama-url", default=settings.ollama_base_url,
                        help="URL de Ollama")
    parser.add_argument("--model", default=settings.default_ollama_model,
                        help="Modelo LLM Ollama a descargar")
    parser.add_argument("--skip-ollama", action="store_true",
                        help="Omitir verificación/descarga de Ollama")
    parser.add_argument("--skip-index", action="store_true",
                        help="Omitir indexación en Qdrant")
    
    args = parser.parse_args()

    print(f"\n{BOLD}🫐 TFM-Allucination — Setup Inicial v2{RESET}")
    print(f"{'─' * 50}")

    # ─── PASO 1: Verificar servicios ─────────────────────────────────────────
    header(f"PASO 1: Verificando servicios (Modo: {settings.execution_mode.upper()})")

    # Qdrant
    if check_qdrant():
        status(f"Qdrant activo en {settings.active_qdrant_url}")
    else:
        status(f"Qdrant NO responde en {settings.active_qdrant_url}", ok=False)
        if settings.execution_mode == "local":
            print(f"\n  {YELLOW}Ejecuta: docker compose -f docker-compose.yml -f docker-compose.local.yml up -d qdrant{RESET}")
        else:
            print(f"\n  {YELLOW}Revisa tus credenciales de Qdrant Cloud en .env (URL y API_KEY){RESET}")
        print(f"  {YELLOW}Esperando 10s y reintentando...{RESET}")
        time.sleep(10)
        if not check_qdrant():
            print(f"\n  {RED}ERROR: Qdrant no está disponible.{RESET}")
            sys.exit(1)
        status(f"Qdrant ahora activo en {settings.active_qdrant_url}")

    # Ollama
    if not args.skip_ollama:
        if check_ollama(args.ollama_url):
            status(f"Ollama activo en {args.ollama_url}")

            # 1. Verificar LLM
            if ollama_has_model(args.ollama_url, args.model):
                status(f"LLM '{args.model}' ya disponible")
            else:
                status(f"LLM '{args.model}' no encontrado, descargando...", ok=False)
                ollama_pull_model(args.ollama_url, args.model)
            
            # 2. Verificar Embeddings
            emb_model = settings.default_embedding_model_local
            if settings.default_embedding_provider == "ollama":
                if ollama_has_model(args.ollama_url, emb_model):
                     status(f"Embeddings '{emb_model}' ya disponible")
                else:
                     status(f"Embeddings '{emb_model}' no encontrado, descargando...", ok=False)
                     ollama_pull_model(args.ollama_url, emb_model)

        else:
            status(f"Ollama NO responde en {args.ollama_url}", ok=False)
            print(f"  {YELLOW}Si usas Gemini/OpenRouter, usa --skip-ollama{RESET}")
    else:
        print(f"  ⏭ Ollama omitido (--skip-ollama)")

    # ─── PASO 2: Verificar corpus ────────────────────────────────────────────
    header("PASO 2: Verificando corpus de documentos")

    total_files, pdfs = count_corpus_files()

    if total_files == 0:
        status("No hay documentos en corpus/raw/", ok=False)
        if not args.skip_index:
             print(f"  {YELLOW}Abortando indexación.{RESET}")
             sys.exit(0)
    else:
        status(f"Encontrados {total_files} archivos ({len(pdfs)} PDFs)")

    # ─── PASO 3: Indexar en Qdrant ───────────────────────────────────────────
    if not args.skip_index:
        header("PASO 3: Indexando documentos en Qdrant")
        run_indexer()
    else:
        print(f"\n  ⏭ Indexación omitida (--skip-index)")

    # ─── RESUMEN ─────────────────────────────────────────────────────────────
    header("SETUP COMPLETO")
    print(f"  Listo para usar.")


if __name__ == "__main__":
    main()
