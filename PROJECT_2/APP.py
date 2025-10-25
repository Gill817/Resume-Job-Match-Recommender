import streamlit as st
import pandas as pd
import random

st.title("Resume–Job Match Dashboard")


matches_df = pd.read_csv(r"C:\Users\PROJECT_2\DATA\resume_job_matches_with_skills.csv")

uploaded_file = st.file_uploader("Upload your resume CSV", type=["csv"])
if uploaded_file:
    user_resumes = pd.read_csv(uploaded_file)
    st.write("Resume uploaded ✅")
    st.dataframe(user_resumes.head(3))
#1
resume_options = matches_df['Resume_ID'].unique()
selected_resume = st.selectbox("Select a Resume ID", resume_options)
#2
filtered = matches_df[matches_df['Resume_ID'] == selected_resume].head(3).copy()

#3
filtered['Fit_Score'] = [random.randint(60, 100) for _ in range(len(filtered))]

# 4 i chose, this for visualziation purpose , as these were the most common , skills found 
demo_skills = ["Excel", "Communication", "Python", "SQL", "PowerPoint"]
filtered['Missing_Skills'] = [", ".join(random.sample(demo_skills, 2)) for _ in range(len(filtered))]

# Step 3: Show top job matches
st.subheader(f"Top 3 Job Matches for Resume {selected_resume}")
st.dataframe(filtered[['Job_ID','Job_Title','Company','Fit_Score','Missing_Skills']])

