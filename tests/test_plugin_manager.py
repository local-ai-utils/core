import importlib
import yaml
from unittest.mock import patch
from core.plugin_manager import PluginManager
from core.core import LocalAIUtilsCore
from core.config import Config

def test_loads_one_plugin():
    class MockPlugin:
        def register(plugin):
            pass


    mock_yaml = {
        'plugins': [1]
    }
    with patch('yaml.safe_load', return_value=mock_yaml):
        Config.loaded_config = None
        core_inst = LocalAIUtilsCore()
        mgr = PluginManager(core_inst)
        with patch("importlib.import_module", return_value=MockPlugin):
            with patch.object(core_inst, 'getPluginConfig', return_value=[1,2]):
                mgr.load_plugins()

    assert len(mgr.plugins) == 1

def test_loads_two_plugins():
    class MockPlugin:
        def register(plugin):
            pass


    mock_yaml = {
        'plugins': [1,2]
    }
    with patch('yaml.safe_load', return_value=mock_yaml):
        Config.loaded_config = None
        core_inst = LocalAIUtilsCore()
        mgr = PluginManager(core_inst)
        with patch("importlib.import_module", return_value=MockPlugin):
            with patch.object(core_inst, 'getPluginConfig', return_value=[1,2]):
                mgr.load_plugins()

    assert len(mgr.plugins) == 2
        
