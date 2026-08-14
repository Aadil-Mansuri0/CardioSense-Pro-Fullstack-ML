from fastapi.testclient import TestClient

from app.main import app


def test_root_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "CardioSense Pro API is running"


def test_health_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert "model_loaded" in payload
    assert "model_version" in payload
