"""
Script para buscar, verificar y descargar artículos científicos de ArXiv
sobre manejo integrado de plagas, fitosanidad y enfermedades de cultivos
(con enfoque en arándanos y frutales) y su relación con el clima.

Genera un CSV de búsqueda y luego descarga los PDFs al directorio corpus/raw.
Actualiza el registry.yaml con los nuevos documentos.

Autor: Generado automáticamente
Fecha: 2026-02-18
"""

import arxiv
import pandas as pd
import os
import re
import time
import hashlib
import yaml
from datetime import datetime

# ─── Configuración ──────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(BASE_DIR, "raw")
REGISTRY_FILE = os.path.join(BASE_DIR, "registry.yaml")
CSV_SEARCH = os.path.join(BASE_DIR, "articulos_fitosanitarios_busqueda.csv")
CSV_FINAL = os.path.join(BASE_DIR, "articulos_fitosanitarios_final.csv")

# IDs recopilados de las búsquedas en ArXiv MCP (selección curada de 30 artículos)
# Estos IDs provienen de búsquedas con los queries:
#   - "plant disease" AND deep learning
#   - "pest" AND agriculture AND detection/prediction
#   - "crop pest" AND climate/IPM
CURATED_ARXIV_IDS = [
    # --- Detección de enfermedades de plantas con DL ---
    "2504.07342",   # Bibliometric analysis DL plant disease 2025
    "1604.03169",   # Using Deep Learning for Image-Based Plant Disease Detection (Seminal 2016)
    "2312.07905",   # Plant Disease Datasets in the Age of Deep Learning 2023
    "2305.11533",   # Embrace Limited Training Datasets: Plant Disease DL 2023
    "2412.07408",   # Explainability of DL-Based Plant Disease Classifiers 2024
    "2508.08317",   # Evaluation State-of-the-Art DL for Plant Disease and Pest 2025
    "2503.16628",   # MobilePlantViT: Mobile-friendly Hybrid ViT Plant Disease 2025
    "2505.02877",   # Wireless Collaborated Inference for Plant Disease 2025
    "2404.16833",   # Leaf-Based Plant Disease Detection and Explainable AI 2023
    "2504.20948",   # DS_FusionNet: Dynamic Dual-Stream Fusion Plant Disease 2025
    "2508.10817",   # Mobile-Friendly DL for Plant Disease 101 Classes 2025
    "2512.18500",   # PlantDiseaseNet-RT50: Fine-tuned ResNet50 2025
    "2207.07919",   # PlantXViT: Vision Transformer for Plant Disease 2022
    "2409.04038",   # PlantSeg: Large-Scale In-the-wild Dataset Plant Disease 2024
    "2508.17653",   # FloraSyntropy-Net: Scalable DL with Novel Archive 2025

    # --- Detección de plagas con tecnología ---
    "2108.00421",   # Automated Pest Detection with DNN on the Edge 2021
    "2505.02441",   # MSFNet-CPD: Multi-Scale Cross-Modal Fusion Crop Pest 2025
    "2507.01494",   # Crop Pest Classification Using DL: Review 2025
    "2601.00243",   # Context-Aware Pesticide Recommendation via Few-Shot 2026
    "2205.07723",   # Pest presence prediction using interpretable ML 2022
    "2312.10948",   # Multimodal Approach for Advanced Pest Detection 2023
    "2407.18000",   # Plant pest identification framework practical 2024
    "2510.00547",   # Forestpest-YOLO: High-Performance Small Pest Detection 2025
    "2512.11871",   # Automated Plant Disease and Pest Detection Hybrid 2025

    # --- MIP, clima y control biológico ---
    "2312.04343",   # Causality and Explainability for Trustworthy IPM 2023
    "2403.05479",   # Temperature affects impact of insecticides on parasitoid 2024
    "2510.24650",   # Advancing site-specific disease/pest in precision agri 2025
    "1602.06584",   # Model-based approach: pest biocontrol by natural enemies 2016
    "2004.11252",   # Weakly Supervised Learning for Citrus Pest (IPM) 2020
    "2111.00298",   # YOLOv4 fine-grain object detection plant disease 2021
]

