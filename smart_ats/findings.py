def calculate_experience_gap(required_years, candidate_years):
    """
    Calculates the candidate's experience gap.

    Returns None when no explicit experience requirement
    is available.
    """

    if required_years is None:
        return None

    return round(max(required_years - candidate_years, 0), 2)


def build_deterministic_findings(skill_analysis, experience_analysis):
    """
    Builds structured findings from deterministic
    ATS analysis results.
    """

    required_years = experience_analysis["required_years"]

    candidate_years = experience_analysis["candidate_years"]

    experience_gap = calculate_experience_gap(required_years, candidate_years)

    skill_evidence = {
        detail["skill"]: sorted(detail["sources"])
        for detail in skill_analysis["matched_skill_details"]
    }

    return {
        "skills": {
            "matched_required": skill_analysis["matched_required_skills"],
            "missing_required": skill_analysis["missing_required_skills"],
            "matched_preferred": skill_analysis["matched_preferred_skills"],
            "missing_preferred": skill_analysis["missing_preferred_skills"],
            "evidence": skill_evidence,
        },
        "experience": {
            "required_years": required_years,
            "candidate_years": candidate_years,
            "gap_years": experience_gap,
        },
    }
