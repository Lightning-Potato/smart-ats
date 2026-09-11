import streamlit as st
from utility import extract_text_from_pdf
from llm_client import get_llm_response
from prompts import build_structured_analysis_prompt
from analysis_parser import parse_analysis_response

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
            with st.spinner(
                "Our AI is analyzing your inputs... This may take a moment."
            ):
                input_prompt = build_structured_analysis_prompt(
                    job_description,
                    resume_text
                )

                response = get_llm_response(input_prompt)

                try:
                    analysis = parse_analysis_response(response)

                    st.subheader("Structured ATS Analysis")

                    st.write("Overall Score:", analysis["overall_score"])
                    st.write("Summary:", analysis["summary"])

                    st.write("Matched Skills:", analysis["matched_skills"])
                    st.write("Missing Skills:", analysis["missing_skills"])

                except ValueError as e:
                    st.error(str(e))

        else:
            st.error("There was an error reading the PDF file.")

    else:
        st.warning(
            "Please provide both a job description and a resume."
        )