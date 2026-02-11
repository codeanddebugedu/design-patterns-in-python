from notifiable import Notifiable


class WhatsappMessage(Notifiable):
    def __init__(self, phone_number, message):
        super().__init__()
        self.__phone_number = phone_number
        self.__message = message

    def send(self):
        print(f"Sending {self.__message} to {self.__phone_number}")
