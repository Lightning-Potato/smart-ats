# Smart ATS

Smart ATS is an AI-powered Applicant Tracking System that analyzes a resume against a job description and provides structured feedback on candidate-job compatibility.

## Current Features

- Job description input and PDF resume upload through Streamlit
- PDF text extraction using PyPDF2
- Deterministic technical skill extraction from raw text
- Skill normalization and alias resolution
- Deterministic skill matching and scoring
- Job experience requirement extraction
- Resume employment timeline parsing
- Overlapping employment period handling
- Deterministic experience duration and match scoring
- Weighted overall ATS scoring with missing-dimension normalization
- Structured ATS analysis dashboard
- AI-generated qualitative insights using DeepSeek
- Mock LLM mode for cost-free local development
- Automated testing with pytest
- Continuous integration using GitHub Actions
- Secure API key management using environment variables

## Tech Stack

- Python 3.12
- Streamlit
- PyPDF2
- DeepSeek API
- OpenAI-compatible Python SDK
- python-dotenv
- pytest
- Git and GitHub
- GitHub Actions

## Project Structure

```text
smart-ats/
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── smart_ats/
│   ├── __init__.py
│   ├── app.py
│   ├── analysis_parser.py
│   ├── experience_analysis.py
│   ├── experience_calculator.py
│   ├── experience_extractor.py
│   ├── experience_timeline.py
│   ├── llm_client.py
│   ├── matching_engine.py
│   ├── mock_responses.py
│   ├── prompts.py
│   ├── scoring.py
│   ├── skill_aliases.py
│   ├── skill_analysis.py
│   ├── skill_extractor.py
│   ├── skill_metadata.py
│   ├── skill_vocabulary.py
│   ├── ui_components.py
│   └── utility.py
│
├── tests/
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Lightning-Potato/smart-ats.git
cd smart-ats
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a local `.env` file from the provided example:

```bash
cp .env.example .env
```

For cost-free local development:

```env
LLM_MODE=mock
```

To use the DeepSeek API:

```env
LLM_MODE=deepseek
DEEPSEEK_API_KEY=your_api_key_here
```

Never commit your real API key to version control.

### 5. Run the Application

```bash
python -m streamlit run smart_ats/app.py
```

## Architecture

Smart ATS uses a hybrid architecture that separates deterministic
matching and scoring from LLM-generated qualitative feedback.

```text
Job Description + Resume
          |
          +----------------------+
          |                      |
          v                      v
 Deterministic Engine        LLM Analysis
          |                      |
     Skill Matching           Summary
     Experience Match         Strengths
     Weighted Scoring         Gaps
          |                   Recommendations
          +----------+-----------+
                     |
                     v
                ATS Dashboard
```

The deterministic engine is responsible for measurable matching and
scoring, while the LLM is used for qualitative interpretation and
resume improvement recommendations.

## Scoring Model

The current deterministic ATS score combines two supported dimensions:

- Skill Match: 70%
- Experience Match: 30%

When a dimension is unavailable, its weight is excluded and the
remaining weights are automatically normalized.

For example, if a job description does not contain an explicit
experience requirement, the overall score is based entirely on the
available skill match score.

The weighting model is project-defined and is not intended to represent
a proprietary or industry-standard ATS algorithm.

## Known Limitations

- Skill extraction currently relies on a curated technical vocabulary
  and known aliases.
- Unknown or highly specialized skills may not be detected.
- Experience requirement extraction currently supports a limited set
  of explicit year-based phrases.
- Resume employment timeline parsing supports selected month-year date
  formats.
- Timeline extraction currently operates on the extracted resume text
  and does not yet fully distinguish employment history from other
  dated sections such as education.
- The current ATS score evaluates skills and explicit experience
  requirements only; education, certifications, seniority, location,
  and other hiring factors are not yet included.
- PDF extraction relies on text-based PDFs and does not currently
  include OCR for scanned resumes.

## Development Status

Current release: **v0.3.0**

Version 0.3.0 introduces deterministic skill and experience matching,
explainable weighted scoring, automated CI validation, and a hybrid
architecture that separates deterministic analysis from LLM-generated
qualitative insights.