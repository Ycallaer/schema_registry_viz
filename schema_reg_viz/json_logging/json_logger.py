import logging
import json_log_formatter


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class JsonLogging(object, metaclass=SingletonType):

    def __init__(self):
        formatter = json_log_formatter.JSONFormatter()
        self.json_handler = logging.StreamHandler()
        self.json_handler.setFormatter(formatter)
        self.logger = logging.getLogger('json')

    def get_logger(self, **kwargs):
        """
        Creates a JSON message for the logging compatible for datadog
        :param kwargs: logging_lvl
        :return: logger by name
        """
        logging_lvl = None
        if 'logging_lvl' in kwargs:
            logging_lvl = kwargs['logging_lvl']
        else:
            logging_lvl = logging.INFO

        self.logger.addHandler(self.json_handler)
        self.logger.setLevel(logging_lvl)

        return self.logger
