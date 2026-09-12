import logging

import streamlit as st

from smart_ats.analysis_parser import parse_analysis_response
from smart_ats.experience_analysis import analyze_experience_match
from smart_ats.findings import build_deterministic_findings
from smart_ats.llm_client import get_llm_response
from smart_ats.logging_config import configure_logging
from smart_ats.prompts import build_structured_analysis_prompt
from smart_ats.scoring import calculate_overall_ats_score
from smart_ats.skill_analysis import analyze_skill_match
from smart_ats.ui_components import display_analysis_dashboard
from smart_ats.utility import extract_text_from_pdf

configure_logging()

logger = logging.getLogger(__name__)


st.set_page_config(
    page_title="Smart ATS",
    page_icon="🤖",
    layout="centered",
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
        placeholder="Paste the job description text here...",
    )

    st.header("2. Upload Your Resume")

    resume_file = st.file_uploader(
        "Upload your resume (PDF only)",
        type="pdf",
    )

    submitted = st.form_submit_button(
        "Analyze My Resume",
        type="primary",
    )


if submitted:
    if not job_description or not resume_file:
        logger.warning("Analysis submitted with incomplete input")

        st.warning("Please provide both a job description and a resume.")

        st.stop()

    logger.info("ATS analysis started")

    # -------------------------
    # PDF Extraction
    # -------------------------

    try:
        resume_text = extract_text_from_pdf(resume_file)

    except Exception:
        logger.exception("Resume PDF extraction failed")

        st.error(
            "The resume could not be processed. "
            "Please verify that the uploaded file "
            "is a valid PDF."
        )

        st.stop()

    if not resume_text:
        logger.warning("Resume text extraction returned no content")

        st.error("No readable text was found in the uploaded resume.")

        st.stop()

    logger.info("Resume text extracted successfully")

    # -------------------------
    # Deterministic Analysis
    # -------------------------

    try:
        skill_analysis = analyze_skill_match(
            job_description,
            resume_text,
        )

        experience_analysis = analyze_experience_match(
            job_description,
            resume_text,
        )

        findings = build_deterministic_findings(
            skill_analysis,
            experience_analysis,
        )

        logger.debug("Deterministic findings context built")

        overall_ats_score = calculate_overall_ats_score(
            skill_analysis["skill_match_score"],
            experience_analysis["experience_match_score"],
        )

    except Exception:
        logger.exception("Deterministic ATS analysis failed")

        st.error("The ATS analysis could not be completed. Please try again.")

        st.stop()

    logger.info("Deterministic ATS analysis completed")

    # -------------------------
    # AI Insight Generation
    # -------------------------

    analysis = None

    try:
        logger.info("Grounded AI insight generation started")

        with st.spinner("Generating grounded AI insights..."):
            input_prompt = build_structured_analysis_prompt(
                job_description,
                resume_text,
                findings,
            )

            response = get_llm_response(input_prompt)

        logger.info("Grounded AI insight generation completed")

    except Exception:
        logger.exception("Grounded AI insight generation failed")

    else:
        try:
            analysis = parse_analysis_response(response)

        except ValueError:
            logger.exception("Failed to parse AI analysis response")

    # -------------------------
    # Dashboard
    # -------------------------

    display_analysis_dashboard(
        analysis,
        skill_analysis,
        experience_analysis,
        overall_ats_score,
    )

    if analysis is None:
        logger.warning("ATS analysis completed without AI insights")
    else:
        logger.info("ATS analysis completed successfully")
