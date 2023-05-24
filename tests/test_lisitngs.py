import pytest
from sanic.response import json

from apis_using_sanic import app


@pytest.mark.asyncio
async def test_listings():
    request, response = await app.asgi_client.get("/api/v1/listings?status=For Sale")
    expect_reponse = {
        "data": [
            {"id": 0, "street_address": "134 st", "price": 100, "status": "For Sale"},
        ]
    }
    assert request.method == "GET"
    assert response.json() == expect_reponse
    assert response.status == 200
