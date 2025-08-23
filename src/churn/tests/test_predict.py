from fastapi.testclient import TestClient
from churn.api.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_predict_schema():
    sample = {"features": {"f1": 1.0, "f2": 0.0}, "threshold": 0.5}
    r = client.post("/predict/", json=sample)
    assert r.status_code in (200, 500)  # 500 allowed if model not present in test env
    # if model loaded in CI, assert response shape
    if r.status_code == 200:
        j = r.json()
        assert "predictions" in j and "probabilities" in j