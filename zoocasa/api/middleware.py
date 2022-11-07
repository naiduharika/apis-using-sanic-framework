from sanic.response import text

from zoocasa import app

CORS_HEADERS = {
    "Access-Control-Allow-Methods": "POST, GET, OPTIONS, PUT, HEAD, DELETE",
    "Access-Control-Max-Age": "3600",
    "Access-Control-Allow-Headers": "Origin, X-Requested-With, \
        Content-Type, Accept, Authorization",
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Expose-Headers": "Authorization",
}


@app.middleware("request")
async def cors_options(request):
    """CORS filter"""
    if request.method == "OPTIONS":
        cors = CORS_HEADERS
        cors["Access-Control-Allow-Origin"] = request.headers.get("origin")
        return text("", status=200, headers=cors)


@app.middleware("response")
async def cors_response(request, response):
    """CORS filter"""
    response.headers["Access-Control-Allow-Origin"] = request.headers.get("origin")
