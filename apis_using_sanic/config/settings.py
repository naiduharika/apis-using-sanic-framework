import os


class ConfigGetter(dict):
    """default getter/setter"""

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError as ke:
            raise AttributeError(f"Config has no '{ke.args[0]}'")

    def __setattr__(self, attr, value):
        self[attr] = value


class WebConfig(ConfigGetter):
    def __init__(self):
        super().__init__({})
        self.host = os.getenv("WEB_HOST")
        self.port = os.getenv("WEB_PORT")


class ServerConfig(ConfigGetter):
    def __init__(self):
        super().__init__()
        self.request_timeout = int(os.getenv("REQUEST_TIMEOUT"))
        self.response_timeout = int(os.getenv("RESPONSE_TIMEOUT"))


class ApplicationConfig(ConfigGetter):
    """Main config class"""

    def __init__(self):
        super().__init__({})
        self.web = WebConfig()
        self.server = ServerConfig()
