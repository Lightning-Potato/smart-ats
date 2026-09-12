from smart_ats.job_requirements import (
    extract_skill_requirements,
    parse_requirement_sections,
)


def test_parse_required_and_preferred_sections():
    job_description = """
REQUIRED SKILLS
Python
Docker

PREFERRED SKILLS
AWS
Kubernetes
"""

    sections = parse_requirement_sections(
        job_description
    )

    assert "required" in sections
    assert "preferred" in sections

    assert "Python" in sections["required"]
    assert "Docker" in sections["required"]

    assert "AWS" in sections["preferred"]
    assert "Kubernetes" in sections["preferred"]


def test_preferred_skills_do_not_leak_into_required_section():
    job_description = """
REQUIRED SKILLS
Python
Docker

PREFERRED SKILLS
AWS
Kubernetes
"""

    sections = parse_requirement_sections(
        job_description
    )

    assert "AWS" not in sections["required"]
    assert "Kubernetes" not in sections["required"]

    assert "Python" not in sections["preferred"]
    assert "Docker" not in sections["preferred"]


def test_requirement_section_aliases():
    job_description = """
MUST HAVE
Python
PostgreSQL

NICE TO HAVE
AWS
Docker
"""

    sections = parse_requirement_sections(
        job_description
    )

    assert "Python" in sections["required"]
    assert "PostgreSQL" in sections["required"]

    assert "AWS" in sections["preferred"]
    assert "Docker" in sections["preferred"]


def test_requirement_headings_are_case_insensitive():
    job_description = """
Required Skills:
Python
Docker

Preferred Qualifications:
AWS
"""

    sections = parse_requirement_sections(
        job_description
    )

    assert "Python" in sections["required"]
    assert "AWS" in sections["preferred"]


def test_extract_required_and_preferred_skills():
    job_description = """
REQUIRED SKILLS
Python
Docker
PostgreSQL

PREFERRED SKILLS
Amazon Web Services
Kubernetes
"""

    result = extract_skill_requirements(
        job_description
    )

    assert set(result["required_skills"]) == {
        "python",
        "docker",
        "postgresql",
    }

    assert set(result["preferred_skills"]) == {
        "aws",
        "kubernetes",
    }


def test_job_description_with_only_required_skills():
    job_description = """
REQUIREMENTS
Python
Docker
"""

    result = extract_skill_requirements(
        job_description
    )

    assert set(result["required_skills"]) == {
        "python",
        "docker",
    }

    assert result["preferred_skills"] == []


def test_job_description_with_only_preferred_skills():
    job_description = """
NICE TO HAVE
AWS
Docker
"""

    result = extract_skill_requirements(
        job_description
    )

    assert result["required_skills"] == []

    assert set(result["preferred_skills"]) == {
        "aws",
        "docker",
    }


def test_unstructured_job_description_has_no_classified_requirements():
    job_description = """
We are looking for a software engineer with
experience in Python, Docker and AWS.
"""

    result = extract_skill_requirements(
        job_description
    )

    assert result["required_skills"] == []
    assert result["preferred_skills"] == []