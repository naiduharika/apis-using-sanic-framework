"""Error handling"""
import traceback

import sanic.exceptions
import sanic.response
from time import time

from apis_using_sanic import app, logger

log = logger.get_logger(__name__)


class APIException(Exception):
    """Base class for API exceptions"""

    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code


class BadRequest(APIException):
    """HTTP 400 Bad Request"""

    def __init__(self, message=None):
        super().__init__(message, 400)


class Unauthorized(APIException):
    """HTTP 401 Unauthorized"""

    def __init__(self, message=None):
        super().__init__(message, 401)


class Forbidden(APIException):
    """HTTP 403 Forbidden"""

    def __init__(self, message=None):
        super().__init__(message, 403)


class NotFound(APIException):
    """HTTP 404 Not Found"""

    def __init__(self, message=None):
        super().__init__(message, 404)


class ServerError(APIException):
    """HTTP 500 Internal Server Error"""

    def __init__(self, message=None):
        super().__init__(message, 500)


def _default_response(request, exception):
    return sanic.response.json(
        {
            "timestamp": int(time() * 100),
            "message": exception.message,
            "exception": type(exception).__name__,
            "path": request.path,
            "method": request.method,
            "status_code": exception.status_code,
        },
        exception.status_code,
    )


@app.exception(BadRequest)
def invalid_usage(request, exception):
    return _default_response(request, exception)


@app.exception(Unauthorized)
def unauthorized(request, exception):
    return _default_response(request, exception)


@app.exception(Forbidden)
def forbidden(request, exception):
    return _default_response(request, exception)


@app.exception(NotFound)
def not_found(request, exception):
    return _default_response(request, exception)


@app.exception(ServerError)
def sanic_server_error(request, exception):
    exception.message = "An internal server occured."
    return _default_response(request, exception)


@app.exception(sanic.exceptions.NotFound)
def sanic_not_found(request, exception):
    exception.message = "Requested path was not found."
    return _default_response(request, exception)


@app.exception(Exception)
def unhandled_exception(request, exception):

    log.error("error occured: %s", exception)
    traceback.print_tb(exception._traceback_)

    exception.message = "An internal server occured: %s" % str(exception)
    exception.status_code = 500
    return _default_response(request, exception)
