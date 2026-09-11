from smart_ats.matching_engine import match_skills
from smart_ats.skill_extractor import extract_skills


def analyze_skill_match(job_description, resume_text):
    """
    Extracts skills from a job description and resume,
    then compares them using the matching engine.

    Returns:
        dict: Extracted, matched, and missing skills.
    """

    job_skills = extract_skills(job_description)
    resume_skills = extract_skills(resume_text)

    match_result = match_skills(
        job_skills,
        resume_skills
    )

    return {
        "job_skills": job_skills,
        "resume_skills": resume_skills,
        "matched_skills": match_result["matched_skills"],
        "missing_skills": match_result["missing_skills"]
    }