# Ecommerce Documentation

## Levantar en desarrollo (local)

1. Backend
   - Desde la carpeta `backend`:
     - Para ejecutar con Docker Compose:
       ```
       docker compose up --build
       ```
     - O con dotnet (asegúrate de tener Postgres en localhost):
       ```
       dotnet build
       dotnet run --project Ecommerce.Api
       ```

2. Frontend
   - Desde la carpeta `frontend`:
     ```
     npm install
     npm run dev
     ```

## CI/CD
- Workflows en `.github/workflows`:
  - `ci.yml` - Build & test
  - `scan-and-report.yml` - SonarCloud / Semgrep / Snyk
  - `deploy.yml` - Terraform apply

## Reemplazar variables
- Añade tus secrets de GitHub: `SONAR_TOKEN`, `SNYK_TOKEN`, y los secrets para AWS si usas deploy automático.
