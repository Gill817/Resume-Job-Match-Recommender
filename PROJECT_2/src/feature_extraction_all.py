
import os
import pandas as pd
import scipy.sparse
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

DATA_FOLDER = r"C:\Users\PROJECT_2\DATA"
RESUMES_CSV = os.path.join(DATA_FOLDER, "resumes_cleaned.csv")
JOBS_CSV = os.path.join(DATA_FOLDER, "postings_cleaned.csv")

OUT_RESUMES_TFIDF = os.path.join(DATA_FOLDER, "resumes_tfidf.npz")
OUT_JOBS_TFIDF = os.path.join(DATA_FOLDER, "jobs_tfidf.npz")
OUT_TFIDF_VECT = os.path.join(DATA_FOLDER, "tfidf_vectorizer.pkl")

print("Loading cleaned CSVs...")
resumes_df = pd.read_csv(RESUMES_CSV, low_memory=False)
jobs_df = pd.read_csv(JOBS_CSV, low_memory=False)
print(f"Resumes: {resumes_df.shape}, Jobs: {jobs_df.shape}")

# checking whether columns exist or not 
if 'Resume_clean' not in resumes_df.columns:
    raise SystemExit("ERROR: 'Resume_clean' not in resumes_cleaned.csv")
if 'description_clean' not in jobs_df.columns:
    raise SystemExit("ERROR: 'description_clean' not in postings_cleaned.csv")

# Filling Nans
resumes_texts = resumes_df['Resume_clean'].fillna("").astype(str)
jobs_texts = jobs_df['description_clean'].fillna("").astype(str)

print("Preparing combined corpus for TF-IDF fitting...")
combined = pd.concat([resumes_texts, jobs_texts], ignore_index=True)

print("Fitting TF-IDF vectorizer on combined corpus (this may take a minute)...")
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
tfidf.fit(combined)
print("TF-IDF vocabulary size:", len(tfidf.vocabulary_))

print("Transforming resumes...")
resume_tfidf = tfidf.transform(resumes_texts)
print("Resume TF-IDF shape:", resume_tfidf.shape)

print("Transforming jobs (this may take a little while)...")
job_tfidf = tfidf.transform(jobs_texts)
print("Job TF-IDF shape:", job_tfidf.shape)

# Make sure output folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

print(f"Saving resume TF-IDF to {OUT_RESUMES_TFIDF} ...")
scipy.sparse.save_npz(OUT_RESUMES_TFIDF, resume_tfidf)

print(f"Saving job TF-IDF to {OUT_JOBS_TFIDF} ...")
scipy.sparse.save_npz(OUT_JOBS_TFIDF, job_tfidf)

print(f"Saving TF-IDF vectorizer to {OUT_TFIDF_VECT} ...")
joblib.dump(tfidf, OUT_TFIDF_VECT)

print("All done. You now have:")
print(" -", OUT_RESUMES_TFIDF)
print(" -", OUT_JOBS_TFIDF)
print(" -", OUT_TFIDF_VECT)

