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
            with st.spinner(
                "Our AI is analyzing your inputs... This may take a moment."
            ):
                input_prompt = f"""
                **Role:** You are a highly skilled and experienced Applicant
                Tracking System (ATS) analyst with deep expertise in the tech
                industry and Human Resources.

                **Task:** Your goal is to analyze the provided resume against
                the given job description and determine their compatibility.

                **Instructions:**
                1. First, carefully review the entire job description to
                understand the key requirements, skills, and qualifications.

                2. Next, thoroughly review the entire resume to identify the
                candidate's skills, experience, and qualifications.

                3. Provide a short, one-paragraph analysis of how well the
                resume aligns with the job description. Do not make up any
                information. Base your analysis strictly on the text provided.

                **Documents for Analysis:**

                **Job Description:**
                ---
                {job_description}
                ---

                **Resume:**
                ---
                {resume_text}
                ---
                """

                response = get_llm_response(input_prompt)

            st.subheader("AI Analysis:")
            st.markdown(response)

        else:
            st.error("There was an error reading the PDF file.")

    else:
        st.warning(
            "Please provide both a job description and a resume."
        )