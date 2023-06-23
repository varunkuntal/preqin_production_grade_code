from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_generate_random_vector():
    response = client.post("/generate_random_vector/", json={"text": "This is a test sentence"})
    assert response.status_code == 200
    assert len(response.json()) == 500
    assert isinstance(response.json()[0], float)

def test_empty_sentence():
    response = client.post("/generate_random_vector/", json={"text": ""})
    assert response.status_code == 200
    assert len(response.json()) == 500
    assert isinstance(response.json()[0], float)