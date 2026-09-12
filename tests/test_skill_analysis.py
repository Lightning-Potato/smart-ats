from smart_ats.skill_analysis import (
    analyze_skill_match,
    resolve_job_skill_requirements,
)


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

    assert result["requirement_fallback_used"] is True

    assert set(result["required_skills"]) == {
        "python",
        "docker",
        "aws",
        "postgresql"
    }

    assert result["preferred_skills"] == []

    assert set(result["matched_required_skills"]) == {
        "python",
        "docker",
        "postgresql"
    }

    assert set(result["missing_required_skills"]) == {
        "aws"
    }

    assert result["matched_preferred_skills"] == []
    assert result["missing_preferred_skills"] == []

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

    assert result["missing_required_skills"] == []

    assert set(result["matched_required_skills"]) == {
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

    assert result["matched_required_skills"] == []

    assert set(result["missing_required_skills"]) == {
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

    assert set(result["matched_required_skills"]) == {
        "aws",
        "postgresql"
    }

    assert result["missing_required_skills"] == []

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


def test_resolve_structured_job_skill_requirements():
    job_description = """
REQUIRED SKILLS
Python
Docker

PREFERRED SKILLS
AWS
Kubernetes
"""

    result = resolve_job_skill_requirements(
        job_description
    )

    assert set(result["required_skills"]) == {
        "python",
        "docker"
    }

    assert set(result["preferred_skills"]) == {
        "aws",
        "kubernetes"
    }

    assert result["used_fallback"] is False


def test_resolve_unstructured_job_skills_with_fallback():
    job_description = """
We are looking for an engineer with experience
in Python, Docker and AWS.
"""

    result = resolve_job_skill_requirements(
        job_description
    )

    assert set(result["required_skills"]) == {
        "python",
        "docker",
        "aws"
    }

    assert result["preferred_skills"] == []
    assert result["used_fallback"] is True


def test_preferred_skills_do_not_reduce_required_skill_score():
    job_description = """
REQUIRED SKILLS
Python
Docker

PREFERRED SKILLS
AWS
Kubernetes
"""

    resume_text = """
SKILLS
Python
Docker
"""

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    assert set(result["matched_required_skills"]) == {
        "python",
        "docker"
    }

    assert result["missing_required_skills"] == []

    assert result["matched_preferred_skills"] == []

    assert set(
        result["missing_preferred_skills"]
    ) == {
        "aws",
        "kubernetes"
    }

    assert result["skill_match_score"] == 100.0


def test_missing_required_skill_reduces_skill_score():
    job_description = """
REQUIRED SKILLS
Python
Docker

PREFERRED SKILLS
AWS
"""

    resume_text = """
SKILLS
Python
AWS
"""

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    assert set(result["matched_required_skills"]) == {
        "python"
    }

    assert set(result["missing_required_skills"]) == {
        "docker"
    }

    assert set(result["matched_preferred_skills"]) == {
        "aws"
    }

    assert result["skill_match_score"] == 50.0


def test_unstructured_job_description_preserves_legacy_score():
    job_description = """
We need experience with Python, Docker,
AWS and PostgreSQL.
"""

    resume_text = """
Experienced with Python, Docker and PostgreSQL.
"""

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    assert result["requirement_fallback_used"] is True
    assert result["skill_match_score"] == 75.0


def test_skill_score_is_none_when_no_required_skills_exist():
    job_description = """
PREFERRED SKILLS
AWS
Docker
"""

    resume_text = """
SKILLS
AWS
"""

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    assert result["required_skills"] == []
    assert set(result["preferred_skills"]) == {
        "aws",
        "docker"
    }

    assert result["skill_match_score"] is None


def test_skill_score_is_zero_when_required_skills_are_missing():
    job_description = """
REQUIRED SKILLS
Python
Docker
"""

    resume_text = """
SKILLS
Java
"""

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    assert result["skill_match_score"] == 0.0


def test_skill_analysis_excludes_legacy_aggregate_fields():
    job_description = """
REQUIRED SKILLS
Python

PREFERRED SKILLS
AWS
"""

    resume_text = """
SKILLS
Python
"""

    result = analyze_skill_match(
        job_description,
        resume_text
    )

    assert "job_skills" not in result
    assert "matched_skills" not in result
    assert "missing_skills" not in result
    assert "resume_skills" not in result