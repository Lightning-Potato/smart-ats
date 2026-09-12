from smart_ats.skill_evidence import analyze_skill_evidence


def test_skill_can_be_declared_and_demonstrated():
    resume = """
SKILLS
Python
AWS

WORK EXPERIENCE
Software Engineer
Built backend services using Python.
"""

    evidence = analyze_skill_evidence(resume)

    assert evidence["python"]["detected"] is True
    assert evidence["python"]["sources"] == {
        "skills",
        "experience",
    }


def test_skill_can_be_declared_only():
    resume = """
SKILLS
Python
AWS

WORK EXPERIENCE
Software Engineer
Built backend services using Python.
"""

    evidence = analyze_skill_evidence(resume)

    assert evidence["aws"]["detected"] is True
    assert evidence["aws"]["sources"] == {
        "skills",
    }


def test_skill_can_be_demonstrated_only():
    resume = """
SKILLS
Python

WORK EXPERIENCE
Software Engineer
Built services using Python and PostgreSQL.
"""

    evidence = analyze_skill_evidence(resume)

    assert evidence["postgresql"]["detected"] is True
    assert evidence["postgresql"]["sources"] == {
        "experience",
    }


def test_skill_evidence_uses_canonical_aliases():
    resume = """
TECHNICAL SKILLS
Amazon Web Services

PROFESSIONAL EXPERIENCE
Deployed services using AWS.
"""

    evidence = analyze_skill_evidence(resume)

    assert "aws" in evidence
    assert evidence["aws"]["detected"] is True
    assert evidence["aws"]["sources"] == {
        "skills",
        "experience",
    }


def test_unstructured_resume_preserves_detected_skills():
    resume = """
John Doe
Software Engineer

Built backend systems using Python and Docker.
"""

    evidence = analyze_skill_evidence(resume)

    assert "python" in evidence
    assert "docker" in evidence

    assert evidence["python"]["detected"] is True
    assert evidence["python"]["sources"] == set()

    assert evidence["docker"]["detected"] is True
    assert evidence["docker"]["sources"] == set()


def test_skill_can_have_project_evidence():
    resume = """
SKILLS
Python

PERSONAL PROJECTS
Smart ATS
Built using Python and Docker.
"""

    evidence = analyze_skill_evidence(resume)

    assert evidence["python"]["sources"] == {
        "skills",
        "projects",
    }

    assert evidence["docker"]["sources"] == {
        "projects",
    }


def test_skill_can_have_multiple_evidence_sources():
    resume = """
TECHNICAL SKILLS
Python

WORK EXPERIENCE
Software Engineer
Built APIs using Python.

PROJECTS
Machine Learning Platform
Built with Python and PyTorch.
"""

    evidence = analyze_skill_evidence(resume)

    assert evidence["python"]["sources"] == {
        "skills",
        "experience",
        "projects",
    }


def test_skill_can_be_detected_only_in_projects():
    resume = """
SKILLS
Python

PROJECTS
Containerized Application
Deployed using Docker and Kubernetes.
"""

    evidence = analyze_skill_evidence(resume)

    assert evidence["docker"]["detected"] is True
    assert evidence["docker"]["sources"] == {
        "projects",
    }


def test_skill_evidence_uses_source_based_contract():
    resume = """
SKILLS
Python

WORK EXPERIENCE
Software Engineer
Used Python.
"""

    evidence = analyze_skill_evidence(resume)

    python_evidence = evidence["python"]

    assert "detected" in python_evidence
    assert "sources" in python_evidence

    assert "declared" not in python_evidence
    assert "demonstrated" not in python_evidence