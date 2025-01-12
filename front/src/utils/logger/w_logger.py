import logging
import os
from datetime import date, datetime
from logging.handlers import RotatingFileHandler

from pytz import timezone

from modules.setup_env import get_env_instance


class CustomFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        tz = timezone("Asia/Jerusalem")
        record.asctime = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return record.asctime


def create_logger(logger_name: str) -> logging.Logger:
    FORMAT = 'time="%(asctime)s" level="%(levelname)s" source="%(module)s.%(funcName)s:%(lineno)d" thread=%(thread)d message="%(message)s"'
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    logs_dir = get_env_instance().LOGS_PATH
    os.makedirs(logs_dir, exist_ok=True)
    handler = RotatingFileHandler(
        os.path.join(logs_dir, f"{date.today()}.log"),
        maxBytes=30000,
        backupCount=3,
    )
    formatter = CustomFormatter(fmt=FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


logger = create_logger(__name__)
