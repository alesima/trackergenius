from tracker_genius_geocoder.address import Address
from tracker_genius_geocoder.address_format import AddressFormat
from tracker_genius_geocoder.json_geocoder import JsonGeocoder
from typing import Optional, Dict, Any


class NominatimGeocoder(JsonGeocoder):
    def __init__(self, url: str = None, key: str = None, language: str = None, address_format: Optional[AddressFormat] = None):
        super().__init__(self.format_url(url, key, language), address_format)

    @staticmethod
    def format_url(url: str = None, key: str = None, language: str = None) -> str:
        if url is None:
            url = "https://nominatim.openstreetmap.org/reverse"
        url += "?format=json&zoom=18&addressdetails=1"

        if key is not None:
            url += "&key=" + key

        if language is not None:
            url += "&accept-language=" + language

        return url

    def parse_address(self, json: Dict[str, Any]) -> Optional[Address]:
        result = json.get('address', {})

        if bool(result):
            address = Address()

            if "display_name" in json:
                address.formatted_address = json["display_name"]

            if "house_number" in result:
                address.house = result["house_number"]
            if "road" in result:
                address.street = result["road"]
            if "suburb" in result:
                address.suburb = result["suburb"]

            if "village" in result:
                address.settlement = result["village"]
            elif "town" in result:
                address.settlement = result["town"]
            elif "city" in result:
                address.settlement = result["city"]

            if "state_district" in result:
                address.district = result["state_district"]
            elif "region" in result:
                address.district = result["region"]

            if "state" in result:
                address.state = result["state"]
            if "country_code" in result:
                address.country = result["country_code"].upper()
            if "postcode" in result:
                address.postcode = result["postcode"]

            return address

        return None
