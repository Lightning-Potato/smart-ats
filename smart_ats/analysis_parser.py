import json

REQUIRED_ANALYSIS_FIELDS = {
    "summary",
    "strengths",
    "gaps",
    "recommendations",
}


def parse_analysis_response(response):
    """
    Parses and validates a structured LLM analysis response.

    Returns:
        dict: Parsed and validated qualitative ATS analysis.

    Raises:
        ValueError: If the response is invalid JSON, is not a JSON
        object, or is missing required fields.
    """

    try:
        analysis = json.loads(response)

    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse LLM response as JSON: {e}")

    if not isinstance(analysis, dict):
        raise ValueError("LLM analysis response must be a JSON object.")

    missing_fields = REQUIRED_ANALYSIS_FIELDS - analysis.keys()

    if missing_fields:
        raise ValueError(
            "LLM analysis response is missing required fields: "
            + ", ".join(sorted(missing_fields))
        )

    return analysis
