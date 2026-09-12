FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY pyproject.toml .
COPY smart_ats ./smart_ats

RUN pip install --no-cache-dir -r requirements.txt

COPY .env.example ./.env.example

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/_stcore/health', timeout=3)"

CMD ["python", "-m", "streamlit", "run", "smart_ats/app.py", "--server.address=0.0.0.0", "--server.port=8501"]