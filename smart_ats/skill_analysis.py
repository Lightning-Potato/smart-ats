from smart_ats.matching_engine import (
    calculate_skill_match_score,
    match_skills,
)
from smart_ats.skill_extractor import extract_skills
from smart_ats.skill_evidence import analyze_skill_evidence



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

    skill_match_score = calculate_skill_match_score(
        match_result["matched_skills"],
        job_skills
    )

    skill_evidence = analyze_skill_evidence(
        resume_text
    )

    matched_skill_details = []

    for skill in match_result["matched_skills"]:
        evidence = skill_evidence.get(
            skill,
            {
                "detected": True,
                "sources": set(),
            }
        )

        matched_skill_details.append({
            "skill": skill,
            "detected": evidence["detected"],
            "sources": evidence["sources"],
        })

    return {
        "job_skills": job_skills,
        "resume_skills": resume_skills,
        "matched_skills": match_result["matched_skills"],
        "missing_skills": match_result["missing_skills"],
        "skill_match_score": skill_match_score,
        "matched_skill_details": matched_skill_details
    }