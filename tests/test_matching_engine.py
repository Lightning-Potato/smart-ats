from smart_ats.matching_engine import (
    match_skills,
    normalize_skill,
)


def test_normalize_skill():
    assert normalize_skill("Python") == "python"
    assert normalize_skill("  PYTHON  ") == "python"
    assert normalize_skill("JavaScript") == "javascript"

def test_match_skills():
    job_skills = [
        "Python",
        "Docker",
        "AWS"
    ]

    resume_skills = [
        "Python",
        "Docker"
    ]

    result = match_skills(
        job_skills,
        resume_skills
    )

    assert result["matched_skills"] == [
        "Python",
        "Docker"
    ]

    assert result["missing_skills"] == [
        "AWS"
    ]

def test_match_skills_is_case_insensitive():
    job_skills = [
        "Python",
        "Docker"
    ]

    resume_skills = [
        "PYTHON",
        "docker"
    ]

    result = match_skills(
        job_skills,
        resume_skills
    )

    assert result["matched_skills"] == [
        "Python",
        "Docker"
    ]

    assert result["missing_skills"] == []

def test_match_skills_with_empty_resume():
    job_skills = [
        "Python",
        "AWS"
    ]

    result = match_skills(
        job_skills,
        []
    )

    assert result["matched_skills"] == []

    assert result["missing_skills"] == [
        "Python",
        "AWS"
    ]

def test_normalize_known_skill_aliases():
    assert normalize_skill("AWS") == "aws"

    assert (
        normalize_skill("Amazon Web Services")
        == "aws"
    )

    assert normalize_skill("Postgres") == "postgresql"

    assert normalize_skill("PostgreSQL") == "postgresql"

    assert normalize_skill("JS") == "javascript"

    assert normalize_skill("JavaScript") == "javascript"

def test_match_skills_with_aliases():
    job_skills = [
        "Amazon Web Services",
        "PostgreSQL",
        "JavaScript"
    ]

    resume_skills = [
        "AWS",
        "Postgres",
        "JS"
    ]

    result = match_skills(
        job_skills,
        resume_skills
    )

    assert result["matched_skills"] == [
        "Amazon Web Services",
        "PostgreSQL",
        "JavaScript"
    ]

    assert result["missing_skills"] == []

def test_normalize_unknown_skill():
    assert normalize_skill("PyTorch") == "pytorch"