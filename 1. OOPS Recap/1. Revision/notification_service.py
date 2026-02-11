from email_c import Email
from whatsappmessage import WhatsappMessage


class NotificationService:
    def __init__(self):
        self.notification_channels = {}

    def add_channel(self, channel_name, notifiable):
        self.notification_channels[channel_name] = notifiable

    def send_notification(self, channel_name):
        notifiation = self.notification_channels.get(channel_name)
        if notifiation is not None:
            notifiation.send()  # Runtime Poly


ns = NotificationService()
ns.add_channel("e", Email("info@codeanddebug.in", "Hey Greetings"))
ns.add_channel("x", WhatsappMessage("432432423423", "Heyyy"))

ns.send_notification("e")
ns.send_notification("x")
