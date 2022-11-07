from zoocasa import app, blueprint
from zoocasa.api.contollers import health_check, home


def setup_routes():
    """Register all app routes"""
    app.add_route(health_check, "health", methods=["GET"])

    blueprint.add_route(home, "/", methods=["GET"])
