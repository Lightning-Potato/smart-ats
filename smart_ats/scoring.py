DEFAULT_SCORE_WEIGHTS = {
    "skills": 0.7,
    "experience": 0.3,
}

def calculate_weighted_score(
    scores,
    weights
):
    """
    Calculates a weighted score using only available dimensions.

    Missing dimensions represented by None are excluded and
    the remaining weights are normalized automatically.
    """

    weighted_sum = 0.0
    active_weight = 0.0

    for dimension, weight in weights.items():
        score = scores.get(dimension)

        if score is None:
            continue

        weighted_sum += score * weight
        active_weight += weight

    if active_weight == 0:
        return None

    return round(
        weighted_sum / active_weight,
        2
    )

def calculate_overall_ats_score(
    skill_score,
    experience_score,
    weights=None
):
    """
    Calculates the overall deterministic ATS score.
    """

    if weights is None:
        weights = DEFAULT_SCORE_WEIGHTS

    scores = {
        "skills": skill_score,
        "experience": experience_score,
    }

    return calculate_weighted_score(
        scores,
        weights
    )