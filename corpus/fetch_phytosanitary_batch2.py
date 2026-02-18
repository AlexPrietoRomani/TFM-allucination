"""
Batch 2: Artículos científicos para agrónomo de campo – fitosanidad, MIP,
moléculas, control biológico, dinámica de plagas/enfermedades + clima.

Proceso:
  1. Cargar curated_arxiv_ids.json, verificar ya descargados en corpus/raw.
  2. Buscar metadatos de nuevos IDs en ArXiv.
  3. Agregar resultados al CSV de búsqueda existente.
  4. Descargar PDFs SOLO de los nuevos artículos.
  5. Actualizar registry.yaml SOLO con los nuevos artículos descargados.
"""

import arxiv
import pandas as pd
import os
import re
import json
import hashlib
import yaml

# ─── Configuración ──────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(BASE_DIR, "raw")
REGISTRY_FILE = os.path.join(BASE_DIR, "registry.yaml")
JSON_IDS_FILE = os.path.join(BASE_DIR, "curated_arxiv_ids.json")
CSV_SEARCH = os.path.join(BASE_DIR, "articulos_fitosanitarios_busqueda.csv")
CSV_FINAL = os.path.join(BASE_DIR, "articulos_fitosanitarios_final.csv")

# ─── 30 nuevos IDs: artículos para agrónomo de campo ────────────────────────
BATCH2_IDS = [
    # --- Resistencia a fungicidas y herbicidas ---
    "1301.6561",    # Fungicide mixtures: resistance risk vs. disease control
    "2302.03471",   # Atrazine mutation: herbicide resistance changed agriculture
    "2512.13718",   # Wild oat economic thresholds: integrated weed management

    # --- Epidemiología de patógenos vegetales ---
    "1903.02246",   # Microbiomes & pathogen survival in crop residues
    "1210.1844",    # Prediction of invasion from early stage of epidemic (fungal)
    "2306.13869",   # Spore dispersal via rain-leaf interactions (disease spread)
    "1305.4206",    # Phytophthora infestans lineage: Irish potato famine
    "2004.09644",   # Phytophthora zoospore propagation: percolation barriers
    "1408.6616",    # Insect-borne plant disease model: Flavescence dorée grapevine
    "2310.07442",   # Network theory crop parasite surveillance & control
    "1911.07007",   # Air mass movement networks: airborne pathogen dispersal

    # --- Control biológico y moléculas ---
    "2103.06007",   # Pest control with biopesticides: awareness model + ICM
    "2009.10378",   # Mycosubtilin overproduction Bacillus subtilis: biocontrol
    "2009.10375",   # Temperature-dependent mycosubtilin: antifungal vs phytopathogens
    "2404.03839",   # Trichoderma fungus kinetics: mathematical model
    "2303.05242",   # Endophytic fungi (Trichoderma harzianum): antimicrobial activity
    "2010.14944",   # Biocontrol of invasive plants: herbivores + native resistance
    "2512.11474",   # AI for agroecological crop protection: biocontrol agents lists

    # --- Dinámica plagas + clima ---
    "2508.03238",   # Soybean pod borer population: temperature-humidity dynamics
    "2112.11448",   # Pest reproductive number: temperature sensitivity (lanternfly)
    "2312.03338",   # Spotted lanternfly invasion spread modeling
    "2109.00121",   # Aphid dynamics on soybean: virulent/avirulent interactions
    "2510.06111",   # Bio-control patch model: climate change & pest extinction

    # --- MIP, redes de monitoreo, clima + agricultura ---
    "2002.00951",   # Pest monitoring networks: reduce pesticide use
    "2504.04965",   # Climate adaptation millet/sorghum: IPM + climate constraints
    "2403.19273",   # Crop disease forecasting: soil + weather + ML framework
    "2305.14357",   # Nano-fertilizers: nutrient use efficiency & soil health
    "1807.07343",   # Grapevine: Botrytis resilience phenotyping (epicuticular wax)
    "2403.01383",   # Postharvest litchi: alginate oligosaccharides quality preservation
    "2506.15728",   # Field diagnosis Phytophthora: CRISPR smartphone system
]

