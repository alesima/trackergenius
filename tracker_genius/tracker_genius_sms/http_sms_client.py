import requests
from tracker_genius_notification.message_exception import MessageException
from tracker_genius_sms.sms_manager import SMSManager
from urllib.parse import quote


class HttpSmsClient(SMSManager):
    def __init__(self, url: str, authorization_header: str, authorization: str, template: str):
        self.url = url
        self.authorization_header = authorization_header
        self.authorization = authorization
        self.template = template
        self.encode = True if template.startswith(
            '{') or self.template.startswith('[') else False
        self.media_type = 'application/json' if self.encode else 'application/x-www-form-urlencoded'

    def prepare_value(self, value):
        return quote(value) if self.encode else value

    def prepare_payload(self, dest_address: str, message: str):
        raise NotImplementedError

    def send_sms(self, dest_address: str, message: str):
        headers = {
            'Content-Type': self.media_type,
            self.authorization_header: self.authorization,
        }

        try:
            response = requests.post(
                self.url,
                headers=headers,
                data=self.prepare_payload(dest_address, message),
            )

            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise MessageException(e)
