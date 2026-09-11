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