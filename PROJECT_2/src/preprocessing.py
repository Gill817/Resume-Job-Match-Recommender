# src/preprocessing.py

import pandas as pd
import re
from bs4 import BeautifulSoup
import spacy

# --- Initialize spaCy ---
nlp = spacy.load("en_core_web_sm", disable=["parser","ner"])  # smaller pipeline

# --- Cleaning functions (from clean_text.py) ---
def strip_html(text):
    return BeautifulSoup(text, "html.parser").get_text(separator=" ")

RE_NON_ALPHANUM = re.compile(r'[^A-Za-z0-9\s\+\#\.\-]')
RE_MULTISPACE = re.compile(r'\s+')

def clean_text_basic(text):
    if not isinstance(text, str):
        return ""
    t = text.lower()
    t = strip_html(t)
    t = RE_NON_ALPHANUM.sub(' ', t)
    t = RE_MULTISPACE.sub(' ', t).strip()
    return t

def clean_text_spacy(text, lemmatize=True, remove_stopwords=True):
    text = clean_text_basic(text)
    doc = nlp(text)
    tokens = []
    for token in doc:
        if token.is_space:
            continue
        if remove_stopwords and token.is_stop:
            continue
        if lemmatize:
            tok = token.lemma_.strip()
        else:
            tok = token.text.strip()
        if tok:
            tokens.append(tok)
    return " ".join(tokens)

# --- CONFIG ---
INPUT_CSV = "DATA/Resume.csv"  # change to your CSV
OUTPUT_CSV = "DATA/resumes_cleaned.csv"

# --- Read CSV ---
df = pd.read_csv(INPUT_CSV)

# --- Clean Resume_h ---
df['Resume_clean'] = df['Resume_html'].apply(lambda x: clean_text_spacy(x, lemmatize=True, remove_stopwords=True))

# --- Save cleaned CSV ---
df.to_csv(OUTPUT_CSV, index=False)

print(f"Cleaning done, saved to {OUTPUT_CSV}")
