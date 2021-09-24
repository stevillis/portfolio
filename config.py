import configparser


def get_config(section, key):
    config = configparser.ConfigParser(interpolation=None)
    config.read('config.ini')
    return config[section][key]
