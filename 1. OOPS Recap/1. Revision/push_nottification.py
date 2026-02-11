from notifiable import Notifiable


class PushNotification(Notifiable):
    def __init__(self, device_id, content):
        super().__init__()
        self.__device_id = device_id
        self.__content = content

    def send(self):
        print(f"Sending {self.__content} to device {self.__device_id}")
