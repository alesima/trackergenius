from abc import ABC, abstractmethod


class SmsManager(ABC):
    @abstractmethod
    def send_sms(self, dest_address: str, message: str):
        raise NotImplementedError
