class StringUtil:
    @staticmethod
    def contains_hex(value: str) -> bool:
        return any(c in value for c in "0123456789abcdefABCDEF")
