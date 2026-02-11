from message import Message


class SMS(Message):
    def __init__(self, recipient, content):
        super().__init__(recipient, content)

    def send(self):
        print(f"Sending {self._content} to {self._recipient}")
