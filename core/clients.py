from openai import OpenAI

class ClientManager:
    def __init__(self, core, keys):
        if type(keys) is not dict:
            raise TypeError("ClientManager's third parameter, keys, must be a dictionary")
        
        self.core = core
        self.__keys = keys
        self.__clients = {}

    def open_ai(self):
        if 'openai' in self.__clients:
            return self.__clients['openai']
        elif 'openai' in self.__keys:
            return OpenAI(api_key=self.__keys['openai'])
        else:
            return None