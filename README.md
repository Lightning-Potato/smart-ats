# Smart ATS

Smart ATS is an AI-powered Applicant Tracking System that analyzes a resume against a job description and provides structured feedback on candidate-job compatibility.

## Current Features

- Job description input through a Streamlit interface
- PDF resume upload and text extraction
- AI-powered resume-job analysis using DeepSeek
- Structured ATS analysis using JSON output
- Overall compatibility score
- Matched and missing skills
- Candidate strengths and gaps
- Resume improvement recommendations
- Mock LLM mode for cost-free local development
- Secure API key management using environment variables

## Tech Stack

- Python
- Streamlit
- PyPDF2
- DeepSeek API
- OpenAI-compatible Python SDK
- python-dotenv
- Git and GitHub

## Project Structure

```text
smart-ats/
├── smart_ats/
│   ├── __init__.py
│   ├── app.py
│   ├── analysis_parser.py
│   ├── llm_client.py
│   ├── mock_responses.py
│   ├── prompts.py
│   ├── ui_components.py
│   └── utility.py
│
├── tests/
│   ├── test_analysis_parser.py
│   └── test_mock_responses.py
│
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

## Development Status

Current release: **v0.2.0**

Version 0.2.0 introduces structured ATS analysis, a dedicated analysis dashboard, mock LLM support, automated testing, improved project reproducibility, and a modular Python package structure.