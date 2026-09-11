import streamlit as st

from smart_ats.utility import extract_text_from_pdf
from smart_ats.llm_client import get_llm_response
from smart_ats.prompts import build_structured_analysis_prompt
from smart_ats.analysis_parser import parse_analysis_response
from smart_ats.ui_components import display_analysis_dashboard
from smart_ats.skill_analysis import analyze_skill_match
from smart_ats.experience_analysis import analyze_experience_match

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
            skill_analysis = analyze_skill_match(
                job_description,
                resume_text
            )

            experience_analysis = analyze_experience_match(
                job_description,
                resume_text
            )

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

                display_analysis_dashboard(
                    analysis,
                    skill_analysis,
                    experience_analysis
                )

            except ValueError as e:
                st.error(str(e))

        else:
            st.error("There was an error reading the PDF file.")

    else:
        st.warning(
            "Please provide both a job description and a resume."
        )