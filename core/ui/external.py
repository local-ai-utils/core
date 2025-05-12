import logging
import subprocess
from .base import UI

log = logging.getLogger(__name__)

class ExternalUI(UI):
    def __init__(self, args: dict):
        super().__init__(args)

        if 'cmd' not in args:
            raise ValueError('cmd is required in config')

    async def message(self, message: str):
      subprocess.run([self.config['cmd'], 'message', message])

    async def prompt(self, message: str):
      result = subprocess.run([self.config['cmd'], 'prompt', message], capture_output=True, text=True)
      return result.stdout.strip()
    
    async def confirm(self, message: str):
      result = subprocess.run([self.config['cmd'], 'confirm', message])
      return result.returncode == 0
