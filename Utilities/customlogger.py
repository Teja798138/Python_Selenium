import logging
from pathlib import Path


class Logger:
    @staticmethod
    def setup_logger():
        log_file_path = Path("/Users/voduri.quali.con/PycharmProjects/Healthplix_webautomation/Logs/automation.log")
        log_file_path.parent.mkdir(parents=True, exist_ok=True)
        logger_name = "AutomationLogger"
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            # Create a file handler
            file_handler = logging.FileHandler(log_file_path, mode='a')
            file_handler.setLevel(logging.INFO)
            # Create a formatter
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            # Add the file handler to the logger
            logger.addHandler(file_handler)
        return logger
