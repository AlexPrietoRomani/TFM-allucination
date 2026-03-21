"""
parsers.py — Pipeline de Parseo Estructurado para PDFs Tabulares

Convierte PDFs complejos (manuales FRAC/IRAC, guías fitosanitarias)
en Markdown estructurado con tablas preservadas y opcionalmente
aplana filas tabulares a oraciones descriptivas para mejorar la
precisión de los embeddings.

Dependencias:
    pip install docling  (o uv add docling)
"""

import re
import logging
from pathlib import Path
from typing import List, Optional, Dict, Any

logger = logging.getLogger(__name__)


# ═══════════════════════════════════════════════════════════════════════════════
# 1. DoclingParser — PDF → Markdown estructurado
# ═══════════════════════════════════════════════════════════════════════════════

class DoclingParser:
    """Convierte un PDF a Markdown usando Docling (IBM).

    Docling reconstruye tablas, headers y layout del PDF respetando
    las Bounding Boxes, produciendo Markdown con tablas intactas.
    """

    def __init__(self):
        # Lazy import para no penalizar el arranque de la app
        try:
            from docling.document_converter import DocumentConverter
            self._converter = DocumentConverter()
        except ImportError:
            raise ImportError(
                "docling no está instalado. Ejecuta: uv add docling"
            )

    def parse(self, pdf_path: Path) -> str:
        """Convierte un PDF a Markdown estructurado.

        Args:
            pdf_path: Ruta al archivo PDF.

        Returns:
            String con el contenido en formato Markdown.
        """
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF no encontrado: {pdf_path}")

        logger.info(f"Parseando con Docling: {pdf_path.name}")
        result = self._converter.convert(str(pdf_path))
        md_content = result.document.export_to_markdown()
        logger.info(
            f"  → {len(md_content)} caracteres extraídos de {pdf_path.name}"
        )
        return md_content


# ═══════════════════════════════════════════════════════════════════════════════
# 2. TableFlattener — Tablas Markdown → Oraciones descriptivas
# ═══════════════════════════════════════════════════════════════════════════════

class TableFlattener:
    """Transforma tablas Markdown en oraciones descriptivas en lenguaje natural.

    Esto eleva dramáticamente la calidad de los embeddings para documentos
    tabulares como FRAC/IRAC donde cada fila contiene relaciones semánticas
    críticas (ingrediente activo → grupo → código → comentarios).
    """

    # Regex para detectar un bloque de tabla Markdown
    _TABLE_PATTERN = re.compile(
        r"((?:^\|.+\|$\n?)+)",
        re.MULTILINE
    )

    @staticmethod
    def _parse_table_block(table_text: str) -> tuple:
        """Extrae headers y filas de un bloque de tabla Markdown.

        Returns:
            (headers: List[str], rows: List[List[str]])
        """
        lines = [
            line.strip()
            for line in table_text.strip().split("\n")
            if line.strip()
        ]

        if len(lines) < 2:
            return [], []

        # Headers: primera línea
        headers = [
            cell.strip()
            for cell in lines[0].split("|")
            if cell.strip()
        ]

        # Filas: saltar header y separador (línea de guiones)
        rows = []
        for line in lines[2:]:  # Skip header + separator
            # Validar que la línea no sea un separador
            if re.match(r"^\|[\s\-:]+\|$", line):
                continue
            cells = [
                cell.strip()
                for cell in line.split("|")
                if cell.strip()
            ]
            if cells:
                rows.append(cells)

        return headers, rows

    @classmethod
    def flatten(
        cls,
        md_text: str,
        doc_meta: Optional[Dict[str, Any]] = None
    ) -> str:
        """Aplana tablas en el Markdown sustituyéndolas por oraciones descriptivas.

        Args:
            md_text: Contenido Markdown con tablas.
            doc_meta: Metadatos del documento (title, year, tags, etc.)
                      para enriquecer las oraciones.

        Returns:
            Markdown con las tablas reemplazadas por oraciones.
        """
        doc_meta = doc_meta or {}
        doc_title = doc_meta.get("title", "Documento")
        doc_year = doc_meta.get("year", "")

        def _replace_table(match):
            table_text = match.group(0)
            headers, rows = cls._parse_table_block(table_text)

            if not headers or not rows:
                return table_text  # Devolver sin cambios si no se pudo parsear

            sentences = []
            for row in rows:
                # Emparejar cada celda con su header
                pairs = []
                for i, cell in enumerate(row):
                    if i < len(headers) and cell and cell != "-":
                        pairs.append(f"{headers[i]}: {cell}")

                if pairs:
                    prefix = f"Según {doc_title}"
                    if doc_year:
                        prefix += f" ({doc_year})"
                    sentence = f"{prefix}, {', '.join(pairs)}."
                    sentences.append(sentence)

            return "\n".join(sentences) if sentences else table_text

        return cls._TABLE_PATTERN.sub(_replace_table, md_text)


# ═══════════════════════════════════════════════════════════════════════════════
# 3. ImageFilter — Filtrado de imágenes vía VLM local (Ollama)
# ═══════════════════════════════════════════════════════════════════════════════

class ImageFilter:
    """Filtra imágenes decorativas (logos, portadas) y describe las útiles.

    Usa un modelo VLM ligero en Ollama (ej: llava:7b, qwen2-vl) para
    determinar si una imagen contiene información semántica relevante.
    """

    SYSTEM_PROMPT = (
        "Analiza esta imagen en el contexto de un documento técnico agrícola. "
        "Si es solo un logo institucional, gráfico decorativo, portada o "
        "elemento sin información técnica, responde ÚNICAMENTE: DESCARTAR. "
        "Si es un diagrama de flujo, esquema químico, tabla visual, mapa, "
        "ciclo de vida de plaga o gráfico con datos, descríbelo "
        "detalladamente en español para que un sistema de búsqueda pueda "
        "encontrar esta información."
    )

    def __init__(
        self,
        model: str = "llama3.2-vision",
        ollama_base_url: str = "http://localhost:11434"
    ):
        self.model = model
        self.base_url = ollama_base_url

    def analyze(self, image_path: Path) -> Optional[str]:
        """Analiza una imagen y retorna su descripción o None si es decorativa.

        Args:
            image_path: Ruta a la imagen extraída del PDF.

        Returns:
            Descripción textual de la imagen, o None si debe descartarse.
        """
        try:
            import ollama
        except ImportError:
            logger.warning("ollama SDK no instalado. Omitiendo análisis de imagen.")
            return None

        image_path = Path(image_path)
        if not image_path.exists():
            logger.warning(f"Imagen no encontrada: {image_path}")
            return None

        try:
            client = ollama.Client(host=self.base_url)
            response = client.chat(
                model=self.model,
                messages=[{
                    "role": "user",
                    "content": self.SYSTEM_PROMPT,
                    "images": [str(image_path)]
                }]
            )

            text = response["message"]["content"].strip()

            if "DESCARTAR" in text.upper():
                logger.info(f"  → Imagen descartada: {image_path.name}")
                return None

            logger.info(
                f"  → Imagen descrita ({len(text)} chars): {image_path.name}"
            )
            return text

        except Exception as e:
            logger.warning(f"Error analizando imagen {image_path.name}: {e}")
            return None
