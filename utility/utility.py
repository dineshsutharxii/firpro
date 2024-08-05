import logging

class Utility:
    def custom_logger(self, log_level = logging.DEBUG):
        logger = logging.getLogger(__name__)
        logger.setLevel(log_level)
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(r"C:\Users\dines\fitPeo_assign\fitPeo_assign\logs\logs.txt")
        file_handler.setLevel(logging.DEBUG)  # setLevel to handler
        console_formatter = logging.Formatter(fmt='%(filename)s - %(asctime)s - %(levelname)s - %(message)s',
                                              datefmt='%d-%m-%Y %H:%M:%S')
        file_formatter = logging.Formatter(fmt='%(filename)s - %(asctime)s - %(levelname)s - %(message)s',
                                           datefmt='%d-%m-%Y %H:%M:%S')
        console_handler.setFormatter(console_formatter)  # add Formatter to handler
        file_handler.setFormatter(file_formatter)  # add Formatter to handler
        logger.addHandler(console_handler)  # added handler to logger
        logger.addHandler(file_handler)  # added handler to logger
        return logger
