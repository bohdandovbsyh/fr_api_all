import configparser
from constants import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f'{ROOT_DIR}/configurations/app_config.ini')


class ReadConfig:

    @staticmethod
    def get_app_base_url():
        return config.get('app_data', 'base_url')

    @staticmethod
    def get_user_creds():
        return config.get('user_data', 'login'), config.get('user_data', 'password')

    @staticmethod
    def get_browser_id():
        return config.get('browser_data', 'browser_id')

    @staticmethod
    def get_auth_token():
        return config.get('user_data', 'auth_token')
