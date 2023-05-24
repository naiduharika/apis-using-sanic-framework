from json import loads

import pytest

from apis_using_sanic import app


@pytest.mark.asyncio
async def test_health():
    request, response = await app.asgi_client.get("/health")

    assert request.method == "GET"
    assert loads(response.body).get("version") == "0.1.0"
    assert response.status == 200
