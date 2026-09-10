import streamlit as st

st.set_page_config(
    page_title="Smart ATS",
    page_icon="🤖",
    layout="centered"
)

st.title("Smart Applicant Tracking System 🤖")

st.write(
    "Optimize your resume by analyzing it against "
    "a job description with the power of AI."
)

st.divider()

with st.form("ats_form"):
    st.header("1. Paste the Job Description")

    job_description = st.text_area(
        "Job Description",
        height=250,
        placeholder="Paste the job description text here..."
    )

    st.header("2. Upload Your Resume")

    resume_file = st.file_uploader(
        "Upload your resume (PDF only)",
        type="pdf"
    )

    submitted = st.form_submit_button(
        "Analyze My Resume",
        type="primary"
    )

if submitted:
    if job_description and resume_file:
        st.success("Inputs received! We're ready to start processing.")
    else:
        st.warning(
            "Please make sure you have provided both "
            "a job description and a resume file."
        )