from zoocasa import app, blueprint
from zoocasa.api.contollers import health_check, hello_world, hello_world_intro


def setup_routes():
    """Register all app routes"""
    app.add_route(health_check, "health", methods=["GET"])

    blueprint.add_route(hello_world, "/", methods=["GET"])
    blueprint.add_route(hello_world_intro, "/intro", methods=["POST"])
