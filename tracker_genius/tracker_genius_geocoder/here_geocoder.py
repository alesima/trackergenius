from tracker_genius_geocoder.address import Address
from tracker_genius_geocoder.address_format import AddressFormat
from tracker_genius_geocoder.json_geocoder import JsonGeocoder
from typing import Optional, Dict, Any


class HereGeocoder(JsonGeocoder):
    def __init__(self, url: str = None, id: str = None, key: str = None, language: str = None, address_format: Optional[AddressFormat] = None):
        super().__init__(self.format_url(url, id, key, language), address_format)

    @staticmethod
    def format_url(url: str = None, id: str = None, key: str = None, language: str = None) -> str:
        if url is None:
            url = "https://reverse.geocoder.ls.hereapi.com/6.2/reversegeocode.json"
        url += "?mode=retrieveAddresses&maxresults=1"
        url += "&prox=%f,%f,0"

        if id is not None:
            url += "&app_id=" + id

        if key is not None:
            url += "&app_code=" + key
            url += "&api_key" + key

        if language is not None:
            url += "&language=" + language

        return url

    def parse_address(self, json: Dict[str, any]) -> Optional[Address]:
        result = json.get('Response', {}).get('View', [{}])[0].get(
            'Result', [{}])[0].get('Location', {}).get('Address', {})

        if bool(result):
            address = Address()

            if 'Label' in result:
                address.formatted_address = result['Label']

            if 'HouseNumber' in result:
                address.house = result['HouseNumber']
            if 'Street' in result:
                address.street = result['Street']
            if 'City' in result:
                address.settlement = result['City']
            if 'District' in result:
                address.district = result['District']
            if 'State' in result:
                address.state = result['State']
            if 'Country' in result:
                address.country = result['Country']
            if 'PostalCode' in result:
                address.postcode = result['PostalCode']

            return address

        return None
