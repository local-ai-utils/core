import importlib

class PluginManager:
    def __init__(self, core, pluginConfig):
        self.core = core
        self.config = pluginConfig
        self.plugins = {}

        self.load_plugins()

    def getPlugins(self):
        return self.plugins

    def load_plugins(self):
        for plugin_name, config in self.config.items():
            try:
                module = importlib.import_module(f"{plugin_name}")
                if hasattr(module, 'register'):
                    plugin_info = module.register(self.core, config)
                    self.plugins[plugin_name] = plugin_info
                else:
                    print(f"Warning: Plugin {plugin_name} does not have a register function.")
            except ImportError as e:
                print(f"Error: Could not import plugin {plugin_name}")
                # Print all details
                print(e)