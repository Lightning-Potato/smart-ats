from smart_ats.analysis_parser import parse_analysis_response
from smart_ats.mock_responses import get_mock_analysis_response


def test_mock_response_is_valid():
    response = get_mock_analysis_response()

    analysis = parse_analysis_response(response)

    assert isinstance(analysis, dict)


def test_mock_response_contains_required_fields():
    response = get_mock_analysis_response()

    analysis = parse_analysis_response(response)

    required_fields = ["summary", "strengths", "gaps", "recommendations"]

    for field in required_fields:
        assert field in analysis


def test_mock_response_excludes_deterministic_fields():
    response = get_mock_analysis_response()

    analysis = parse_analysis_response(response)

    deterministic_fields = ["overall_score", "matched_skills", "missing_skills"]

    for field in deterministic_fields:
        assert field not in analysis
