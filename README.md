# Simple Deploy Demo API

A minimal FastAPI application demonstrating CI/CD deployment to AWS EC2 using GitHub Actions.

## Endpoints
- `GET /` — health message
- `GET /health` — health check
- `POST /echo` — echoes back sent text

## Run Locally
\`\`\`bash
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt
uvicorn main:app --reload
\`\`\`

## Run Tests
\`\`\`bash
pytest tests/
\`\`\`

## Run with Docker
\`\`\`bash
docker build -t myapp .
docker run -p 8000:8000 myapp
\`\`\`

## CI/CD
Push to `main` branch triggers:
1. Automated tests (pytest)
2. Deployment to AWS EC2 (only if tests pass)
