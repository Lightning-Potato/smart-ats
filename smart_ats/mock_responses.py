import json


def get_mock_analysis_response():
    """
    Returns a mock qualitative AI analysis response
    for local development.
    """

    mock_analysis = {
        "summary": (
            "The candidate demonstrates a solid software engineering "
            "foundation and relevant programming experience, but some "
            "important requirements are not clearly demonstrated."
        ),
        "strengths": [
            "Strong programming foundation",
            "Relevant software engineering education",
            "Experience with multiple programming languages",
        ],
        "gaps": [
            "Limited demonstrated cloud experience",
            "Some role-specific technologies are not clearly demonstrated",
            "Relevant experience could be described in greater detail",
        ],
        "recommendations": [
            "Highlight relevant technical experience where applicable",
            "Add measurable outcomes to technical projects",
            "Demonstrate experience with technologies required by the role",
        ],
    }

    return json.dumps(mock_analysis)
