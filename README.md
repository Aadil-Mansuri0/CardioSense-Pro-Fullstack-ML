# CardioSense Pro - End-to-End ML Health Risk Platform

[![CI](https://github.com/Aadil-Mansuri0/CardioSense-Pro-Fullstack-ML/actions/workflows/ci.yml/badge.svg)](https://github.com/Aadil-Mansuri0/CardioSense-Pro-Fullstack-ML/actions/workflows/ci.yml)

A full-stack machine-learning application combining a browser UI, FastAPI backend, JWT authentication, per-user prediction history, and a reproducible model-training pipeline.

## Project Links

- Source: [GitHub Repository](https://github.com/Aadil-Mansuri0/CardioSense-Pro-Fullstack-ML)
- Frontend Demo: [https://aadil-mansuri0.github.io/projects/cardiosense/](https://aadil-mansuri0.github.io/projects/cardiosense/)
- API Docs (local): `http://127.0.0.1:8000/docs`
- Health Check (local): `http://127.0.0.1:8000/api/v1/health`
- Deployment Checklist: [`docs/deployment_checklist.md`](docs/deployment_checklist.md)

Deployment note: the frontend demo is hosted and verified through the live portfolio GitHub Pages site. The FastAPI backend is Docker-ready and runs locally, but a public backend URL is not claimed until a backend hosting provider is connected and verified.

## What It Demonstrates

- Interactive frontend for health-risk prediction
- FastAPI REST API with automatic OpenAPI/Swagger documentation
- JWT-based authentication and protected prediction history
- SQLAlchemy persistence with SQLite for local development
- ML training and artifact loading with scikit-learn/joblib
- Model metadata and reproducible evaluation results
- Docker-ready backend
- GitHub Actions CI with automated API tests and route checks

## Verified Model Evaluation

The checked-in model metrics report contains results from 918 rows with a 20% test split. The evaluated models include Gradient Boosting, Random Forest, SVM (RBF), and Logistic Regression.

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Random Forest | 91.30% | 90.57% | 94.12% | 92.31% | 93.44% |
| Gradient Boosting | 89.13% | 90.20% | 90.20% | 90.20% | 93.61% |
| Logistic Regression | 88.04% | 87.74% | 91.18% | 89.42% | 89.92% |
| SVM (RBF) | 86.41% | 85.98% | 90.20% | 88.04% | 92.12% |

Important: these are project evaluation results, not clinical validation. They should not be interpreted as medical-grade diagnostic performance.

## Architecture

```mermaid
flowchart LR
    UI[Browser Frontend] --> API[FastAPI REST API]
    API --> AUTH[JWT Authentication]
    API --> DB[(SQLite / SQLAlchemy)]
    API --> MODEL[Model Service]
    MODEL --> ART[Joblib Model Artifact]
    TRAIN[Training Pipeline] --> ART
    DATA[Kaggle Dataset] --> TRAIN
```

## Project Structure

```text
.
├── CardioSense_Pro_v2.html
├── README.md
├── docs/
│   └── deployment_checklist.md
└── backend/
    ├── app/
    │   ├── api/routes/
    │   ├── core/
    │   ├── db/
    │   ├── models/
    │   ├── schemas/
    │   ├── services/
    │   └── main.py
    ├── ml/
    ├── data/
    ├── model_artifacts/
    ├── tests/
    ├── .env.example
    ├── Dockerfile
    ├── Makefile
    └── requirements.txt
```

## Run Locally

### 1. Start the backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

### 2. Train the model (optional for development)

```bash
python -m ml.download_kaggle_data --dataset-slug fedesoriano/heart-failure-prediction
python -m ml.train
```

The repository also contains a model artifact/metrics report so the application can be inspected without presenting a fabricated benchmark.

### 3. Open the frontend

Serve the repository root with a local static server rather than relying on a `file://` URL:

```bash
python3 -m http.server 5500
```

Then open `http://127.0.0.1:5500/CardioSense_Pro_v2.html`.

## Docker

```bash
cp backend/.env.example backend/.env
docker compose up --build
```

## Environment Variables

Use `backend/.env.example` as the template. Never commit real secrets.

Important settings include:

- `SECRET_KEY`
- `DATABASE_URL`
- `MODEL_ARTIFACT_PATH`
- `CORS_ORIGINS`

## API Surface

Base path: `/api/v1`

- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me`
- `GET /health`
- `POST /predictions` (authenticated)
- `GET /predictions/history` (authenticated)

FastAPI exposes interactive API documentation at `/docs` when the backend is running.

## Quality & CI

Every push and pull request to `main` runs backend validation that:

1. Installs pinned dependencies.
2. Compiles application, ML and test modules.
3. Runs the automated API tests.
4. Verifies required API routes.

Workflow: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

## Educational / Medical Disclaimer

CardioSense Pro is an educational software and machine-learning project. It is not a medical device and must not be used for diagnosis, treatment, or clinical decision-making. Predictions are model outputs and should not replace professional medical advice.

## Engineering Roadmap

- PostgreSQL deployment for production persistence
- Alembic database migrations
- Containerized frontend + backend deployment
- Model versioning and reproducible training artifacts
- Observability and structured application logging

## Author

Aadil Mansuri - CSE (AI) student building ML, data-engineering and backend systems.

[GitHub](https://github.com/Aadil-Mansuri0)
