from core.core import LocalAIUtilsCore

def test_getPluginConfig():
    core = LocalAIUtilsCore()
    config = core.getPluginConfig()

    # should only have one key
    assert len(config.keys()) == 1
    assert 'plugins' in config