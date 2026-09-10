from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "API is live and alam is talking to you hi"


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_echo():
    response = client.post("/echo", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json()["you_sent"] == "hello"
    assert response.json()["length"] == 5
