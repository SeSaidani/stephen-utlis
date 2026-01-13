import sys
from loggers.logger_setup import LoggerSetup


class Logger(LoggerSetup):
    '''
    A class which contains methods that log messages to the configure
    location.
    '''

    def __init__(self):
        super().__init__()

    # Change this to args as this is shit and limited
    def log_it(self, message, level, error_text_1=None, error_text_2=None, error_text_3=None, error_text_4=None):
        """_summary_

        Args:
            message (_type_): _description_
            level (_type_): _description_
            error_text_1 (_type_, optional): _description_. Defaults to None.
            error_text_2 (_type_, optional): _description_. Defaults to None.
        """
        try:
            output_message = message.format(
                error_text_1, error_text_2, error_text_3, error_text_4)
        except Exception as error:
            output_message = str(error)

        try:
            output_message = output_message.replace('\n', '')
            output_message = output_message.replace('  ', '')
        except Exception as error:
            output_message = str(error)

        if level == 'critical':
            self.logger.critical(output_message)
            sys.exit(1)

        elif level == 'info':
            self.logger.info(output_message)

        elif level == 'error':
            self.logger.error(output_message)

        elif level == 'warning' or level == 'warnings':
            self.logger.warning(output_message)

        elif level == 'debug':
            self.logger.debug(output_message)
        else:
            self.logger.critical(output_message)
            sys.exit(1)
