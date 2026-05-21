import configparser


class Configuration:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file, encoding="utf-8")

    def __getitem__(self, key):
        return self.config[key]
