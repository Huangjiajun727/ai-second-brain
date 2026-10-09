from fastapi.testclient import TestClient

from notes.request import app

client = TestClient(app)


def test_get_user():
    response = client.get("/user", params={"id": "123"})
    assert response.status_code == 200
    assert response.json() == {"id": "123", "name": "jjh", "desc": "good"}
