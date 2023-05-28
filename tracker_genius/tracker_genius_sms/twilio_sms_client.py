import logging
from django.conf import settings
from tracker_genius_sms.sms_manager import SmsManager
from twilio.rest import Client

logger = logging.getLogger(__name__)


class TwilioSmsClinet(SmsManager):
    def __init__(self) -> None:
        self.account_sid = settings.TWILIO_ACCOUNT_SID
        self.auth_token = settings.TWILIO_AUTH_TOKEN
        self.sender_phone_number = settings.TWILIO_SENDER_PHONE_NUMBER
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, dest_address: str, message: str):
        try:
            self.client.messages.create(
                to=dest_address,
                from_=self.sender_phone_number,
                body=message
            )
        except Exception as e:
            logger.error("SMS send failed", exc_info=e)
