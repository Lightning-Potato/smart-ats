from datetime import date

from smart_ats.experience_analysis import (
    analyze_experience_match,
    calculate_experience_match_score,
)


def test_experience_score_partial_match():
    score = calculate_experience_match_score(
        candidate_years=2,
        required_years=4
    )

    assert score == 50.0

def test_experience_score_exact_match():
    score = calculate_experience_match_score(
        candidate_years=4,
        required_years=4
    )

    assert score == 100.0

def test_experience_score_is_capped_at_100():
    score = calculate_experience_match_score(
        candidate_years=8,
        required_years=4
    )

    assert score == 100.0

def test_experience_score_without_requirement():
    score = calculate_experience_match_score(
        candidate_years=3,
        required_years=None
    )

    assert score is None

def test_analyze_experience_match():
    job_description = """
    Candidates should have 3+ years of experience
    in software engineering.
    """

    resume_text = """
    Software Engineer
    Jan 2022 - Dec 2024
    """

    result = analyze_experience_match(
        job_description,
        resume_text
    )

    assert result["required_years"] == 3
    assert result["candidate_years"] == 3.0
    assert result["experience_match_score"] == 100.0

def test_analyze_current_experience():
    job_description = """
    At least 3 years of experience is required.
    """

    resume_text = """
    Software Engineer
    Jan 2024 - Present
    """

    result = analyze_experience_match(
        job_description,
        resume_text,
        current_date=date(2026, 12, 1)
    )

    assert result["required_years"] == 3
    assert result["candidate_years"] == 3.0
    assert result["experience_match_score"] == 100.0

def test_analyze_insufficient_experience():
    job_description = """
    Candidates should have 4 years of experience.
    """

    resume_text = """
    Software Engineer
    Jan 2023 - Dec 2024
    """

    result = analyze_experience_match(
        job_description,
        resume_text
    )

    assert result["candidate_years"] == 2.0
    assert result["experience_match_score"] == 50.0