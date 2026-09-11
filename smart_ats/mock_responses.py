import json


def get_mock_analysis_response():
    """
    Returns a mock ATS analysis response for local development.
    """

    mock_analysis = {
        "overall_score": 72,
        "summary": (
            "The candidate demonstrates a solid software engineering "
            "foundation and relevant programming experience, but some "
            "important requirements are not clearly demonstrated."
        ),
        "matched_skills": [
            "Python",
            "Java",
            "Git",
            "SQL"
        ],
        "missing_skills": [
            "AWS",
            "Kubernetes",
            "PyTorch"
        ],
        "strengths": [
            "Strong programming foundation",
            "Relevant software engineering education",
            "Experience with multiple programming languages"
        ],
        "gaps": [
            "Limited demonstrated cloud experience",
            "No explicit Kubernetes experience",
            "No explicit PyTorch experience"
        ],
        "recommendations": [
            "Highlight relevant cloud experience if applicable",
            "Add measurable outcomes to technical projects",
            "Demonstrate experience with technologies required by the role"
        ]
    }

    return json.dumps(mock_analysis)