def compute_sha256(filepath):
    """Calcula el hash SHA-256 de un archivo."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def determine_relevance(title, summary):
    """Calcula relevancia con fitosanidad en arándanos según keywords."""
    text = (str(title) + " " + str(summary)).lower()
    score = 0
    keywords_found = []

    scoring = {
        'blueberry': 5, 'vaccinium': 5, 'arándano': 5,
        'berry': 4, 'fruit crop': 4,
        'pest management': 4, 'integrated pest': 5, 'ipm': 5,
        'phytosanitary': 4, 'plant disease': 4, 'crop disease': 4,
        'fungal': 3, 'fungus': 3, 'botrytis': 5, 'rust': 3,
        'climate': 3, 'temperature': 3,
        'detection': 2, 'deep learning': 2, 'classification': 2,
        'pest': 3, 'insect': 2,
        'biological control': 4, 'biocontrol': 4,
        'pesticide': 3, 'insecticide': 3,
        'crop protection': 3, 'agriculture': 2,
        'latin america': 5, 'south america': 5,
        'precision agriculture': 3,
    }

    for kw, val in scoring.items():
        if kw in text:
            score += val
            keywords_found.append(kw)

    if score >= 12:
        level = "Alta"
    elif score >= 7:
        level = "Media"
    else:
        level = "Baja"

    return f"{level} ({score})", "; ".join(keywords_found)


def clean_abstract_short(text, max_len=250):
    """Genera un resumen muy corto a partir del abstract."""
    if not text:
        return ""
    cleaned = text.replace('\n', ' ').strip()
    sentences = re.split(r'(?<=[.!?])\s+', cleaned)
    short = ""
    for s in sentences:
        if len(short) + len(s) <= max_len:
            short += s + " "
        else:
            break
    return short.strip() if short.strip() else cleaned[:max_len]


def main():
    os.makedirs(RAW_DIR, exist_ok=True)

    client = arxiv.Client(
        page_size=10,
        delay_seconds=1,
        num_retries=3
    )

    # ────────────────────────────────────────────────────────────────────────
    # PASO 1: Obtener metadatos de ArXiv para los IDs curados
    # ────────────────────────────────────────────────────────────────────────
    print("=" * 60)
    print("PASO 1: Obteniendo metadatos de ArXiv...")
    print("=" * 60)

    search_results = []

    search = arxiv.Search(id_list=CURATED_ARXIV_IDS)
    
    for paper in client.results(search):
        paper_id = paper.entry_id.split("/abs/")[-1].split("v")[0]
        authors_str = ", ".join([a.name for a in paper.authors])
        categories_str = ", ".join(paper.categories)
        short_abstract = clean_abstract_short(paper.summary)
        relevance, keywords = determine_relevance(paper.title, paper.summary)

        search_results.append({
            'Año de publicación': paper.published.year,
            'Autores': authors_str,
            'Titulo del articulo': paper.title,
            'DOI correcto': paper.doi if paper.doi else f"ArXiv:{paper_id}",
            'Palabras clave': f"{categories_str}; {keywords}",
            'Resumen muy corto': short_abstract,
            'Relevancia con fitosanidad en arándanos': relevance,
            '_paper_id': paper_id,
            '_pdf_url': paper.pdf_url,
            '_entry_id': paper.entry_id,
            '_categories': paper.categories,
            '_full_summary': paper.summary,
        })
        print(f"  ✓ [{paper.published.year}] {paper.title[:60]}...")

    print(f"\nTotal artículos obtenidos: {len(search_results)}")

    # Guardar CSV de búsqueda (sin columnas internas)
    df_search = pd.DataFrame(search_results)
    public_cols = [
        'Año de publicación', 'Autores', 'Titulo del articulo',
        'DOI correcto', 'Palabras clave', 'Resumen muy corto',
        'Relevancia con fitosanidad en arándanos'
    ]
    df_search[public_cols].to_csv(CSV_SEARCH, sep=';', index=False, encoding='utf-8-sig')
    print(f"CSV de búsqueda guardado: {CSV_SEARCH}")

    # ────────────────────────────────────────────────────────────────────────
    # PASO 2: Descargar PDFs
    # ────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("PASO 2: Descargando PDFs...")
    print("=" * 60)

    for item in search_results:
        paper_id = item['_paper_id']
        safe_title = re.sub(r'[^\w\s-]', '', item['Titulo del articulo'])[:50].strip()
        safe_title = re.sub(r'\s+', '_', safe_title)
        filename = f"arxiv-{paper_id}.pdf"
        filepath = os.path.join(RAW_DIR, filename)

        if os.path.exists(filepath):
            item['Estado Descarga'] = "Ya existente"
            item['Ruta Local'] = filename
            print(f"  ⏭ Ya existe: {filename}")
            continue

        print(f"  ⬇ Descargando: {filename}...")
        try:
            # Descargar usando arxiv library
            search_dl = arxiv.Search(id_list=[paper_id])
            paper_obj = next(client.results(search_dl))
            paper_obj.download_pdf(dirpath=RAW_DIR, filename=filename)
            item['Estado Descarga'] = "Success"
            item['Ruta Local'] = filename
            print(f"    ✓ Descargado correctamente")
        except Exception as e:
            item['Estado Descarga'] = f"Failed: {str(e)[:80]}"
            item['Ruta Local'] = ""
            print(f"    ✗ Error: {e}")

    # ────────────────────────────────────────────────────────────────────────
    # PASO 3: Guardar CSV final con columnas de descarga
    # ────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("PASO 3: Generando CSV final...")
    print("=" * 60)

    final_cols = public_cols + [
        'Estado Descarga', 'Ruta Local', 'Hoja Origen', 'URL ArXiv'
    ]
    for item in search_results:
        item['Hoja Origen'] = "ArXiv MCP Search"
        item['URL ArXiv'] = item.get('_entry_id', '')

    df_final = pd.DataFrame(search_results)
    df_final[final_cols].to_csv(CSV_FINAL, sep=';', index=False, encoding='utf-8-sig')
    print(f"CSV final guardado: {CSV_FINAL}")

    # ────────────────────────────────────────────────────────────────────────
    # PASO 4: Actualizar registry.yaml
    # ────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("PASO 4: Actualizando registry.yaml...")
    print("=" * 60)

    # Cargar registry existente
    with open(REGISTRY_FILE, 'r', encoding='utf-8') as f:
        registry = yaml.safe_load(f)

    if registry is None:
        registry = {'documents': []}
    if 'documents' not in registry:
        registry['documents'] = []

    existing_ids = {doc['id'] for doc in registry['documents']}

    new_entries = 0
    for item in search_results:
        paper_id = item['_paper_id']
        doc_id = f"arxiv-{paper_id}"
        filepath = os.path.join(RAW_DIR, f"{doc_id}.pdf")

        if doc_id in existing_ids:
            print(f"  ⏭ Ya registrado: {doc_id}")
            continue

        if item.get('Estado Descarga') != 'Success' and item.get('Estado Descarga') != 'Ya existente':
            print(f"  ⏭ No descargado, omitiendo: {doc_id}")
            continue

        # Calcular checksum
        checksum = ""
        if os.path.exists(filepath):
            checksum = compute_sha256(filepath)

        # Determinar tags relevantes
        tags = []
        text_lower = (item['Titulo del articulo'] + " " + item.get('_full_summary', '')).lower()

        tag_map = {
            'plant disease': 'enfermedades de plantas',
            'pest detection': 'detección de plagas',
            'pest management': 'manejo de plagas',
            'integrated pest': 'manejo integrado de plagas',
            'deep learning': 'deep learning',
            'classification': 'clasificación de imágenes',
            'climate': 'clima',
            'temperature': 'temperatura',
            'biocontrol': 'control biológico',
            'precision agriculture': 'agricultura de precisión',
            'crop': 'cultivos',
            'fruit': 'frutales',
            'insecticide': 'insecticidas',
            'pesticide': 'plaguicidas',
            'computer vision': 'visión por computadora',
            'transformer': 'transformer',
            'mobile': 'dispositivos móviles',
        }

        for keyword, tag in tag_map.items():
            if keyword in text_lower and tag not in tags:
                tags.append(tag)

        # Agregar tag de ArXiv
        tags.append("artículo científico")
        tags.append("ArXiv")

        new_doc = {
            'id': doc_id,
            'title': item['Titulo del articulo'],
            'url': item.get('_entry_id', ''),
            'type': 'pdf',
            'language': 'en',
            'tags': tags,
            'description': clean_abstract_short(item.get('_full_summary', ''), 300),
            'year': int(item['Año de publicación']),
            'country': 'Internacional',
            'source': f"ArXiv ({', '.join(item.get('_categories', []))})",
            'doc_type': 'Artículo científico',
            'checksum': checksum,
        }

        registry['documents'].append(new_doc)
        existing_ids.add(doc_id)
        new_entries += 1
        print(f"  ✓ Agregado: {doc_id}")

    # Guardar registry
    with open(REGISTRY_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(registry, f, allow_unicode=True, default_flow_style=False, sort_keys=False, width=100)

    print(f"\nNuevos documentos en registry: {new_entries}")
    print(f"Total documentos en registry: {len(registry['documents'])}")

    # ────────────────────────────────────────────────────────────────────────
    # Resumen final
    # ────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("RESUMEN FINAL")
    print("=" * 60)
    success = sum(1 for i in search_results if i.get('Estado Descarga') in ('Success', 'Ya existente'))
    failed = len(search_results) - success
    print(f"  Artículos buscados:     {len(search_results)}")
    print(f"  Descargas exitosas:     {success}")
    print(f"  Descargas fallidas:     {failed}")
    print(f"  Nuevos en registry:     {new_entries}")
    print(f"  CSV búsqueda:           {CSV_SEARCH}")
    print(f"  CSV final:              {CSV_FINAL}")
    print(f"  Registry actualizado:   {REGISTRY_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()
