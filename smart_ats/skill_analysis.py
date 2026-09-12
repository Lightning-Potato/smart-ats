from smart_ats.job_requirements import (
    extract_skill_requirements,
)
from smart_ats.matching_engine import (
    calculate_skill_match_score,
    match_skills,
)
from smart_ats.skill_evidence import analyze_skill_evidence
from smart_ats.skill_extractor import extract_skills


def resolve_job_skill_requirements(job_description):
    """
    Resolves required and preferred job skills.

    Uses structured requirement sections when available.
    Falls back to full job-description skill extraction when
    no recognized requirement sections are found.
    """

    classified = extract_skill_requirements(
        job_description
    )

    required_skills = classified["required_skills"]
    preferred_skills = classified["preferred_skills"]

    if required_skills or preferred_skills:
        return {
            "required_skills": required_skills,
            "preferred_skills": preferred_skills,
            "used_fallback": False,
        }

    return {
        "required_skills": extract_skills(
            job_description
        ),
        "preferred_skills": [],
        "used_fallback": True,
    }


def analyze_skill_match(job_description, resume_text):
    """
    Analyzes required and preferred job skills against
    skills detected in the resume.

    Required and preferred skills are matched separately.
    The skill match score is currently based only on
    required skills.

    Returns:
        dict: Requirement-aware skill analysis results.
    """

    requirements = resolve_job_skill_requirements(
        job_description
    )

    required_skills = requirements["required_skills"]
    preferred_skills = requirements["preferred_skills"]

    resume_skills = extract_skills(
        resume_text
    )

    required_match = match_skills(
        required_skills,
        resume_skills
    )

    preferred_match = match_skills(
        preferred_skills,
        resume_skills
    )

    if required_skills:
        skill_match_score = calculate_skill_match_score(
            required_match["matched_skills"],
            required_skills
        )
    else:
        skill_match_score = None

    all_matched_skills = list(
        dict.fromkeys(
            required_match["matched_skills"]
            + preferred_match["matched_skills"]
        )
    )

    skill_evidence = analyze_skill_evidence(
        resume_text
    )

    matched_skill_details = []

    for skill in all_matched_skills:
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
        "required_skills": required_skills,
        "preferred_skills": preferred_skills,

        "matched_required_skills":
            required_match["matched_skills"],

        "missing_required_skills":
            required_match["missing_skills"],

        "matched_preferred_skills":
            preferred_match["matched_skills"],

        "missing_preferred_skills":
            preferred_match["missing_skills"],

        "skill_match_score": skill_match_score,
        "matched_skill_details": matched_skill_details,

        "requirement_fallback_used":
            requirements["used_fallback"],
    }