import json
import pytest

from smart_ats.analysis_parser import parse_analysis_response


def test_parse_valid_analysis_response():
    response = json.dumps({
        "overall_score": 80,
        "summary": "Strong alignment with the role.",
        "matched_skills": ["Python", "Git"],
        "missing_skills": ["AWS"],
        "strengths": ["Strong programming foundation"],
        "gaps": ["Limited cloud experience"],
        "recommendations": ["Gain AWS experience"]
    })

    result = parse_analysis_response(response)

    assert result["overall_score"] == 80
    assert result["summary"] == "Strong alignment with the role."
    assert result["matched_skills"] == ["Python", "Git"]
    assert result["missing_skills"] == ["AWS"]

def test_parse_invalid_analysis_response():
    invalid_response = "This is not valid JSON."

    with pytest.raises(ValueError):
        parse_analysis_response(invalid_response)