from fastapi.testclient import TestClient
from api import app, _calculate_bmi

client = TestClient(app)


def test_health_check():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_welcome_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome de BMI Calculator API"}


def test_calculate_bmi():
    response = client.post("/calculate_bmi", json={"weight": 70, "height": 1.75})
    assert response.status_code == 200
    assert response.json() == {"bmi": _calculate_bmi(70, 1.75)}
