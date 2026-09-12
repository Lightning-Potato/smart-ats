# Smart ATS

Smart ATS is an AI-powered Applicant Tracking System that analyzes a resume against a job description and provides structured feedback on candidate-job compatibility.

## Current Features

- Job description input and PDF resume upload through Streamlit
- PDF text extraction using PyPDF2
- Deterministic resume section parsing
- Separation of Skills, Experience, Education, and Projects sections
- Section-aware professional experience analysis
- Technical skill extraction with normalization and alias resolution
- Source-based skill evidence tracking across Skills, Experience, and Projects
- Required and preferred job skill classification
- Requirement-aware deterministic skill matching
- Separate required and preferred skill presentation
- Deterministic experience requirement extraction
- Resume employment timeline parsing
- Overlapping employment period handling
- Deterministic skill and experience scoring
- Weighted overall ATS scoring with missing-dimension normalization
- Structured deterministic findings for LLM grounding
- Grounded AI-generated summaries, strengths, gaps, and recommendations
- Structured LLM response validation
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
│   ├── findings.py
│   ├── job_requirements.py
│   ├── llm_client.py
│   ├── matching_engine.py
│   ├── mock_responses.py
│   ├── prompts.py
│   ├── resume_sections.py
│   ├── scoring.py
│   ├── skill_aliases.py
│   ├── skill_analysis.py
│   ├── skill_evidence.py
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

Smart ATS uses a hybrid architecture that combines deterministic
resume-job matching with grounded LLM-generated qualitative feedback.

```text
Job Description                     Resume
       │                               │
       ▼                               ▼
Requirement Parsing             Section Parsing
       │                               │
Required / Preferred           Skills / Experience /
Skills                         Projects / Education
       │                               │
       └──────────────┬────────────────┘
                      ▼
             Deterministic Engine
                      │
             ┌────────┴─────────┐
             │                  │
             ▼                  ▼
       ATS Scoring      Structured Findings
             │                  │
             │                  ▼
             │               LLM
             │                  │
             │          Qualitative Insights
             │                  │
             └────────┬─────────┘
                      ▼
                 ATS Dashboard
```

Deterministic parsing, matching, and scoring are used for measurable
resume-job compatibility. These results are transformed into structured
findings that ground the LLM's qualitative analysis.

The LLM does not determine the ATS score. It uses deterministic findings
together with the original documents to generate summaries, strengths,
gaps, and recommendations.

## Scoring Model

The current deterministic ATS score combines two supported dimensions:

- Required Skill Match: 70%
- Experience Match: 30%

The skill score is calculated from explicitly classified required
skills. Preferred skills are analyzed and reported separately and do
not reduce the required-skill match score.

When a scoring dimension is unavailable, it is represented as N/A.
The overall scoring model excludes unavailable dimensions and
automatically normalizes the remaining active weights.

For example, if no explicit required technical skills can be scored
but an experience requirement is available, the overall ATS score is
calculated entirely from the experience dimension.

The weighting model is project-defined and is not intended to represent
a proprietary or industry-standard ATS algorithm.

## Known Limitations

- Resume section detection relies on a curated set of recognized headings.
- Unstructured resumes may preserve detected skills without reliable evidence-source classification.
- Skill extraction relies on a curated technical vocabulary and known aliases.
- Specialized or unknown technologies may not be detected.
- Required and preferred skill classification works best with explicit job-description section headings.
- Requirement language embedded in free-form sentences may use fallback classification rather than precise requirement semantics.
- Experience requirement extraction supports a limited set of explicit year-based phrases.
- Employment timeline parsing supports selected month-year formats.
- Section-aware parsing reduces education-date contamination but does not provide full semantic document understanding.
- Deterministic scoring currently covers required technical skills and explicit experience requirements only.
- LLM insights are grounded through prompting but remain generative and are not mathematically guaranteed to follow every instruction.
- Scanned PDF resumes are not currently supported through OCR.

## Development Status

Current release: **v0.4.0**

Version 0.4.0 introduces structured resume and job-description
understanding, source-based skill evidence, requirement-aware matching,
and deterministic findings used to ground qualitative AI analysis.