import sys
import os
from core.config import Config
from unittest.mock import mock_open, patch

def test_default_configs():
    mock_config_yaml = {
        'plugins': []
    }
    with patch("builtins.open", mock_open(read_data="")):
        with patch("yaml.safe_load", return_value=mock_config_yaml):
            config = Config()
            assert config.plugins == []

def test_load_config_file():
    Config.loaded_config = None

    mock_config_yaml = {}
    mock_func = mock_open(read_data="")
    with patch("builtins.open", mock_func):
        Config.load()

    mock_func.assert_called_once()

def test_preloaded_config():

    mock_func = mock_open(read_data="")
    with patch("builtins.open", mock_func):
        Config.load()

    mock_func.assert_not_called()

def test_config_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with patch('sys.exit') as mock_exit:
            Config.loaded_config = None
            Config.load()
            mock_exit.assert_called_once_with(1)

def test_configurable_file_path():
    old_path = os.environ.get('AI_UTILS_CONFIG_PATH')
    os.environ['AI_UTILS_CONFIG_PATH'] = 'test_config'

    mock_func = mock_open(read_data="")
    with patch("builtins.open", mock_func):
        Config.loaded_config = None
        Config.load()

    mock_func.assert_called_once_with('test_config', 'r')

    os.environ['AI_UTILS_CONFIG_PATH'] = old_path if old_path else ''

def test_sets_loaded_config():
    Config.loaded_config = None
    Config.load()

    assert Config.loaded_config is not None