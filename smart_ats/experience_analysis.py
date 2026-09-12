from smart_ats.experience_calculator import (
    calculate_total_experience_years,
)
from smart_ats.experience_extractor import (
    extract_required_years,
)
from smart_ats.experience_timeline import (
    extract_experience_periods,
)
from smart_ats.resume_sections import parse_resume_sections



def calculate_experience_match_score(
    candidate_years,
    required_years
):
    """
    Calculates how well the candidate satisfies the
    explicitly stated experience requirement.

    Returns:
        float | None: Match score from 0 to 100,
        or None if no explicit requirement exists.
    """

    if required_years is None:
        return None

    if required_years <= 0:
        return 100.0

    score = min(
        candidate_years / required_years,
        1.0
    ) * 100

    return round(score, 2)

def analyze_experience_match(
    job_description,
    resume_text,
    current_date=None
):
    """
    Analyzes experience compatibility between
    a job description and resume.
    """

    required_years = extract_required_years(
        job_description
    )

    experience_text = get_experience_text(
        resume_text
    )

    experience_periods = extract_experience_periods(
        experience_text
    )

    candidate_years = calculate_total_experience_years(
        experience_periods,
        current_date
    )

    experience_match_score = (
        calculate_experience_match_score(
            candidate_years,
            required_years
        )
    )

    return {
        "required_years": required_years,
        "candidate_years": candidate_years,
        "experience_match_score": experience_match_score,
        "experience_periods": experience_periods,
    }


def get_experience_text(resume_text):
    """
    Returns the most appropriate text for employment
    timeline analysis.

    Uses the recognized experience section when available.
    Falls back to the full resume only when no recognized
    resume sections are detected.
    """

    sections = parse_resume_sections(resume_text)

    if "experience" in sections:
        return sections["experience"]

    if not sections:
        return resume_text

    return ""