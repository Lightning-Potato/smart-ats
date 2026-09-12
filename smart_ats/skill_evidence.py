from smart_ats.resume_sections import parse_resume_sections
from smart_ats.skill_extractor import extract_skills


def analyze_skill_evidence(resume_text):
    """
    Analyzes where technical skills are evidenced within a resume.

    A skill may be:
    - detected anywhere in the resume
    - declared in a recognized skills section
    - demonstrated in a recognized experience section

    Returns:
        dict: Canonical skill names mapped to their evidence.
    """

    sections = parse_resume_sections(resume_text)

    declared_skills = set(
        extract_skills(
            sections.get("skills", "")
        )
    )

    demonstrated_skills = set(
        extract_skills(
            sections.get("experience", "")
        )
    )

    all_resume_skills = set(
        extract_skills(resume_text)
    )

    all_skills = (
        declared_skills
        | demonstrated_skills
        | all_resume_skills
    )

    evidence = {}

    for skill in all_skills:
        evidence[skill] = {
            "detected": True,
            "declared": skill in declared_skills,
            "demonstrated": skill in demonstrated_skills,
        }

    return evidence