from smart_ats.skill_extractor import extract_skills

REQUIREMENT_SECTION_ALIASES = {
    "required": {
        "required skills",
        "requirements",
        "must have",
        "must-have",
        "minimum qualifications",
        "required qualifications",
    },
    "preferred": {
        "preferred skills",
        "preferred qualifications",
        "nice to have",
        "nice-to-have",
        "bonus skills",
    },
}


def build_requirement_section_lookup():
    """
    Builds a mapping from job requirement heading aliases
    to canonical requirement categories.
    """

    lookup = {}

    for category, aliases in REQUIREMENT_SECTION_ALIASES.items():
        for alias in aliases:
            lookup[alias] = category

    return lookup


def normalize_requirement_heading(line):
    """
    Normalizes a potential job requirement heading.
    """

    return line.strip().lower().rstrip(":")


def parse_requirement_sections(job_description):
    """
    Splits a job description into recognized required
    and preferred requirement sections.

    Returns:
        dict: Recognized requirement categories and text.
    """

    section_lookup = build_requirement_section_lookup()

    sections = {}
    current_section = None
    current_lines = []

    for line in job_description.splitlines():
        normalized_line = normalize_requirement_heading(line)

        if normalized_line in section_lookup:
            if current_section is not None:
                sections[current_section] = "\n".join(current_lines).strip()

            current_section = section_lookup[normalized_line]
            current_lines = []

        elif current_section is not None:
            current_lines.append(line)

    if current_section is not None:
        sections[current_section] = "\n".join(current_lines).strip()

    return sections


def extract_skill_requirements(job_description):
    """
    Extracts required and preferred technical skills
    from recognized job-description sections.

    Returns:
        dict: Required and preferred canonical skills.
    """

    sections = parse_requirement_sections(job_description)

    required_skills = extract_skills(sections.get("required", ""))

    preferred_skills = extract_skills(sections.get("preferred", ""))

    return {
        "required_skills": required_skills,
        "preferred_skills": preferred_skills,
    }
