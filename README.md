# Ecommerce FastAPI Scaffold

This scaffold contains:
- FastAPI backend (backend/app)
- Docker & docker-compose with Postgres
- Tests with pytest
- GitHub Actions: CI, Semgrep, Snyk, SonarCloud placeholders
- Terraform skeleton (infra/terraform)

## How to run locally

1. Start Docker:
   docker-compose up --build

2. API available at: http://localhost:8000

3. Run tests:
   pytest -q

--- 

Replace placeholder auth with proper JWT and integrate frontend app under /frontend.
