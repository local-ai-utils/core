import logging
from .base import UI

# https://bugs.python.org/issue25692
# There's a bug that causes input and prompt to be sent to stderr by default.
# Importing readline fixes this.
import readline 

log = logging.getLogger(__name__)

class TerminalUI(UI):
    async def message(self, message: str):
        print(message)

    async def prompt(self, message: str):
        return input(f'{message}: ')
    
    async def confirm(self, message: str):
        return input(f'{message} (y/n): ') == 'y'
