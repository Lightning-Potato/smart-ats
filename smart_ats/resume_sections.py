SECTION_ALIASES = {
    "experience": {
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "work history",
    },
    "education": {
        "education",
        "academic background",
        "academic history",
    },
    "skills": {
        "skills",
        "technical skills",
        "core skills",
        "core competencies",
    },
}

def build_section_lookup():
    """
    Builds a mapping from section heading aliases
    to canonical section names.
    """

    lookup = {}

    for canonical_name, aliases in SECTION_ALIASES.items():
        for alias in aliases:
            lookup[alias] = canonical_name

    return lookup

def normalize_heading(line):
    """
    Normalizes a potential resume section heading.
    """

    return line.strip().lower().rstrip(":")

def parse_resume_sections(resume_text):
    """
    Splits resume text into recognized canonical sections.

    Returns:
        dict: Recognized resume sections and their content.
    """

    section_lookup = build_section_lookup()

    sections = {}
    current_section = None
    current_lines = []

    for line in resume_text.splitlines():
        normalized_line = normalize_heading(line)

        if normalized_line in section_lookup:
            if current_section is not None:
                sections[current_section] = "\n".join(
                    current_lines
                ).strip()

            current_section = section_lookup[
                normalized_line
            ]
            current_lines = []

        elif current_section is not None:
            current_lines.append(line)

    if current_section is not None:
        sections[current_section] = "\n".join(
            current_lines
        ).strip()

    return sections