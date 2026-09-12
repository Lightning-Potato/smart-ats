from smart_ats.scoring import calculate_overall_ats_score


def test_overall_score_uses_default_weights():
    score = calculate_overall_ats_score(skill_score=80, experience_score=50)

    assert score == 71.0


def test_overall_score_full_match():
    score = calculate_overall_ats_score(skill_score=100, experience_score=100)

    assert score == 100.0


def test_overall_score_no_match():
    score = calculate_overall_ats_score(skill_score=0, experience_score=0)

    assert score == 0.0


def test_overall_score_without_experience_requirement():
    score = calculate_overall_ats_score(skill_score=75, experience_score=None)

    assert score == 75.0


def test_overall_score_without_skill_requirement():
    score = calculate_overall_ats_score(skill_score=None, experience_score=75)

    assert score == 75.0


def test_overall_score_with_no_available_dimensions():
    score = calculate_overall_ats_score(skill_score=None, experience_score=None)

    assert score is None


def test_overall_score_supports_custom_weights():
    weights = {
        "skills": 0.5,
        "experience": 0.5,
    }

    score = calculate_overall_ats_score(
        skill_score=80, experience_score=60, weights=weights
    )

    assert score == 70.0
