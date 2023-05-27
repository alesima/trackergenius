from tracker_genius_geocoder.json_geocoder import JsonGeocoder
from tracker_genius.tracker_genius_geocoder.address import Address
from tracker_genius.tracker_genius_geocoder.address_format import AddressFormat
from typing import Any, Dict, Optional, List


class GoogleGeocoder(JsonGeocoder):
    def __init__(self, key: str = None, language: str = None, address_format: Optional[AddressFormat] = None) -> None:
        super().__init__(self.format_url(key, language), address_format)

    @staticmethod
    def format_url(key: str, language: str) -> str:
        url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=%f,%f'

        if key is not None:
            url += '&key=' + key

        if language is not None:
            url += '&language=' + language

        return url

    def parse_address(self, json: Dict[str, Any]) -> Optional[Address]:
        results: List[Dict[str, Any]] = json.get('results', [])

        if len(results):
            address = Address()

            result: Dict[str, Any] = results[0]
            components: List[Dict[str, Any]] = result.get(
                'address_components', [])

            if 'formatted_address' in result:
                address.formatted_address = result['formatted_address']

            for component in components:
                value = component.get('short_name')

                for type in component.get('types', []):
                    if type == 'street_number':
                        address.house = value
                    elif type == 'route':
                        address.street = value
                    elif type == 'locality':
                        address.settlement = value
                    elif type == 'administrative_area_level_2':
                        address.district = value
                    elif type == 'administrative_area_level_1':
                        address.state = value
                    elif type == 'country':
                        address.country = value
                    elif type == 'postal_code':
                        address.postcode = value
            return address

        return None
