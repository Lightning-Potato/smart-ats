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