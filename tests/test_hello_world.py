import pytest

from apis_using_sanic import app


@pytest.mark.asyncio
async def test_hello_world():
    request, response = await app.asgi_client.get("/api/v1/")

    assert request.method == "GET"
    assert response.text == "Hello World!"
    assert response.status == 200
