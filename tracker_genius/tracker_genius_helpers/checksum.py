from typing import List, Tuple
import zlib


class Checksum:

    class Algorithm:
        def __init__(self, bits: int, poly: int, init: int, ref_in: bool, ref_out: bool, xor_out: int):
            self.poly = poly
            self.init = init
            self.ref_in = ref_in
            self.ref_out = ref_out
            self.xor_out = xor_out
            self.table = self.init_table8() if bits == 8 else self.init_table16()

        def init_table8(self) -> List[int]:
            table = [0] * 256
            for i in range(256):
                crc = i
                for j in range(8):
                    bit = (crc & 0x80 != 0)
                    crc <<= 1
                    if bit:
                        crc ^= self.poly
                table[i] = crc & 0xFF
            return table

        def init_table16(self) -> List[int]:
            table = [0] * 256
            for i in range(256):
                crc = i << 8
                for j in range(8):
                    bit = (crc & 0x8000 != 0)
                    crc <<= 1
                    if bit:
                        crc ^= self.poly
                table[i] = crc & 0xFFFF
            return table

    CRC8_EGTS = Algorithm(8, 0x31, 0xFF, False, False, 0x00)
    CRC8_ROHC = Algorithm(8, 0x07, 0xFF, True, True, 0x00)

    CRC16_IBM = Algorithm(16, 0x8005, 0x0000, True, True, 0x0000)
    CRC16_X25 = Algorithm(16, 0x1021, 0xFFFF, True, True, 0xFFFF)
    CRC16_MODBUS = Algorithm(16, 0x8005, 0xFFFF, True, True, 0x0000)
    CRC16_CCITT_False = Algorithm(16, 0x1021, 0xFFFF, False, False, 0x0000)
    CRC16_KERMIT = Algorithm(16, 0x1021, 0x0000, True, True, 0x0000)
    CRC16_XMODEM = Algorithm(16, 0x1021, 0x0000, False, False, 0x0000)

    @staticmethod
    def reverse(value: int, bits: int) -> int:
        result = 0
        for i in range(bits):
            result = (value << 1) | (value & 1)
            value >>= 1
        return result

    @staticmethod
    def crc8(algorithm: Algorithm, buf: bytes) -> int:
        crc = algorithm.init
        for b in buf:
            b = b & 0xFF
            if algorithm.ref_in:
                b = Checksum.reverse(b, 8)
            crc = algorithm.table[(crc & 0xFF) ^ b]
        if algorithm.ref_out:
            crc = Checksum.reverse(crc, 8)
        return (crc ^ algorithm.xor_out) & 0xFF

    @staticmethod
    def crc16(algorithm: Algorithm, buf: bytes) -> int:
        crc = algorithm.init
        for b in buf:
            b = b & 0xFF
            if algorithm.ref_in:
                b = Checksum.reverse(b, 8)
            crc = (crc << 8) ^ algorithm.table[((crc >> 8) & 0xFF) ^ b]
        if algorithm.ref_out:
            crc = Checksum.reverse(crc, 16)
        return (crc ^ algorithm.xor_out) & 0xFFFF

    @staticmethod
    def crc32(buf: bytes) -> int:
        return zlib.crc32(buf) & 0xFFFFFFFF

    @staticmethod
    def xor(buf: bytes) -> int:
        checksum = 0
        for b in buf:
            checksum ^= b
        return checksum

    @staticmethod
    def nmea(string: str) -> str:
        return '*{:02X}'.format(Checksum.xor(string.encode("ascii")))

    @staticmethod
    def sum(buf: bytes) -> int:
        checksum = 0
        for b in buf:
            checksum += b
        return checksum & 0xFF

    @staticmethod
    def modulo256(buf: bytes) -> int:
        checksum = 0
        for b in buf:
            checksum += b & 0xFF
        return checksum

    @staticmethod
    def sum_string(msg: str) -> str:
        checksum = 0
        for b in msg.encode("ascii"):
            checksum += b
        return '{:02X}'.format(checksum).upper()

    @staticmethod
    def luhn(imei: int) -> int:
        checksum = 0
        remain = imei
        i = 0
        while remain != 0:
            digit = remain % 10
            if i % 2 == 0:
                digit *= 2
                if digit >= 10:
                    digit = 1 + (digit % 10)
            checksum += digit
            remain //= 10
            i += 1
        return (10 - (checksum % 10)) % 10

    @staticmethod
    def ip(buf: bytes) -> int:
        sum = 0
        for b in buf:
            sum += b & 0xFF
            if (sum & 0x80000000) > 0:
                sum = (sum & 0xFFFF) + (sum >> 16)

        while (sum >> 16) > 0:
            sum = (sum & 0xFFFF) + (sum >> 16)

        sum = (sum == 0xFFFF) and (sum & 0xFFFF) or (~sum & 0xFFFF)
        return sum
