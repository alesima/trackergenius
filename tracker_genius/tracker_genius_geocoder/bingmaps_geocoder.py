from typing import Any, Dict, Optional, List
from tracker_genius.tracker_genius_geocoder.address import Address
from tracker_genius.tracker_genius_geocoder.address_format import AddressFormat
from tracker_genius_geocoder.json_geocoder import JsonGeocoder


class BingMapsGeocoder(JsonGeocoder):
    def __init__(self, url: str, key: str, address_format: Optional[AddressFormat]) -> None:
        super().__init__(self.format_url(url, key), address_format)

    @staticmethod
    def format_url(url: str = None, key: str = None) -> str:
        return f'{url}/Locations/%f,%f?key={key}&include=ciso2'

    def parse_address(self, json: Dict[str, Any]) -> Optional[Address]:
        result: List[Dict[str, Any]] = json.get('resourceSets', [])

        if len(result):
            location = result[0].get(
                'resources', [{}])[0].get('address', {})

            if len(location):
                address = Address()

                if 'addressLine' in location:
                    address.street = location['addressLine']
                elif 'locality' in location:
                    address.settlement = location['locality']
                elif 'adminDistrict2' in location:
                    address.district = location['adminDistrict2']
                elif 'adminDistrict' in location:
                    address.state = location['adminDistrict']
                elif 'countryRegionIso2' in location:
                    address.country = location['countryRegionIso2'].upper()
                elif 'postalCode' in location:
                    address.postcode = location['postalCode']
                elif 'formattedAddress' in location:
                    address.formatted_address = location['formattedAddress']
        return None
