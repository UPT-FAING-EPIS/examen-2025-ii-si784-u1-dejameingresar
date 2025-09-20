from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_root():
    r = client.get("/api/")
    assert r.status_code == 200
