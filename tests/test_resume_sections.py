from smart_ats.resume_sections import parse_resume_sections


def test_parse_basic_resume_sections():
    resume = """
SKILLS
Python
Docker

EXPERIENCE
Software Engineer
Jan 2023 - Present

EDUCATION
University of Aberdeen
Sep 2024 - Jun 2026
"""

    sections = parse_resume_sections(resume)

    assert "skills" in sections
    assert "experience" in sections
    assert "education" in sections

    assert "Python" in sections["skills"]
    assert "Software Engineer" in sections["experience"]
    assert "University of Aberdeen" in sections["education"]


def test_parse_section_heading_aliases():
    resume = """
TECHNICAL SKILLS
Python
AWS

PROFESSIONAL EXPERIENCE
Backend Developer
Jan 2022 - Dec 2023

ACADEMIC BACKGROUND
Bachelor of Computing
"""

    sections = parse_resume_sections(resume)

    assert "skills" in sections
    assert "experience" in sections
    assert "education" in sections


def test_section_headings_are_case_insensitive():
    resume = """
Technical Skills:
Python

Work Experience:
Software Engineer

Education:
Bachelor of Computing
"""

    sections = parse_resume_sections(resume)

    assert "skills" in sections
    assert "experience" in sections
    assert "education" in sections


def test_education_content_is_separate_from_experience():
    resume = """
WORK EXPERIENCE
Software Engineer
Jan 2023 - Dec 2023

EDUCATION
University
Jan 2020 - Dec 2022
"""

    sections = parse_resume_sections(resume)

    assert "Jan 2023 - Dec 2023" in sections["experience"]

    assert "Jan 2020 - Dec 2022" not in sections["experience"]

    assert "Jan 2020 - Dec 2022" in sections["education"]


def test_resume_without_recognized_sections():
    resume = """
John Doe
Software Engineer
Python, Docker, AWS
"""

    sections = parse_resume_sections(resume)

    assert sections == {}