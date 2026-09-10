import streamlit as st
from utility import extract_text_from_pdf
from llm_client import get_llm_response

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
        resume_text = extract_text_from_pdf(resume_file)

        if resume_text:
            with st.spinner("Our AI is analyzing your inputs..."):
                input_prompt = f"""
                You are an experienced Applicant Tracking System (ATS) analyst.

                Your task is to provide a first impression of the alignment
                between a resume and a job description.

                Job Description:
                {job_description}

                Resume:
                {resume_text}

                Based on the above, provide a one-sentence summary of the
                resume's relevance to the job.
                """

                response = get_llm_response(input_prompt)

            st.subheader("AI's First Impression:")
            st.write(response)

        else:
            st.error("There was an error reading the PDF file.")

    else:
        st.warning(
            "Please provide both a job description and a resume."
        )