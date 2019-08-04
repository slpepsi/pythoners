import logging
import logging.config
import sys
from logging.handlers import RotatingFileHandler


reload(sys)
sys.setdefaultencoding('utf8')


class MyLogger(object):
    def __init__(self):
        pass

    @staticmethod
    def get_logger(log_name="mylogger.log", log_path="/var/log/"):
        logger = logging.getLogger(log_name[:-4])
        formatter = logging.Formatter("%(asctime)s | %(filename)s[line:%(lineno)d] | %(levelname)s | %(message)s")

        # 文件handler
        file_handler = RotatingFileHandler(log_path + log_name, maxBytes=5 * 1024 * 1024, backupCount=2,
                                           encoding="utf8")
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.DEBUG)
        logger.addHandler(console_handler)

        logger.setLevel(logging.DEBUG)
        return logger
