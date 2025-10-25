📄 Resume–Job Match Recommender



🌟 Overview



This project is an interactive system that matches candidate resumes with job postings based on textual similarity and skills analysis. It allows recruiters or candidates to quickly find the best job opportunities while highlighting skill gaps.



The project demonstrates data cleaning, NLP-based text processing, TF-IDF vectorization, and cosine similarity, wrapped in an easy-to-use Streamlit dashboard.



🎯 Objectives



* Clean and preprocess resumes and job postings for analysis 
* Automatically find the top job matches for a given resume 
* Highlight missing skills between candidate resumes and job requirements 
* Provide an intuitive interface to view results 
* Showcase a portfolio project that combines data science, NLP, and dashboarding 



✨ Features



* &nbsp;Resume Upload: Upload CSV of resumes and view top matched jobs
* &nbsp;Top Job Matches: See the top 3 job recommendations per resume
* Fit Score: Get a score (0–100) representing how well a resume matches a job
* Skills Gap Analysis: Identify missing skills for each recommended job
* &nbsp;Interactive Dashboard: Filter and view results in a clean Streamlit interface



⚙️ How It Works



Data Cleaning:



1. Remove HTML tags, punctuation, and special characters
2. Convert text to lowercase and lemmatize
3. Remove stopwords for cleaner analysis



Vectorization:



1. Convert text from resumes and job postings into TF-IDF vectors





Matching:



1. Compute cosine similarity between resume vectors and job vectors
2. Identify top job matches based on similarity



Skills Analysis:



1. Compare candidate skills with job requirements
2. Highlight missing skills and compute a Fit Score





📁 Project Structure



PROJECT\_2/

│

├─ DATA/

│   ├─ resumes\_cleaned.csv

│   ├─ postings\_cleaned.csv

│   ├─ resume\_job\_matches.csv

│   ├─ tfidf\_vectorizer.pkl

│

├─ src/

│   ├─ job\_preprocessing.py

│   ├─ clean\_text.py

│

├─ app.py        # Streamlit dashboard



🛠️ Tech Stack

Python (pandas, scikit-learn, BeautifulSoup, spacy)
NLP (TF-IDF vectorization, text cleaning, cosine similarity)
Streamlit (interactive dashboard)



🚀 Quick Start

Install dependencies

pip install pandas scikit-learn spacy beautifulsoup4 streamlit




Run the dashboard

streamlit run APP.py


Here is the preview:

<img width="1003" height="637" alt="Screenshot (130)" src="https://github.com/user-attachments/assets/77e76ed9-f0b1-4ed8-9a7d-0715029743d3" />





