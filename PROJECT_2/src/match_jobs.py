import os
import pandas as pd
import scipy.sparse
from sklearn.metrics.pairwise import cosine_similarity

# Paths
DATA_FOLDER = r"C:\Users\PROJECT_2\DATA"
RESUMES_CSV = os.path.join(DATA_FOLDER, "resumes_cleaned.csv")
JOBS_CSV = os.path.join(DATA_FOLDER, "postings_cleaned.csv")
RESUME_TFIDF = os.path.join(DATA_FOLDER, "resumes_tfidf.npz")
JOB_TFIDF = os.path.join(DATA_FOLDER, "jobs_tfidf.npz")
OUTPUT_MATCHES = os.path.join(DATA_FOLDER, "resume_job_matches.csv")

print("Loading data...")
resumes_df = pd.read_csv(RESUMES_CSV)
jobs_df = pd.read_csv(JOBS_CSV)
resume_tfidf = scipy.sparse.load_npz(RESUME_TFIDF)
job_tfidf = scipy.sparse.load_npz(JOB_TFIDF)

print("Computing cosine similarity (this may take a few minutes)...")
similarity_matrix = cosine_similarity(resume_tfidf, job_tfidf)

print("Finding top 3 job matches for each resume...")
top_k = 3
matches = []

for i, resume_id in enumerate(resumes_df['ID']):
    top_indices = similarity_matrix[i].argsort()[-top_k:][::-1]
    for rank, idx in enumerate(top_indices, start=1):
        matches.append({
            "Resume_ID": resume_id,
            "Job_ID": jobs_df.iloc[idx]['job_id'],
            "Job_Title": jobs_df.iloc[idx]['title'],
            "Company": jobs_df.iloc[idx]['company_name'],
            "Similarity": round(similarity_matrix[i, idx], 4),
            "Rank": rank
        })

matches_df = pd.DataFrame(matches)
matches_df.to_csv(OUTPUT_MATCHES, index=False, encoding='utf-8')

print(f"✅ Matching complete. Results saved to: {OUTPUT_MATCHES}")
print("Each resume now has its top 3 most similar job postings.")

