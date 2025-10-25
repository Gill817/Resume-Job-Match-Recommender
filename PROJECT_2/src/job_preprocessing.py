import sys, os
sys.path.append(os.path.dirname(__file__))

from clean_text import clean_text_spacy
import pandas as pd

# Paths
DATA_FOLDER = r"C:\Users\PROJECT_2\DATA"
INPUT_CSV = os.path.join(DATA_FOLDER, "postings.csv")
OUTPUT_CSV = os.path.join(DATA_FOLDER, "postings_cleaned.csv")

print("Step 1: Checking if input file exists...")
if not os.path.exists(INPUT_CSV):
    print(f"❌ Input file not found: {INPUT_CSV}")
    sys.exit(1)
else:
    print(f"✅ Found input file: {INPUT_CSV}")

print("Step 2: Reading job postings CSV...")
df_jobs = pd.read_csv(INPUT_CSV, low_memory=False)
print(f"✅ Loaded {len(df_jobs)} rows")

print("Step 3: Filling NaN descriptions...")
df_jobs['description'] = df_jobs['description'].fillna("")

print("Step 4: Cleaning text (this may take a while)...")
df_jobs['description_clean'] = df_jobs['description'].apply(
    lambda x: clean_text_spacy(x, lemmatize=True, remove_stopwords=True)
)

print("Step 5: Saving cleaned data...")
df_jobs.to_csv(OUTPUT_CSV, index=False, encoding='utf-8')

print(f"✅ Saved cleaned job postings to: {OUTPUT_CSV}")
