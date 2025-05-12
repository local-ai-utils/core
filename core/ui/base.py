import logging

log = logging.getLogger(__name__)

class UI:
  def __init__(self, args: dict):
    self.config = args
    pass
  
  def info(self, text: str):
    log.info(text)

  async def message(self, text: str):
    print(text)

  async def prompt(self, text: str):
    return ''
  
  async def confirm(self, text: str):
    return False
    