def compute_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def determine_relevance(title, summary):
    text = (str(title) + " " + str(summary)).lower()
    score = 0
    keywords_found = []
    scoring = {
        'blueberry': 5, 'vaccinium': 5, 'arándano': 5,
        'berry': 4, 'fruit crop': 4, 'grapevine': 3, 'grape': 3,
        'pest management': 4, 'integrated pest': 5, 'ipm': 5,
        'phytosanitary': 4, 'plant disease': 4, 'crop disease': 4,
        'fungal': 3, 'fungus': 3, 'botrytis': 5, 'rust': 3,
        'phytophthora': 5, 'colletotrichum': 4, 'alternaria': 4,
        'climate': 3, 'temperature': 3, 'weather': 3, 'humidity': 3,
        'fungicide': 5, 'insecticide': 4, 'herbicide': 4,
        'resistance': 3, 'pesticide': 3,
        'biocontrol': 5, 'biological control': 5, 'biopesticide': 5,
        'trichoderma': 5, 'bacillus': 4, 'mycosubtilin': 5,
        'endophytic': 4, 'antagonistic': 3,
        'pathogen': 3, 'epidemiology': 3, 'epidemic': 3,
        'spore': 4, 'dispersal': 3,
        'pest population': 4, 'pest dynamics': 4,
        'crop protection': 3, 'agriculture': 2,
        'postharvest': 4, 'post-harvest': 4,
        'field': 2, 'crop residue': 3,
        'monitoring': 2, 'surveillance': 3,
        'precision agriculture': 3,
        'nano-fertilizer': 3, 'soil health': 3,
        'latin america': 5, 'south america': 5,
    }
    for kw, val in scoring.items():
        if kw in text:
            score += val
            keywords_found.append(kw)
    if score >= 15:
        level = "Alta"
    elif score >= 9:
        level = "Media"
    else:
        level = "Baja"
    return f"{level} ({score})", "; ".join(keywords_found)


