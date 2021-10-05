from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)

class TestVegetable:
    def test_read_main(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}
