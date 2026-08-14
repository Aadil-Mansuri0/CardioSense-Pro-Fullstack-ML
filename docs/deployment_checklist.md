# CardioSense Pro Deployment Verification Checklist

Use this checklist before claiming a public end-to-end or production-ready deployment.

## Current Verified Status

- Frontend demo is hosted through GitHub Pages.
- FastAPI backend is implemented and Docker-ready for local execution.
- JWT authentication, SQLAlchemy persistence, prediction history and ML inference code exist.
- CI validates backend modules and API routes.
- No public backend URL is claimed in this repository yet.

## Required Before Public End-to-End Claim

1. Deploy the FastAPI backend to a public host.
2. Configure a production-safe `SECRET_KEY` through the hosting platform's secret manager.
3. Configure `DATABASE_URL` for a persistent production database.
4. Set CORS to the exact frontend origin instead of broad local-only defaults.
5. Confirm `/api/v1/health` is reachable publicly.
6. Register/login through the deployed backend.
7. Submit a prediction through the hosted frontend against the hosted backend.
8. Confirm prediction history persists per authenticated user.
9. Confirm API docs are available or intentionally disabled according to deployment policy.
10. Add the verified backend URL and end-to-end demo status to `README.md` only after testing.

## Recommended Production Hardening

- PostgreSQL instead of local SQLite for hosted persistence.
- Alembic migrations for schema changes.
- Structured logging with request IDs.
- Rate limiting for auth and prediction routes.
- HTTPS-only frontend/backend communication.
- Centralized error monitoring.
- Model artifact versioning and retraining notes.
- Dependency update policy and security scanning.

## Claims To Avoid Until Verified

- Production-ready
- Public full-stack deployment
- Clinical or medical-grade prediction system
- Validated diagnostic tool
- HIPAA/healthcare compliance

CardioSense Pro is an educational ML engineering project and should remain described that way unless the project is formally validated and deployed under appropriate standards.
