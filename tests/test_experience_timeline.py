from datetime import date

from smart_ats.experience_timeline import (
    extract_experience_periods,
)


def test_extract_completed_experience_period():
    resume = """
    Software Engineer
    Jan 2021 - Dec 2022
    """

    periods = extract_experience_periods(resume)

    assert len(periods) == 1
    assert periods[0]["start"] == date(2021, 1, 1)
    assert periods[0]["end"] == date(2022, 12, 1)

def test_extract_current_experience_period():
    resume = """
    Software Engineer
    Jan 2023 - Present
    """

    periods = extract_experience_periods(resume)

    assert len(periods) == 1
    assert periods[0]["start"] == date(2023, 1, 1)
    assert periods[0]["end"] is None

def test_extract_full_month_names():
    resume = """
    Backend Developer
    January 2021 - December 2022
    """

    periods = extract_experience_periods(resume)

    assert periods[0]["start"] == date(2021, 1, 1)
    assert periods[0]["end"] == date(2022, 12, 1)

def test_extract_period_with_en_dash():
    resume = """
    Backend Developer
    June 2021 – December 2022
    """

    periods = extract_experience_periods(resume)

    assert len(periods) == 1

def test_extract_multiple_experience_periods():
    resume = """
    Software Engineer
    Jan 2023 - Present

    Backend Developer
    Jun 2021 - Dec 2022
    """

    periods = extract_experience_periods(resume)

    assert len(periods) == 2

def test_resume_without_experience_periods():
    resume = """
    Skills
    Python, Docker, AWS

    Education
    Bachelor of Computing
    """

    periods = extract_experience_periods(resume)

    assert periods == []

def test_resume_without_experience_periods():
    resume = """
    Skills
    Python, Docker, AWS

    Education
    Bachelor of Computing
    """

    periods = extract_experience_periods(resume)

    assert periods == []