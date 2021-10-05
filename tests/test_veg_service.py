import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from server.app import app

app2 = TestClient(app)

TEST_API_URL = 'http://0.0.0.0:8000/vegetables'


def log(a: str):
    f = open('pr.txt', '+w')
    f.write(a)
    f.close()


class TestVegetable:
    COLLECTIONS_COUNT = 14

    def test_get(self):
        res = app2.get("/vegetables")
        assert res.json()['code'] == 200
        total_items = res.json().get('size')
        assert total_items == TestVegetable.COLLECTIONS_COUNT

    @pytest.mark.asyncio
    async def test_root(self):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to this fantastic app!"}
