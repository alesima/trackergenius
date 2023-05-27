from typing import Dict, Any
from tracker_genius_geocoder.address import Address

"""
Available parameters:
%p - postcode
%c - country
%s - state
%d - district
%t - settlement (town)
%u - suburb
%r - street (road)
%h - house
%f - formatted address
"""


class AddressFormat:
    def __init__(self, format: str = "%h %r, %t, $s, %c") -> None:
        self._format = format

    @staticmethod
    def replace(s: str, key: str, value: str) -> str:
        if value is not None:
            s = s.replace(key, value)
        else:
            s = s.replace(key, "").replace(", ", "").replace(" ,", "")
        return s

    def format(self, o: Dict[str, Any]) -> str:
        address: Address = o
        result = self._format

        result = self.replace(result, "%p", address.postcode)
        result = self.replace(result, "%c", address.country)
        result = self.replace(result, "%s", address.state)
        result = self.replace(result, "%d", address.district)
        result = self.replace(result, "%t", address.settlement)
        result = self.replace(result, "%u", address.suburb)
        result = self.replace(result, "%r", address.street)
        result = self.replace(result, "%h", address.house)
        result = self.replace(result, "%f", address.formatted_address)

        result = result.strip(", ")

        return result
