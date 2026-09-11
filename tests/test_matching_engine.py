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