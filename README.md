# Ecommerce - Ready for Render (FastAPI + React)

## What is included
- Backend: FastAPI app with JWT auth scaffolding, SQLAlchemy models, Alembic integration, Dockerfile and start script that runs migrations.
- Frontend: Vite + React basic scaffold and Dockerfile for production.
- CI/CD: GitHub Actions for tests, builds, Semgrep, Snyk, SonarCloud placeholders.
- Terraform skeleton (AWS) for later infra automation.

## Quick Deploy to Render
1. Push this repo to GitHub.
2. On Render, create a **Postgres** database (Dashboard > New > PostgreSQL). Copy the `External Database URL`.
3. Create a new **Web Service** in Render:
   - Name: ecommerce-api
   - Branch: main
   - Root Directory: (leave empty)
   - Dockerfile Path: `./Dockerfile`
   - Environment Variables:
     - `DATABASE_URL` = (paste your External Database URL)
     - `JWT_SECRET` = (a long random secret)
     - `PORT` = 8000 (optional)
4. Click Create and Render will build the Docker image and deploy. The start script runs `alembic upgrade head` automatically.
5. (Optional) Create a second Web Service for the frontend using `frontend/Dockerfile` or use Render Static Site.

## Local dev
- Start with Docker Compose: `docker-compose up --build`
- API docs: http://localhost:8000/docs

## Notes
- Configure GitHub Secrets: `SNYK_TOKEN`, `SONAR_TOKEN`, `SONAR_ORG`, `SONAR_PROJECT_KEY` for full CI.
- Adjust Alembic migrations before production; current alembic env ready for autogenerate.
