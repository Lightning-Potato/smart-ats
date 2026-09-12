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

    project_skills = set(
    extract_skills(
        sections.get("projects", "")
    )
)

    all_skills = (
        declared_skills
        | demonstrated_skills
        | project_skills
        | all_resume_skills
    )

    evidence = {}

    for skill in all_skills:
        sources = set()

        if skill in declared_skills:
            sources.add("skills")

        if skill in demonstrated_skills:
            sources.add("experience")

        if skill in project_skills:
            sources.add("projects")

        evidence[skill] = {
            "detected": True,
            "sources": sources,
        }

    return evidence