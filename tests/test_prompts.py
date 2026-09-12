from smart_ats.prompts import (
    build_structured_analysis_prompt,
)


def test_structured_prompt_includes_deterministic_findings():
    findings = {
        "skills": {
            "matched_required": ["python"],
            "missing_required": ["docker"],
            "matched_preferred": ["aws"],
            "missing_preferred": [],
            "evidence": {"python": ["experience", "skills"], "aws": ["skills"]},
        },
        "experience": {"required_years": 3, "candidate_years": 2.0, "gap_years": 1.0},
    }

    prompt = build_structured_analysis_prompt(
        "Python and Docker required.", "Experienced Python developer.", findings
    )

    assert "Deterministic ATS Findings" in prompt
    assert '"missing_required"' in prompt
    assert '"docker"' in prompt
    assert '"gap_years": 1.0' in prompt


def test_structured_prompt_preserves_source_documents():
    job_description = "Required skill: Python"

    resume_text = "Experience using Python."

    findings = {
        "skills": {
            "matched_required": ["python"],
            "missing_required": [],
            "matched_preferred": [],
            "missing_preferred": [],
            "evidence": {"python": ["experience"]},
        },
        "experience": {
            "required_years": None,
            "candidate_years": 2.0,
            "gap_years": None,
        },
    }

    prompt = build_structured_analysis_prompt(job_description, resume_text, findings)

    assert job_description in prompt
    assert resume_text in prompt


def test_structured_prompt_instructs_llm_not_to_contradict_findings():
    findings = {
        "skills": {
            "matched_required": [],
            "missing_required": ["docker"],
            "matched_preferred": [],
            "missing_preferred": [],
            "evidence": {},
        },
        "experience": {
            "required_years": None,
            "candidate_years": 1.0,
            "gap_years": None,
        },
    }

    prompt = build_structured_analysis_prompt(
        "Docker required.", "Resume text.", findings
    )

    assert "Do not contradict" in prompt
    assert "deterministic findings" in prompt.lower()
