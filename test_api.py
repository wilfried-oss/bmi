from fastapi.testclient import TestClient
from api import app, _calculate_bmi, _advice

client = TestClient(app)


def test_health_check():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_calculate_bmi():
    response = client.post("/calculate_bmi", json={"weight": 70, "height": 1.75})
    assert response.status_code == 200
    bmi_result = _calculate_bmi(70, 1.75)
    assert response.json() == {
        "bmi": round(bmi_result, 2),
        "advice": _advice(bmi_result),
    }
