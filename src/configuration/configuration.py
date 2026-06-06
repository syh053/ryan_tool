import configparser


class Configuration(configparser.ConfigParser):
    def __init__(self, config_file):
        super().__init__()
        self.read(config_file, encoding="utf-8")
