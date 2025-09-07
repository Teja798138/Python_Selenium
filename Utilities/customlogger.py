import logging
from pathlib import Path


class Logger:
    @staticmethod
    def setup_logger():
        """
        Sets up and returns a custom logger instance.

        The logger writes to a file and ensures that the logging directory exists.
        It avoids creating duplicate handlers if the logger is already configured.

        Returns:
            logging.Logger: The configured logger instance.
        """
        # Using pathlib for a more modern and robust way to handle file paths.
        log_file_path = Path("/Users/voduri.quali.con/PycharmProjects/Healthplix_webautomation/Logs/automation.log")

        # Ensure the parent directory exists
        log_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Create a custom logger
        logger_name = "AutomationLogger"
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)

        # Avoid adding multiple handlers if the logger is already configured
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
