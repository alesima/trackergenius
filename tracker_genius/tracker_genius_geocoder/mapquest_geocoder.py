from tracker_genius_geocoder.json_geocoder import JsonGeocoder
from tracker_genius.tracker_genius_geocoder.address import Address
from tracker_genius.tracker_genius_geocoder.address_format import AddressFormat
from typing import Any, Dict, Optional


class MapQuestGeocoder(JsonGeocoder):
    def __init__(self, url: str = None, key: str = None, address_format: Optional[AddressFormat] = None) -> None:
        super().__init__(self.format_url(url, key), address_format)

    @staticmethod
    def format_url(url: str = None, key: str = None):
        if url is not None:
            url = 'http://www.mapquestapi.com/geocoding/v1/reverse'

        if key is not None:
            url += '?key=' + key + "&location=%f,%f"

        return url

    def parse_address(self, json: Dict[str, Any]) -> Optional[Address]:
        result = json.get('results', [{}])

        if len(result):
            locations = result[0].get('locations', [{}])

            if len(locations):
                location = locations[0]

                address = Address()

                if 'street' in location:
                    address.street = location['street']
                elif 'adminArea5' in location:
                    address.settlement = location['adminArea5']
                elif 'adminArea4' in location:
                    address.district = location['adminArea4']
                elif 'adminArea3' in location:
                    address.state = location['adminArea3']
                elif 'adminArea1' in location:
                    address.country = location['adminArea1'].upper()
                elif 'postalCode' in location:
                    address.postcode = location['postalCode']

                return address

        return None
