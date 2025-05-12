import importlib
import logging

log = logging.getLogger(__name__)

class PluginManager:
    def __init__(self, core, pluginConfig):
        self.core = core
        self.config = pluginConfig
        self._plugins = None

    async def plugins(self):
        if self._plugins is None:
            await self.load_plugins()

        return self._plugins

    async def load_plugins(self):
        self._plugins = {}

        for plugin_name, config in self.config.items():
            try:
                module = importlib.import_module(f"{plugin_name}")
                if hasattr(module, 'register'):
                    plugin_info = await module.register(self.core, config)
                    self._plugins[plugin_name] = plugin_info
                else:
                    log.warn(f"Warning: Plugin {plugin_name} does not have a register function.")
            except ImportError as e:
                log.warn(f"Error: Could not import plugin {plugin_name}")
                log.warn(e)