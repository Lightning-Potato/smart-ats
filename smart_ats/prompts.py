def build_initial_analysis_prompt(job_description, resume_text):
    """
    Builds the prompt used for the initial resume-job analysis.
    """

    return f"""
**Role:** You are a highly skilled and experienced Applicant Tracking
System (ATS) analyst with deep expertise in the tech industry and
Human Resources.

**Task:** Your goal is to analyze the provided resume against the
given job description and determine their compatibility.

**Instructions:**
1. Carefully review the job description to understand the key
requirements, skills, and qualifications.

2. Review the resume to identify the candidate's skills, experience,
and qualifications.

3. Provide a short, one-paragraph analysis of how well the resume
aligns with the job description.

4. Do not make up any information. Base your analysis strictly on
the provided documents.

**Documents for Analysis:**

**Job Description:**
---
{job_description}
---

**Resume:**
---
{resume_text}
---
"""

def build_structured_analysis_prompt(job_description, resume_text):
    """
    Builds a prompt that requests a structured ATS analysis in JSON format.
    """

    return f"""
You are a highly skilled Applicant Tracking System (ATS) analyst
with expertise in technical recruitment and Human Resources.

Analyze the resume against the provided job description.

Follow these rules:
1. Base the analysis strictly on the provided job description and resume.
2. Do not invent skills, qualifications, or experience.
3. Identify skills that are clearly supported by the resume.
4. Identify important job requirements that are missing or not demonstrated.
5. Provide an overall compatibility score from 0 to 100.
6. Return ONLY valid JSON.
7. Do not include Markdown code fences or any text outside the JSON.

Return the result using exactly this structure:

{{
    "overall_score": 0,
    "summary": "A concise summary of the candidate's overall alignment.",
    "matched_skills": [
        "skill"
    ],
    "missing_skills": [
        "skill"
    ],
    "strengths": [
        "strength"
    ],
    "gaps": [
        "gap"
    ],
    "recommendations": [
        "recommendation"
    ]
}}

Job Description:
---
{job_description}
---

Resume:
---
{resume_text}
---
"""