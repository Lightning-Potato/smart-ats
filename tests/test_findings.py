import json


from smart_ats.findings import (
    build_deterministic_findings,
    calculate_experience_gap,
)


def test_calculate_experience_gap():
    gap = calculate_experience_gap(
        required_years=4,
        candidate_years=2.5
    )

    assert gap == 1.5


def test_experience_gap_is_never_negative():
    gap = calculate_experience_gap(
        required_years=3,
        candidate_years=5
    )

    assert gap == 0


def test_experience_gap_is_none_without_requirement():
    gap = calculate_experience_gap(
        required_years=None,
        candidate_years=5
    )

    assert gap is None


def test_build_deterministic_findings():
    skill_analysis = {
        "matched_required_skills": [
            "python"
        ],
        "missing_required_skills": [
            "docker"
        ],
        "matched_preferred_skills": [
            "aws"
        ],
        "missing_preferred_skills": [
            "kubernetes"
        ],
        "matched_skill_details": [
            {
                "skill": "python",
                "detected": True,
                "sources": {
                    "skills",
                    "experience"
                }
            },
            {
                "skill": "aws",
                "detected": True,
                "sources": {
                    "skills"
                }
            }
        ]
    }

    experience_analysis = {
        "required_years": 3,
        "candidate_years": 2.0,
    }

    findings = build_deterministic_findings(
        skill_analysis,
        experience_analysis
    )

    assert findings["skills"][
        "matched_required"
    ] == ["python"]

    assert findings["skills"][
        "missing_required"
    ] == ["docker"]

    assert findings["skills"][
        "matched_preferred"
    ] == ["aws"]

    assert findings["skills"][
        "missing_preferred"
    ] == ["kubernetes"]

    assert findings["skills"]["evidence"][
        "python"
    ] == [
        "experience",
        "skills"
    ]

    assert findings["experience"][
        "required_years"
    ] == 3

    assert findings["experience"][
        "candidate_years"
    ] == 2.0

    assert findings["experience"][
        "gap_years"
    ] == 1.0



def test_deterministic_findings_are_json_serializable():
    skill_analysis = {
        "matched_required_skills": ["python"],
        "missing_required_skills": [],
        "matched_preferred_skills": [],
        "missing_preferred_skills": [],
        "matched_skill_details": [
            {
                "skill": "python",
                "detected": True,
                "sources": {
                    "skills",
                    "projects"
                }
            }
        ]
    }

    experience_analysis = {
        "required_years": None,
        "candidate_years": 2.0,
    }

    findings = build_deterministic_findings(
        skill_analysis,
        experience_analysis
    )

    serialized = json.dumps(findings)

    assert isinstance(serialized, str)