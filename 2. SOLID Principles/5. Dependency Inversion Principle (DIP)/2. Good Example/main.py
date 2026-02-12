from notification_service import NotificationService
from sms_service import SMSService
from email_service import EmailService


sms_service = SMSService()

ns = NotificationService(sms_service)
ns.notify("Hey")
