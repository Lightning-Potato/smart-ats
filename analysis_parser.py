import json


def parse_analysis_response(response):
    """
    Parses a JSON response returned by the LLM.

    Returns:
        dict: Parsed ATS analysis.

    Raises:
        ValueError: If the response is not valid JSON.
    """

    try:
        return json.loads(response)

    except json.JSONDecodeError as e:
        raise ValueError(
            f"Failed to parse LLM response as JSON: {e}"
        )