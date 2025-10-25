import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy.sparse

# Load cleaned resumes
df = pd.read_csv("DATA/resumes_cleaned.csv")

# TF-IDF vectorization
tfidf = TfidfVectorizer(max_features=5000)
X_resumes = tfidf.fit_transform(df['Resume_clean'])

# Save TF-IDF matrix
scipy.sparse.save_npz("DATA/Resume/resumes_tfidf.npz", X_resumes)

print("TF-IDF vectorization done. Shape:", X_resumes.shape)
