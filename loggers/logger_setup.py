import logging
import logging.config
import yaml


class LoggerSetup:
    """
    A class that configures the logging setup.

    The default file path  to the config file is ./config/config.cfg

    The default path to the logging YAML config file is ./config/logging.yaml

    config_path: The path to the config file. default: None
    logger_config_path: The path the logging YAML config file. default: None

    """

    def __init__(self, logger_name='meta_ss', logger_config_path=None):

        if logger_config_path is None:
            self.logger_config_path = './loggers/logging.yaml'
        else:
            self.logger_config_path = logger_config_path

        with open(self.logger_config_path, 'r', encoding='utf8') as log_config:
            config_yml = log_config.read()
            config_dict = yaml.load(config_yml, Loader=yaml.FullLoader)
            logging.config.dictConfig(config_dict)
        self.logger = logging.getLogger(logger_name)
