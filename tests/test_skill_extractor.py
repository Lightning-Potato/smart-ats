from smart_ats.skill_extractor import extract_skills


def test_extract_basic_skills():
    text = (
        "We are looking for an engineer with experience "
        "in Python, Docker, and AWS."
    )

    result = extract_skills(text)

    assert "python" in result
    assert "docker" in result
    assert "aws" in result

def test_extract_skills_is_case_insensitive():
    text = "Experience with PYTHON, docker and Aws is required."

    result = extract_skills(text)

    assert "python" in result
    assert "docker" in result
    assert "aws" in result

def test_javascript_does_not_match_java():
    text = "The candidate has strong JavaScript experience."

    result = extract_skills(text)

    assert "javascript" in result
    assert "java" not in result

def test_unknown_skills_are_not_extracted():
    text = "Experience with SomeUnknownTechnology is preferred."

    result = extract_skills(text)

    assert result == []

def test_extract_multiple_skills():
    text = """
    The candidate should have experience with Python,
    PostgreSQL, Docker, Kubernetes, Git and Linux.
    """

    result = extract_skills(text)

    expected_skills = {
        "python",
        "postgresql",
        "docker",
        "kubernetes",
        "git",
        "linux"
    }

    assert expected_skills.issubset(set(result))