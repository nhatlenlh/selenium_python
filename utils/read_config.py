import json
import os
import pytest
class ConfigReader:
    _config = None
    @staticmethod
    def load_config():
            if ConfigReader._config is None:
                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                config_path = os.path.join(base_dir, "testsetting.json")
                with open(config_path, "r") as file:
                   ConfigReader._config  = json.load(file)
            return ConfigReader._config
    @staticmethod
    def get_base_url():
         return ConfigReader.load_config()['base-url']
    @staticmethod
    def get_username():
         return ConfigReader.load_config()['username']
    @staticmethod
    def get_password():
         return ConfigReader.load_config()['password']
    
    @staticmethod
    def get_new_user():
         return ConfigReader.load_config()['new-user']
    
    @staticmethod
    def get_search_user():
         return ConfigReader.load_config()['search-user']
    @staticmethod
    def get_new_vacancy():
         return ConfigReader.load_config()['new-vacancy']
