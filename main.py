from apis_using_sanic.config import core
from apis_using_sanic import logger

log = logger.get_logger(__name__)

if __name__ == "__main__":
    log.info("Starting Application")
    core.initialize()
    core.run()
