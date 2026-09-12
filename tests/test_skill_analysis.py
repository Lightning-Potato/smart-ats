from smart_ats.skill_analysis import analyze_skill_match


def test_analyze_skill_match():
    job_description = """
    We are looking for a software engineer with
    experience in Python, Docker, AWS and PostgreSQL.
    """

    resume_text = """
    Software engineer experienced in Python,
    Docker and PostgreSQL.
    """

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    assert "python" in result["job_skills"]
    assert "docker" in result["job_skills"]
    assert "aws" in result["job_skills"]
    assert "postgresql" in result["job_skills"]

    assert "python" in result["matched_skills"]
    assert "docker" in result["matched_skills"]
    assert "postgresql" in result["matched_skills"]

    assert "aws" in result["missing_skills"]

    assert result["skill_match_score"] == 75.0


def test_analyze_skill_match_with_full_match():
    job_description = """
    Required skills: Python, Docker and AWS.
    """

    resume_text = """
    Experienced with Python, Docker and AWS.
    """

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    assert result["missing_skills"] == []

    assert set(result["matched_skills"]) == {
        "python",
        "docker",
        "aws"
    }

    assert result["skill_match_score"] == 100.0


def test_analyze_skill_match_with_no_match():
    job_description = """
    Required skills: Python, Docker and AWS.
    """

    resume_text = """
    Experienced with Java and MySQL.
    """

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    assert result["matched_skills"] == []

    assert set(result["missing_skills"]) == {
        "python",
        "docker",
        "aws"
    }

    assert result["skill_match_score"] == 0.0


def test_analyze_skill_match_with_aliases():
    job_description = """
    Experience with Amazon Web Services and PostgreSQL
    is required.
    """

    resume_text = """
    Worked with AWS and Postgres in production systems.
    """

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    assert set(result["matched_skills"]) == {
        "aws",
        "postgresql"
    }

    assert result["missing_skills"] == []

    assert result["skill_match_score"] == 100.0


def test_matched_skill_details_include_evidence_sources():
    job_description = """
Required skills:
Python, AWS, PostgreSQL
"""

    resume_text = """
SKILLS
Python
AWS

WORK EXPERIENCE
Software Engineer
Built backend services using Python and PostgreSQL.
"""

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    details = {
        item["skill"]: item
        for item in result["matched_skill_details"]
    }

    assert details["python"]["sources"] == {
        "skills",
        "experience"
    }

    assert details["aws"]["sources"] == {
        "skills"
    }

    assert details["postgresql"]["sources"] == {
        "experience"
    }


def test_matched_skill_details_preserve_alias_evidence():
    job_description = """
Experience with Amazon Web Services is required.
"""

    resume_text = """
TECHNICAL SKILLS
AWS

PROFESSIONAL EXPERIENCE
Deployed production services using Amazon Web Services.
"""

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    details = {
        item["skill"]: item
        for item in result["matched_skill_details"]
    }

    assert "aws" in details

    assert details["aws"]["sources"] == {
        "skills",
        "experience"
    }


def test_matched_skill_details_handle_unstructured_resume():
    job_description = """
Python and Docker experience required.
"""

    resume_text = """
Software Engineer

Built backend systems using Python and Docker.
"""

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    details = {
        item["skill"]: item
        for item in result["matched_skill_details"]
    }

    assert details["python"]["detected"] is True
    assert details["python"]["sources"] == set()

    assert details["docker"]["detected"] is True
    assert details["docker"]["sources"] == set()


def test_skill_evidence_does_not_change_match_score():
    job_description = """
Required skills:
Python, AWS, Docker, PostgreSQL
"""

    resume_text = """
SKILLS
Python
AWS

WORK EXPERIENCE
Used Python and PostgreSQL.
"""

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    assert result["skill_match_score"] == 75.0


def test_matched_skill_details_include_project_sources():
    job_description = """
Required skills:
Python, Docker
"""

    resume_text = """
SKILLS
Python

PROJECTS
Smart ATS
Built using Python and Docker.
"""

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    details = {
        item["skill"]: item
        for item in result["matched_skill_details"]
    }

    assert details["python"]["sources"] == {
        "skills",
        "projects"
    }

    assert details["docker"]["sources"] == {
        "projects"
    }


def test_matched_skill_details_use_source_based_contract():
    job_description = """
Required skill: Python
"""

    resume_text = """
SKILLS
Python
"""

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    detail = result["matched_skill_details"][0]

    assert "sources" in detail
    assert "declared" not in detail
    assert "demonstrated" not in detail