import pytest
from unittest.mock import mock_open, patch

@pytest.fixture(autouse=True)
def mock_config_file():
    mock_yaml = ['one', 'two']

    with patch("builtins.open", mock_open(read_data="")):
        with patch('yaml.safe_load', return_value=mock_yaml):
            yield