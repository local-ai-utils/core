import os
import sys
from .terminal import TerminalUI
from .push_notifications import DarwinPushNotificationsUI, PushNotificationsUI
from .external import ExternalUI
from .base import UI
from ..config import Config

CONFIG_MAPPING = {
  'terminal': TerminalUI,
  'external': ExternalUI,
  'push': PushNotificationsUI if sys.platform != 'darwin' else DarwinPushNotificationsUI,
}

__ui = None

def is_terminal():
  return os.isatty(sys.stdout.fileno())

def get_ui():
  global __ui
  if __ui is not None:
    return __ui

  config = Config.load()

  ui_type = None
  ui_config = config.get('ui', 'default')
  ui_args = {}
  if isinstance(ui_config, dict):
    ui_args = ui_config.copy()

    if 'type' not in ui_args:
      raise ValueError('ui.type is required in config')

    ui_type = ui_args.pop('type')
  else:
    ui_type = ui_config

  if ui_type == 'default':
    if is_terminal():
      ui_type = 'terminal'
    else:
      ui_type = 'push'

  if ui_type not in CONFIG_MAPPING:
    raise ValueError(f'Invalid ui type: {ui_type}')

  return CONFIG_MAPPING[ui_type](ui_args)