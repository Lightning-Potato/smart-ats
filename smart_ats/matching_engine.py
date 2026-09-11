from smart_ats.skill_aliases import SKILL_ALIASES

def normalize_skill(skill):
    """
    Normalizes a skill name and resolves known aliases.
    """

    normalized = skill.strip().lower()

    return SKILL_ALIASES.get(
        normalized,
        normalized
    )

def match_skills(job_skills, resume_skills):
    """
    Compares required job skills against resume skills.

    Returns:
        dict: Matched and missing skills.
    """

    normalized_resume_skills = {
        normalize_skill(skill)
        for skill in resume_skills
    }

    matched_skills = []
    missing_skills = []

    for job_skill in job_skills:
        normalized_job_skill = normalize_skill(job_skill)

        if normalized_job_skill in normalized_resume_skills:
            matched_skills.append(job_skill)
        else:
            missing_skills.append(job_skill)

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }