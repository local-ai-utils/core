from .config import Config

class LocalAIUtilsCore:
    def __init__(self):
        self.__config = Config.load()

    def getPluginConfig(self):
        return {
            self.__config.plugins
        }