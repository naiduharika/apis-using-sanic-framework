import logging

import colorlog


class ColouredLogs:
    def __init__(self, config):
        self.log_format = (
            "[%(asctime)s] "
            "[%(name)s > "
            "%(funcName)s] "
            "[%(process)d] "
            "[%(levelname)s] "
            "%(message)s"
        )
        self.bold_seq = "\033[1m"
        self.colorlog_format = f"{self.bold_seq} " "%(log_color)s " f"{self.log_format}"

    def get_logger(self, dunder_name) -> logging.Logger:
        self._logger = logging.getLogger(dunder_name)

        colorlog.basicConfig(format=self.colorlog_format)
        self._logger.setLevel(logging.DEBUG)

        return self._logger
