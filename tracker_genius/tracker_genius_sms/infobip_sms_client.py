import logging
import requests
from django.conf import settings
from tracker_genius_sms.http_sms_client import HttpSmsClient


logger = logging.getLogger(__name__)


class InfobipSmsClient(HttpSmsClient):
    def __init__(self):
        url = 'https://api.infobip.com/sms/2/text/single'

        authorization_header = 'Authorization'
        authorization = self.get_authorization_token()

        template = '''
        {
            "from": "{{from}}",
            "to": "{{to}}",
            "text": "{{text}}"
        }
        '''

        super().__init__(url,
                         authorization_header, authorization, template)

    @staticmethod
    def get_authorization_token():
        auth_url = 'https://api.infobip.com/auth/1/authenticate'

        payload = {
            'username': settings.INFOBIP_USERNAME,
            'password': settings.INFOBIP_PASSWORD
        }

        response = requests.post(auth_url, json=payload)

        if response.status_code == 200:
            authorization_token = response.json()['token']
            return f'Bearer {authorization_token}'

    def prepare_payload(self, dest_address: str, message: str):
        placeholders = {
            '{{from}}': self.prepare_value(settings.INFOBIP_SENDER_PHONE_NUMBER),
            '{{to}}': self.prepare_value(dest_address),
            '{{text}}': self.prepare_value(message)
        }

        prepared_template = self.template
        for placeholder, value in placeholders.items():
            prepared_template = prepared_template.replace(placeholder, value)

        return prepared_template
