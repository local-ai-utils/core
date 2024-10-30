import os
import sys
import yaml

DEFAULT_CONFIG_PATH = os.path.expanduser('~/.config/ai-utils.yaml')

class Config:
    loaded_config = None

    def __init__(self):
        config = Config.load()
        self.plugins = config.get('plugins', [])
        self.keys = config.get('keys', {})

    def load():
        if Config.loaded_config is not None:
            return Config.loaded_config
        
        config_path = os.environ.get('AI_UTILS_CONFIG_PATH', DEFAULT_CONFIG_PATH)

        try:
            with open(config_path, 'r') as file:
                Config.loaded_config = yaml.safe_load(file)
                return Config.loaded_config
            
        except FileNotFoundError:
            print(f"Error: Config file not found at {config_path}")
            sys.exit(1)