from datetime import datetime

from sanic.request import Request
from sanic.response import HTTPResponse, json, text

from zoocasa import logger

log = logger.get_logger(__name__)


async def health_check(request: Request) -> HTTPResponse:
    """Get system health"""
    return json(
        {
            "status": "OK",
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "version": "0.1.0",
        }
    )


async def home(request: Request) -> HTTPResponse:
    """returns hello world"""
    return text("Hello World!")
