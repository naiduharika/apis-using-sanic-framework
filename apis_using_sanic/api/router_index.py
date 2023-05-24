from apis_using_sanic import app, blueprint
from apis_using_sanic.api.controllers import (
    health_check,
    hello_world,
    hello_world_intro,
    listings,
)


def setup_routes():
    """Register all app routes"""
    app.add_route(health_check, "health", methods=["GET"])

    blueprint.add_route(hello_world, "/", methods=["GET"])
    blueprint.add_route(hello_world_intro, "/intro", methods=["POST"])
    blueprint.add_route(listings, "/listings", methods=["GET"])
