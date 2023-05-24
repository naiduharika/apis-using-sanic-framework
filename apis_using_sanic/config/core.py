from apis_using_sanic import app, blueprint, logger, settings
from apis_using_sanic.api import router_index

log = logger.get_logger(__name__)


def initialize():
    app.config.REQUEST_TIMEOUT = settings.server.request_timeout
    app.config.RESPONSE_TIMEOUT = settings.server.response_timeout

    router_index.setup_routes()
    app.blueprint(blueprint)

    log.info("-------- Registered API endpoints --------")
    for (handler, (rule, router)) in app.router.routes_names.items():
        log.info(rule)
    log.info("------------------------------------------")


def run():
    """Starts app and exposes functionality through web services"""
    app.run(host=settings.web.host, port=settings.web.port, access_log=True, debug=True)
