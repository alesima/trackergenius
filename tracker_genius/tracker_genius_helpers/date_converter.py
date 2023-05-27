import base64
import binascii


class DateConverter:
    @staticmethod
    def parse_hex(string):
        try:
            return binascii.unhexlify(string)
        except binascii.Error as e:
            raise RuntimeError(e)

    @staticmethod
    def print_hex(data):
        return binascii.hexlify(data).decode()

    @staticmethod
    def parse_base64(string):
        return base64.b64decode(string)

    @staticmethod
    def print_base64(data):
        return base64.b64encode(data).decode()
