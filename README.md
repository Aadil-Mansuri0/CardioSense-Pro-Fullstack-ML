# CardioSense Pro - End-to-End Heart Disease ML Platform

CardioSense Pro is now structured as a complete project with:
- Existing modern frontend UI (`CardioSense_Pro_v2.html`)
- Production-style backend API (FastAPI)
- JWT authentication for multi-user access
- Per-user prediction history persisted in database
- ML training pipeline using Kaggle heart disease datasets
- Model artifact loading with backend inference

## Project Structure

```text
.
├── CardioSense_Pro_v2.html
├── README.md
└── backend
    ├── app
    │   ├── api
    │   │   ├── deps.py
    │   │   └── routes
    │   │       ├── auth.py
    │   │       ├── health.py
    │   │       └── predictions.py
    │   ├── core
    │   │   ├── config.py
    │   │   └── security.py
    │   ├── db
    │   │   ├── base.py
    │   │   └── session.py
    │   ├── models
    │   │   ├── prediction.py
    │   │   └── user.py
    │   ├── schemas
    │   │   ├── auth.py
    │   │   └── prediction.py
    │   ├── services
    │   │   ├── feature_schema.py
    │   │   └── model_service.py
    │   └── main.py
    ├── ml
    │   ├── constants.py
    │   ├── dataset_utils.py
    │   ├── download_kaggle_data.py
    │   └── train.py
    ├── data
    │   ├── raw
    │   └── processed
    ├── model_artifacts
    ├── .env.example
    ├── Dockerfile
    └── requirements.txt
```

## Fast Setup (Local)

1. Open terminal in `backend` folder
2. Create virtual environment and install dependencies
3. Configure `.env`
4. Download dataset(s) from Kaggle
5. Train model
6. Run backend API
7. Open frontend HTML file

### Commands

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m ml.download_kaggle_data --dataset-slug fedesoriano/heart-failure-prediction
python -m ml.train
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Or use shortcuts:

```bash
cd backend
make install
make download
make train
make run
```

Then open `CardioSense_Pro_v2.html` in browser.

If browser blocks local file behavior on your setup, serve project root with a static server and open the HTML via localhost.

## Docker Run

```bash
cp backend/.env.example backend/.env
docker compose up --build
```

## Multi-User Flow

Frontend top bar now includes:
- Register
- Login
- Logout
- History

Behavior:
- Logged-in users: prediction calls backend `/api/v1/predictions` and saves history per user.
- Logged-out users: app uses local fallback model (same UX, no persistence).

## API Endpoints

Base: `http://127.0.0.1:8000/api/v1`

- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me`
- `GET /health`
- `POST /predictions` (auth required)
- `GET /predictions/history` (auth required)

## Kaggle + Large Data Strategy

`ml.train` supports combining multiple CSVs automatically:
- Put one or more Kaggle heart-disease CSV files inside `backend/data/raw`
- Training script normalizes schema and merges compatible datasets
- This allows scaling beyond a single small dataset

You can run multiple downloads with different slugs and then retrain.

## Notes

- Default DB: SQLite (`backend/cardiosense.db`)
- JWT auth enabled via `SECRET_KEY`
- If model artifact is missing, backend falls back to safe heuristic mode until training completes
- CORS configured for local frontend/backend development

## Deployment Direction (Next Step)

- Move SQLite to PostgreSQL
- Add Alembic migrations
- Add Redis + background retraining jobs
- Host frontend as static app and backend as containerized API
