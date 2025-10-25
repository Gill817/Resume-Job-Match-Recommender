import re
import spacy
from bs4 import BeautifulSoup

# Load small English model
nlp = spacy.load("en_core_web_sm", disable=["parser","ner"])

def strip_html(text):
    return BeautifulSoup(text, "html.parser").get_text(separator=" ")

RE_NON_ALPHANUM = re.compile(r'[^A-Za-z0-9\s\+\#\.\-]')  # allow plus/hash for C++/C#
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
