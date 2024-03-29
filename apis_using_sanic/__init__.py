from sanic import Blueprint, Sanic

from apis_using_sanic.config import logger, settings

app = Sanic("Zoocasa Technical Intervie app")
blueprint = Blueprint(name="api", url_prefix="/api/v1")

settings = settings.ApplicationConfig()
logger = logger.ColouredLogs(settings)
