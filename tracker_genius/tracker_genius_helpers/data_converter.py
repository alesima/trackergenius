import base64
import binascii


class DataConverter:
    @staticmethod
    def parse_hex(string: str) -> bytes:
        try:
            return bytes.fromhex(string)
        except binascii.Error as e:
            raise RuntimeError(str(e))

    @staticmethod
    def print_hex(data: bytes) -> str:
        return binascii.hexlify(data).decode('utf-8')

    @staticmethod
    def parse_base64(string: str) -> bytes:
        try:
            return base64.b64decode(string)
        except binascii.Error as e:
            raise RuntimeError(str(e))

    @staticmethod
    def print_base64(data: bytes) -> str:
        return base64.b64encode(data).decode('utf-8')
