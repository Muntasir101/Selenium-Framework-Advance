import configparser


class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.base_url = config.get('test_environment', 'base_url')
        self.username = config.get('test_credentials', 'username')
        self.password = config.get('test_credentials', 'password')
