import json
import os

class ReadConfig:
    _config_data = None
    @staticmethod
    def _load_config():
        if ReadConfig._config_data is None:
            current_dir = os.path.dirname(__file__)
            config_path = os.path.join(current_dir, "config.json")
            with open(config_path, "r") as f:
                ReadConfig._config_data = json.load(f)
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
