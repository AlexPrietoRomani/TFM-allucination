"""
parsers.py — Pipeline de Parseo Estructurado para PDFs Tabulares

Convierte PDFs complejos (manuales FRAC/IRAC, guías fitosanitarias)
en Markdown estructurado con tablas preservadas y opcionalmente
aplana filas tabulares a oraciones descriptivas para mejorar la
precisión de los embeddings.

Dependencias:
    pip install docling  (o uv add docling)
"""

import torch
import ollama
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
            from docling.document_converter import DocumentConverter, PdfFormatOption
            from docling.datamodel.pipeline_options import PdfPipelineOptions, AcceleratorOptions, AcceleratorDevice
            
            # 1. Configurar el Acelerador (GPU si está disponible, sino CPU)
            device = AcceleratorDevice.CUDA if torch.cuda.is_available() else AcceleratorDevice.CPU
            
            accel_options = AcceleratorOptions(
                num_threads=8,
                device=device
            )
            
            options = PdfPipelineOptions()
            options.accelerator_options = accel_options
            options.do_formula_enrichment = True
            options.generate_picture_images = True
            
            self._converter = DocumentConverter(
                format_options={
                    "pdf": PdfFormatOption(pipeline_options=options)
                }
            )
            logger.info(f"✅ Docling inicializado con acelerador: {device.name}")
            
        except ImportError as e:
            logger.error(f"Falta una dependencia para Docling: {e}")
            raise

    def parse(self, pdf_path: Path, image_filter: Optional[Any] = None) -> str:
        """Convierte un PDF a Markdown estructurado. Opcionalmente inyecta descripciones VLM.

        Args:
            pdf_path: Ruta al archivo PDF.
            image_filter: Instancia de ImageFilter para describir gráficos.

        Returns:
            String con el contenido en formato Markdown.
        """
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF no encontrado: {pdf_path}")

        logger.info(f"Parseando con Docling: {pdf_path.name}")
        result = self._converter.convert(str(pdf_path))
        doc = result.document

        # 1. Analizar imágenes con VLM consecutivamente si se pasan
        image_descriptions = []
        if image_filter and hasattr(doc, "pictures"):
            logger.info(f"  → Analizando {len(doc.pictures)} imágenes con VLM...")
            for i, pic in enumerate(doc.pictures):
                try:
                    img = pic.get_image(result.document)
                    import io
                    img_byte_arr = io.BytesIO()
                    img.save(img_byte_arr, format='PNG')
                    
                    desc = image_filter.analyze(img_byte_arr.getvalue())
                    image_descriptions.append(desc)
                except Exception as e:
                    logger.warning(f"  → Error procesando imagen {i} en VLM: {e}")
                    image_descriptions.append(None)

        md_content = doc.export_to_markdown()

        # 2. Inyectar descripciones VLM en las etiquetas <!-- image -->
        if image_descriptions:
            count = 0
            def _replace_image(match):
                nonlocal count
                if count < len(image_descriptions):
                    desc = image_descriptions[count]
                    count += 1
                    if desc:
                        return f"\n\n> **[💡 Descripción de Imagen VLM]:** {desc}\n\n"
                return match.group(0)
            
            md_content = re.sub(r"<!--\s*image\s*-->", _replace_image, md_content)

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
        "Eres un analista experto en extracción de datos científicos. "
        "Describe en un único párrafo corto y directo qué representa esta imagen "
        "(por ejemplo: 'Gráfico de líneas mostrando...', 'Diagrama de flujo de...'). "
        "Ignora cualquier texto que no puedas leer claramente. "
        "Si la imagen es solo un logotipo, un adorno, o texto borroso ilegible, "
        "debes responder EXACTAMENTE y ÚNICAMENTE con la palabra: DESCARTAR."
    )

    def __init__(self, model_name: str = "llama3.2-vision", base_url: str = "http://localhost:11434"):
        self.model = model_name
        self.base_url = base_url

    def analyze(self, image_path: Path) -> str | None:
        """Devuelve la descripción de la imagen o None si debe descartarse."""
        img_name = "imagen_memoria"
        if hasattr(image_path, 'name'):
            img_name = image_path.name

        try:
            client = ollama.Client(host=self.base_url)
            
            response = client.chat(
                model=self.model,
                messages=[{
                    "role": "user",
                    "content": self.SYSTEM_PROMPT,
                    "images": [str(image_path)]
                }],
                options={
                    "num_predict": 150,
                    "temperature": 0.1,
                    "top_p": 0.9,
                    "repeat_penalty": 1.0,
                    "stop": ["\n\n", "Fuente:"]
                }
            )

            text = response["message"]["content"].strip()
            logger.debug(f"VLM raw text = {repr(text)}")

            # Limpieza agresiva de caracteres invisibles
            text = text.replace('\xa0', ' ').replace('\xad', '')
            text = re.sub(r'([.…] ?){3,}', '...', text)
            text = re.sub(r'(\s){2,}', ' ', text)
            text = text.strip()

            if "DESCARTAR" in text.upper() or len(text) < 10:
                logger.info(f"  → {img_name} descartada")
                return None

            logger.info(f"  → {img_name} descrita ({len(text)} chars)")
            return text

        except Exception as e:
            logger.warning(f"  → Fallo en VLM para {img_name}: {e}")
            return None
