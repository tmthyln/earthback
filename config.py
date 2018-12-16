import os
import yaml


CONFIG_FILE = 'config.yaml'


if not os.path.exists(CONFIG_FILE):
    DEFAULT_CONFIG = {
        'source': 'earthporn',
        'rotf': 1,
    }
    
    with open(CONFIG_FILE, 'w') as config_file:
        yaml.dump(DEFAULT_CONFIG, config_file)

with open(CONFIG_FILE) as config_file:
    _config = yaml.load(config_file)


def get_property(prop):
    if prop not in _config:
        raise ValueError(f'config property does not exist: {prop}')
    
    return _config[prop]


def set_property(prop: str, val: str):
    if prop not in _config:
        raise ValueError(f'config property does not exist: {prop}')
    
    _config[prop] = val
    
    with open(CONFIG_FILE) as config_file:
        yaml.dump(_config, config_file)

