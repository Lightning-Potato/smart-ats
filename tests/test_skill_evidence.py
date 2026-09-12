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
    assert evidence["python"]["declared"] is True
    assert evidence["python"]["demonstrated"] is True


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
    assert evidence["aws"]["declared"] is True
    assert evidence["aws"]["demonstrated"] is False


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
    assert evidence["postgresql"]["declared"] is False
    assert evidence["postgresql"]["demonstrated"] is True


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
    assert evidence["aws"]["declared"] is True
    assert evidence["aws"]["demonstrated"] is True


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
    assert evidence["python"]["declared"] is False
    assert evidence["python"]["demonstrated"] is False

    assert evidence["docker"]["detected"] is True
    assert evidence["docker"]["declared"] is False
    assert evidence["docker"]["demonstrated"] is False


def test_skill_can_have_project_evidence():
    resume = """
SKILLS
Python

PERSONAL PROJECTS
Smart ATS
Built using Python and Docker.
"""

    evidence = analyze_skill_evidence(resume)

    assert "projects" in evidence["python"]["sources"]
    assert "projects" in evidence["docker"]["sources"]

    assert evidence["python"]["declared"] is True
    assert evidence["docker"]["declared"] is False


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

    assert evidence["docker"]["sources"] == {
        "projects"
    }

    assert evidence["docker"]["detected"] is True
    assert evidence["docker"]["declared"] is False
    assert evidence["docker"]["demonstrated"] is False


def test_source_based_evidence_preserves_legacy_flags():
    resume = """
SKILLS
AWS

WORK EXPERIENCE
Cloud Engineer
Deployed systems using AWS.
"""

    evidence = analyze_skill_evidence(resume)

    assert evidence["aws"]["sources"] == {
        "skills",
        "experience"
    }

    assert evidence["aws"]["declared"] is True
    assert evidence["aws"]["demonstrated"] is True


