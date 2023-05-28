import boto3
import logging
from botocore.exceptions import BotoCoreError, ClientError
from django.conf import settings
from tracker_genius_sms.sms_manager import SmsManager

logger = logging.getLogger(__name__)


class SnsSmsClient(SmsManager):
    def __init__(self) -> None:
        self.sns_client = boto3.client(
            "sns",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION_NAME,
        )

    def send_sms(self, dest_address: str, message: str):
        sms_attributes = {
            "AWS.SNS.SMS.SenderID": {"DataType": "String", "StringValue": "SNS"},
            "AWS.SNS.SMS.SMSType": {"DataType": "String", "StringValue": "Transactional"},
        }

        try:
            self.sns_client.publish(
                PhoneNumber=dest_address,
                Message=message,
                MessageAttributes=sms_attributes,
            )
        except (BotoCoreError, ClientError) as e:
            logger.error('SMS send failed', exc_info=e)
