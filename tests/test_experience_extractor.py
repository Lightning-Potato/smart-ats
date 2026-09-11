from smart_ats.experience_extractor import extract_required_years


def test_extract_required_years():
    text = (
        "Candidates should have 3 years of experience "
        "in software development."
    )

    assert extract_required_years(text) == 3

def test_extract_required_years_with_plus():
    text = (
        "We require 5+ years of experience "
        "in backend engineering."
    )

    assert extract_required_years(text) == 5

def test_extract_at_least_required_years():
    text = (
        "Candidates should have at least 4 years "
        "of professional software engineering experience."
    )

    assert extract_required_years(text) == 4

def test_extract_minimum_required_years():
    text = (
        "A minimum of 2 years of relevant "
        "industry experience is required."
    )

    assert extract_required_years(text) == 2

def test_extract_single_year_requirement():
    text = "At least 1 year of professional experience is required."

    assert extract_required_years(text) == 1

def test_no_explicit_experience_requirement():
    text = (
        "Experience with Python and cloud "
        "technologies is preferred."
    )

    assert extract_required_years(text) is None