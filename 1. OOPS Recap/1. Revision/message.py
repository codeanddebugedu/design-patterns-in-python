from abc import abstractmethod
from notifiable import Notifiable


class Message(Notifiable):
    def __init__(self, recipient, content):
        self._recipient = recipient
        self._content = content

    def get_recipient(self):
        return self._recipient

    def get_content(self):
        return self._content

    @abstractmethod
    def send(self):
        pass
