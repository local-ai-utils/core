from .config import Config
from .clients import ClientManager
from .plugin_manager import PluginManager

class LocalAIUtilsCore:
    def __init__(self):
        self.__config = Config()
        self.clients = ClientManager(self, self.__config.keys)
        self.plugins = PluginManager(self, self.__config.plugins)

    def getPlugins(self):
        return self.plugins.getPlugins()