def clean_abstract_short(text, max_len=250):
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

    # ─── VERIFICAR QUÉ YA EXISTE ────────────────────────────────────────────
    print("=" * 60)
    print("VERIFICANDO ARCHIVOS EXISTENTES...")
    print("=" * 60)

    existing_pdfs = set()
    for f in os.listdir(RAW_DIR):
        if f.endswith(".pdf"):
            existing_pdfs.add(f)
    print(f"PDFs ya en corpus/raw: {len(existing_pdfs)}")

    # Cargar registry
    with open(REGISTRY_FILE, 'r', encoding='utf-8') as f:
        registry = yaml.safe_load(f)
    if registry is None:
        registry = {'documents': []}
    if 'documents' not in registry:
        registry['documents'] = []
    existing_registry_ids = {doc['id'] for doc in registry['documents']}
    print(f"Documentos ya en registry: {len(existing_registry_ids)}")

    # Verificar cuáles de batch2 ya están descargados
    new_ids = []
    skipped_ids = []
    for pid in BATCH2_IDS:
        fname = f"arxiv-{pid}.pdf"
        doc_id = f"arxiv-{pid}"
        if fname in existing_pdfs and doc_id in existing_registry_ids:
            skipped_ids.append(pid)
        else:
            new_ids.append(pid)

    print(f"\nIDs a procesar (nuevos): {len(new_ids)}")
    print(f"IDs ya existentes (omitir descarga+registry): {len(skipped_ids)}")
    for sid in skipped_ids:
        print(f"  ⏭ Ya existe: arxiv-{sid}")

    if not new_ids:
        print("\n¡Todos los artículos del batch 2 ya están descargados y registrados!")
        return

    # ─── PASO 1: OBTENER METADATOS ──────────────────────────────────────────
    print("\n" + "=" * 60)
    print("PASO 1: Obteniendo metadatos de ArXiv...")
    print("=" * 60)

    client = arxiv.Client(page_size=10, delay_seconds=1, num_retries=3)
    search = arxiv.Search(id_list=new_ids)

    results = []
    for paper in client.results(search):
        paper_id = paper.entry_id.split("/abs/")[-1].split("v")[0]
        authors_str = ", ".join([a.name for a in paper.authors])
        categories_str = ", ".join(paper.categories)
        short_abstract = clean_abstract_short(paper.summary)
        relevance, keywords = determine_relevance(paper.title, paper.summary)

        results.append({
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
        print(f"  ✓ [{paper.published.year}] {paper.title[:65]}...")

    print(f"\nMetadatos obtenidos: {len(results)}")

    # ─── PASO 2: AGREGAR AL CSV DE BÚSQUEDA ─────────────────────────────────
    print("\n" + "=" * 60)
    print("PASO 2: Actualizando CSV de búsqueda...")
    print("=" * 60)

    public_cols = [
        'Año de publicación', 'Autores', 'Titulo del articulo',
        'DOI correcto', 'Palabras clave', 'Resumen muy corto',
        'Relevancia con fitosanidad en arándanos'
    ]

    # Leer CSV existente
    if os.path.exists(CSV_SEARCH):
        df_existing = pd.read_csv(CSV_SEARCH, sep=';', encoding='utf-8-sig')
        print(f"  CSV existente: {len(df_existing)} filas")
    else:
        df_existing = pd.DataFrame(columns=public_cols)

    df_new = pd.DataFrame(results)[public_cols]
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    df_combined.to_csv(CSV_SEARCH, sep=';', index=False, encoding='utf-8-sig')
    print(f"  CSV actualizado: {len(df_combined)} filas totales")

    # ─── PASO 3: DESCARGAR PDFs SOLO NUEVOS ─────────────────────────────────
    print("\n" + "=" * 60)
    print("PASO 3: Descargando PDFs nuevos...")
    print("=" * 60)

    for item in results:
        paper_id = item['_paper_id']
        filename = f"arxiv-{paper_id}.pdf"
        filepath = os.path.join(RAW_DIR, filename)

        if os.path.exists(filepath):
            item['Estado Descarga'] = "Ya existente"
            item['Ruta Local'] = filename
            print(f"  ⏭ Ya existe: {filename}")
            continue

        print(f"  ⬇ Descargando: {filename}...")
        try:
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

    # ─── PASO 4: ACTUALIZAR CSV FINAL ────────────────────────────────────────
    print("\n" + "=" * 60)
    print("PASO 4: Actualizando CSV final...")
    print("=" * 60)

    final_cols = public_cols + [
        'Estado Descarga', 'Ruta Local', 'Hoja Origen', 'URL ArXiv'
    ]
    for item in results:
        item['Hoja Origen'] = "ArXiv Batch 2 - Agronomía de campo"
        item['URL ArXiv'] = item.get('_entry_id', '')

    if os.path.exists(CSV_FINAL):
        df_final_existing = pd.read_csv(CSV_FINAL, sep=';', encoding='utf-8-sig')
        print(f"  CSV final existente: {len(df_final_existing)} filas")
    else:
        df_final_existing = pd.DataFrame(columns=final_cols)

    df_final_new = pd.DataFrame(results)
    # Asegurar columnas correctas
    for col in final_cols:
        if col not in df_final_new.columns:
            df_final_new[col] = ""
    df_final_combined = pd.concat(
        [df_final_existing, df_final_new[final_cols]], ignore_index=True
    )
    df_final_combined.to_csv(CSV_FINAL, sep=';', index=False, encoding='utf-8-sig')
    print(f"  CSV final actualizado: {len(df_final_combined)} filas totales")

    # ─── PASO 5: ACTUALIZAR REGISTRY.YAML SOLO NUEVOS ───────────────────────
    print("\n" + "=" * 60)
    print("PASO 5: Actualizando registry.yaml...")
    print("=" * 60)

    new_entries = 0
    for item in results:
        paper_id = item['_paper_id']
        doc_id = f"arxiv-{paper_id}"
        filepath = os.path.join(RAW_DIR, f"{doc_id}.pdf")

        if doc_id in existing_registry_ids:
            print(f"  ⏭ Ya registrado: {doc_id}")
            continue

        status = item.get('Estado Descarga', '')
        if status not in ('Success', 'Ya existente'):
            print(f"  ⏭ No descargado, omitiendo: {doc_id}")
            continue

        checksum = ""
        if os.path.exists(filepath):
            checksum = compute_sha256(filepath)

        tags = []
        text_lower = (item['Titulo del articulo'] + " " +
                      item.get('_full_summary', '')).lower()

        tag_map = {
            'fungicide': 'fungicidas',
            'herbicide': 'herbicidas',
            'insecticide': 'insecticidas',
            'resistance': 'resistencia',
            'biocontrol': 'control biológico',
            'biological control': 'control biológico',
            'biopesticide': 'biopesticidas',
            'trichoderma': 'Trichoderma',
            'bacillus': 'Bacillus',
            'mycosubtilin': 'mycosubtilin',
            'phytophthora': 'Phytophthora',
            'botrytis': 'Botrytis',
            'pathogen': 'patógenos vegetales',
            'epidem': 'epidemiología',
            'spore': 'dispersión de esporas',
            'pest management': 'manejo de plagas',
            'integrated pest': 'manejo integrado de plagas',
            'pest population': 'dinámica de poblaciones',
            'climate': 'clima',
            'temperature': 'temperatura',
            'monitoring': 'monitoreo fitosanitario',
            'crop protection': 'protección de cultivos',
            'postharvest': 'poscosecha',
            'nano-fertilizer': 'nano-fertilizantes',
            'soil health': 'salud del suelo',
            'grapevine': 'vid',
            'fruit': 'frutales',
            'weed': 'malezas',
            'invasive': 'especies invasoras',
        }

        for keyword, tag in tag_map.items():
            if keyword in text_lower and tag not in tags:
                tags.append(tag)

        tags.append("artículo científico")
        tags.append("ArXiv")
        tags.append("agronomía de campo")

        new_doc = {
            'id': doc_id,
            'title': item['Titulo del articulo'],
            'url': item.get('_entry_id', ''),
            'type': 'pdf',
            'language': 'en',
            'tags': tags,
            'description': clean_abstract_short(
                item.get('_full_summary', ''), 300),
            'year': int(item['Año de publicación']),
            'country': 'Internacional',
            'source': f"ArXiv ({', '.join(item.get('_categories', []))})",
            'doc_type': 'Artículo científico',
            'checksum': checksum,
        }

        registry['documents'].append(new_doc)
        existing_registry_ids.add(doc_id)
        new_entries += 1
        print(f"  ✓ Agregado: {doc_id}")

    with open(REGISTRY_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(registry, f, allow_unicode=True, default_flow_style=False,
                  sort_keys=False, width=100)
    print(f"\nNuevos documentos en registry: {new_entries}")
    print(f"Total documentos en registry: {len(registry['documents'])}")

    # ─── PASO 6: ACTUALIZAR JSON DE IDS ──────────────────────────────────────
    print("\n" + "=" * 60)
    print("PASO 6: Actualizando curated_arxiv_ids.json...")
    print("=" * 60)

    with open(JSON_IDS_FILE, 'r', encoding='utf-8') as f:
        ids_json = json.load(f)

    ids_json['batch_2_agronomia_campo']['ids'] = BATCH2_IDS
    ids_json['batch_2_agronomia_campo']['date_added'] = "2026-02-18"

    with open(JSON_IDS_FILE, 'w', encoding='utf-8') as f:
        json.dump(ids_json, f, ensure_ascii=False, indent=2)
    print(f"  ✓ JSON actualizado con {len(BATCH2_IDS)} IDs del batch 2")

    # ─── RESUMEN FINAL ───────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("RESUMEN FINAL - BATCH 2 (Agronomía de campo)")
    print("=" * 60)
    success = sum(1 for i in results
                  if i.get('Estado Descarga') in ('Success', 'Ya existente'))
    failed = len(results) - success
    print(f"  Artículos procesados:     {len(results)}")
    print(f"  Descargas exitosas:       {success}")
    print(f"  Descargas fallidas:       {failed}")
    print(f"  Nuevos en registry:       {new_entries}")
    print(f"  CSV búsqueda total:       {CSV_SEARCH}")
    print(f"  CSV final total:          {CSV_FINAL}")
    print(f"  Registry actualizado:     {REGISTRY_FILE}")
    print(f"  IDs JSON actualizado:     {JSON_IDS_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()
