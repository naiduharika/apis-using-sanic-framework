from datetime import datetime
from json import loads

from sanic.request import Request
from sanic.response import HTTPResponse, json, text

from apis_using_sanic import logger
from apis_using_sanic.config.errors import ServerError
from apis_using_sanic.utils.validation import validate
from apis_using_sanic.api.services.get_listings import get_listings

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


async def hello_world(request: Request) -> HTTPResponse:
    """returns hello world"""
    return text("Hello World!")


@validate({"name": {"type": "string"}, "languages": {"type": "list"}})
async def hello_world_intro(request: Request) -> HTTPResponse:
    """returns hello world"""
    req = request.json or {}
    try:
        name_str = f"Hello World! my name is {req['name'].capitalize()}"
        num_languages = f"and I can speak {len(req['languages'])} languages"
        languages_list = f"they are {', '.join(language.capitalize() for language in sorted(req['languages']))}"
        return text(f"{name_str} {num_languages} {languages_list}")
    except Exception as e:
        log.error(e)
        raise ServerError()


async def listings(request: Request) -> HTTPResponse:
    try:
        req = request.args
        print(req)
        listings = get_listings(req)
        return json({"data": listings})
    except Exception as e:
        log.error(e)
        raise ServerError()
