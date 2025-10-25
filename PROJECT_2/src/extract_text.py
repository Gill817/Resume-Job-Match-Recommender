# src/extract_text.py
import os
from pathlib import Path
import PyPDF2
import docx
from tqdm import tqdm

def extract_text_from_pdf(path):
    text_parts = []
    try:
        with open(path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for p in reader.pages:
                txt = p.extract_text()
                if txt:
                    text_parts.append(txt)
    except Exception as e:
        print(f"PDF read error {path}: {e}")
    return "\n".join(text_parts)

def extract_text_from_docx(path):
    try:
        doc = docx.Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        print(f"DOCX read error {path}: {e}")
        return ""

def extract_text_from_txt(path):
    try:
        return Path(path).read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        print(f"TXT read error {path}: {e}")
        return ""

def extract_text(path):
    p = Path(path)
    ext = p.suffix.lower()
    if ext == '.pdf':
        return extract_text_from_pdf(path)
    elif ext in ('.docx', '.doc'):
        return extract_text_from_docx(path)
    elif ext == '.txt':
        return extract_text_from_txt(path)
    else:
        print(f"Unsupported file {path}")
        return ""

def batch_extract(input_dir, output_csv):
    import pandas as pd
    rows = []
    for root, _, files in os.walk(input_dir):
        for fn in files:
            if fn.startswith('.'):
                continue
            full = os.path.join(root, fn)
            txt = extract_text(full)
            rows.append({"file": fn, "path": full, "text_raw": txt})
    df = pd.DataFrame(rows)
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"Saved {len(df)} rows to {output_csv}")

if __name__ == "__main__":
    import sys
    input_dir = sys.argv[1]  # e.g. data/resumes_raw
    output_csv = sys.argv[2] # e.g. data/resumes_extracted.csv
    batch_extract(input_dir, output_csv)
