import importlib

class PluginManager:
    def __init__(self, core):
        self.core = core
        self.config = self.core.getPluginConfig()
        self.plugins = {}

    def load_plugins(self):
        for plugin_name in self.config['plugins']:
            try:
                module = importlib.import_module(f"{plugin_name}")
                if hasattr(module, 'register'):
                    plugin_info = module.register(self.core)
                    self.plugins[plugin_name] = plugin_info
                else:
                    print(f"Warning: Plugin {plugin_name} does not have a register function.")
            except ImportError as e:
                print(f"Error: Could not import plugin {plugin_name}")
                # Print all details
                print(e)