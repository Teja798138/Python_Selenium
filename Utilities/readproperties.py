import json
import os

class ReadConfig:
    _config_data = None
    @staticmethod
    def _load_config():
        if ReadConfig._config_data is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(current_dir, "config.json")
            if not os.path.exists(config_path):
                raise FileNotFoundError(f"Configuration file not found at {config_path}")

            try:
                with open(config_path, "r", encoding="utf-8") as file:
                    ReadConfig._config_data = json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error parsing JSON configuration file: {e}")
        return ReadConfig._config_data

    @staticmethod
    def getApplicationURL():
        return ReadConfig._load_config().get("url")

    @staticmethod
    def getUseremail():
        return ReadConfig._load_config().get("email")

    @staticmethod
    def getPassword():
        return ReadConfig._load_config().get("password")
