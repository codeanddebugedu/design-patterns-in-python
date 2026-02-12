from notification_channel import NotificationChannel


class NotificationService:
    def __init__(self, channel: NotificationChannel):
        self.channel = channel

    def notify(self, message):
        self.channel.send(message)
