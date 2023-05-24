from json import dumps
import pytest

from apis_using_sanic import app


@pytest.mark.asyncio
async def test_hello_world_intro():
    params = {
        "name": "harika",
        "languages": ["english", "hindi", "telugu", "tamil", "kannada"],
    }

    request, response = await app.asgi_client.post("/api/v1/intro", json=params)

    assert request.method == "POST"
    assert (
        response.text
        == "Hello World! my name is Harika and I can speak 5 languages they are English, Hindi, Kannada, Tamil, Telugu"
    )
    assert response.status == 200
