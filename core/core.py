from .config import Config

class LocalAIUtilsCore:
    def __init__(self):
        self.__config = Config.load()

    def getPluginConfig(self):
        plugins = []
        if 'plugins' in self.__config:
            plugins = self.__config['plugins']

        return {
            'plugins': plugins
        }