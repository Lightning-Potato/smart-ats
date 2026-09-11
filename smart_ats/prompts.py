def build_structured_analysis_prompt(job_description, resume_text):
    """
    Builds a prompt that requests structured qualitative
    ATS insights in JSON format.
    """

    return f"""
You are a highly skilled Applicant Tracking System (ATS) analyst
with expertise in technical recruitment and Human Resources.

Analyze the resume against the provided job description.

Follow these rules:
1. Carefully review the job description and resume.

2. Provide a concise summary of the candidate's overall alignment
with the role.

3. Identify qualitative strengths demonstrated by the resume that
are relevant to the job description.

4. Identify important gaps or weaknesses relevant to the role.

5. Provide actionable recommendations for improving the resume's
alignment with the job description.

6. Do not invent skills, qualifications, experience, or achievements.

7. Base all conclusions strictly on the provided documents.

8. Return ONLY valid JSON using the exact structure specified below.

9. Do not include Markdown code fences or any text outside the JSON.

Return the result using exactly this structure:

{{
    "summary": "A concise summary of the candidate's overall alignment.",
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