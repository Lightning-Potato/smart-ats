import json

import pytest

from smart_ats.analysis_parser import parse_analysis_response


def test_parse_valid_analysis_response():
    response = json.dumps(
        {
            "summary": "Strong alignment with the role.",
            "strengths": ["Strong programming foundation"],
            "gaps": ["Limited cloud experience"],
            "recommendations": ["Gain AWS experience"],
        }
    )

    result = parse_analysis_response(response)

    assert result["summary"] == "Strong alignment with the role."
    assert result["strengths"] == ["Strong programming foundation"]
    assert result["gaps"] == ["Limited cloud experience"]
    assert result["recommendations"] == ["Gain AWS experience"]


def test_parse_invalid_analysis_response():
    invalid_response = "This is not valid JSON."

    with pytest.raises(ValueError):
        parse_analysis_response(invalid_response)


def test_parse_analysis_response_must_be_object():
    response = json.dumps(["summary", "strengths", "gaps", "recommendations"])

    with pytest.raises(ValueError):
        parse_analysis_response(response)


def test_parse_analysis_response_missing_required_fields():
    response = json.dumps({"summary": "Candidate summary."})

    with pytest.raises(ValueError):
        parse_analysis_response(response)


def test_missing_fields_error_identifies_fields():
    response = json.dumps({"summary": "Candidate summary."})

    with pytest.raises(ValueError) as error:
        parse_analysis_response(response)

    message = str(error.value)

    assert "strengths" in message
    assert "gaps" in message
    assert "recommendations" in message
