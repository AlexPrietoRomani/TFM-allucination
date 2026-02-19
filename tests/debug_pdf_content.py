import sys
import os
from pathlib import Path

# Add root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.knowledge.loaders import DocumentLoader

def check_pdf():
    output = []
    pdf_path = Path("corpus/raw/arxiv-2403.05479.pdf")
    output.append(f"--- CHECKING PDF CONTENT: {pdf_path} ---")
    
    if not pdf_path.exists():
        output.append("ERROR: File not found!")
    else:
        try:
            docs = DocumentLoader.load_pdf(pdf_path)
            output.append(f"Pages Loaded: {len(docs)}")
            
            full_text = "\n".join([d.page_content for d in docs])
            output.append(f"Total Characters: {len(full_text)}")
            
            output.append("\n--- FIRST 500 CHARS ---")
            output.append(full_text[:500])
            
            output.append("\n--- SEARCH FOR 'Telenomus' ---")
            if "Telenomus" in full_text:
                output.append("✅ 'Telenomus' FOUND in text.")
                idx = full_text.find('Telenomus')
                ctx = full_text[idx:idx+200].replace('\n', ' ')
                output.append(f"Context: {ctx}...")
            else:
                output.append("❌ 'Telenomus' NOT FOUND in extracted text.")
                
        except Exception as e:
            output.append(f"Error loading PDF: {e}")

    with open("tests/debug_pdf_out.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output))

if __name__ == "__main__":
    check_pdf()
