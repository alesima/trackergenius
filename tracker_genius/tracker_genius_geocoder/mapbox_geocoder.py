from tracker_genius_geocoder.json_geocoder import JsonGeocoder
from tracker_genius.tracker_genius_geocoder.address import Address
from tracker_genius.tracker_genius_geocoder.address_format import AddressFormat
from typing import Any, Dict, Optional, List


class MapboxGeocoder(JsonGeocoder):
    def __init__(self, key: str = None, address_format: Optional[AddressFormat] = None) -> None:
        super().__init__(self.format_url(key), address_format)

    @staticmethod
    def format_url(key: str = None) -> str:
        return 'https://api.mapbox.com/geocoding/v5/mapbox.places/%f,%f.json?access_token=' + key

    def parse_address(self, json: Dict[str, Any]) -> Optional[Address]:
        features: List[Dict[str, Any]] = json.get('features', [])

        if len(features):
            address = Address()

            most_specific_feature: Dict[str, Any] = features[0]

            if 'place_name' in most_specific_feature:
                address.formatted_address = most_specific_feature['place_name']

            for feature in features:
                value = feature.get('text')

                for type in feature.get('place_type', []):
                    if type == 'address':
                        address.street = value
                    elif type == 'neighborhood':
                        address.suburb = value
                    elif type == 'postcode':
                        address.postcode = value
                    elif type == 'locality':
                        address.settlement = value
                    elif type == 'district' or type == 'place':
                        address.district = value
                    elif type == 'region':
                        address.state = value
                    elif type == 'country':
                        address.country = value
            return Address

        return None
