from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "Ecommerce API" in r.json().get("message", "")

def test_list_products_empty():
    r = client.get("/api/products/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
