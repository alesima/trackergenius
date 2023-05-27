import logging
import requests
from django.core.cache import cache
from tracker_genius_geocoder.address import Address
from tracker_genius_geocoder.address_format import AddressFormat
from tracker_genius_geocoder.geocoder import Geocoder
from typing import Optional, Callable, Any, Dict


logger = logging.getLogger(__name__)


class JsonGeocoder(Geocoder):
    def __init__(self, url: str, address_format: Optional[AddressFormat] = None) -> None:
        self.url = url
        self.address_format = address_format
        self.statitics_manager = None

    def set_statitics_manager(self, statitics_manager: Callable):
        self.statitics_manager = statitics_manager

    def read_value(self, object: Dict[str, Any], key: str) -> Optional[Any]:
        if key in object and object[key] is not None:
            return object[key]
        return None

    def handle_response(self, latitude: float, longitude: float, json: Dict[str, Any], callback: Geocoder.ReverseGeocoderCallback = None):
        address: Optional[Address] = self.parse_address(json)
        if address is not None:
            formatted_address = self.address_format.format(
                address) if self.address_format else None
            if formatted_address is not None:
                if cache.get(f"{latitude}:{longitude}") is None:
                    cache.set(f"{latitude}:{longitude}", formatted_address)
                if callback is not None:
                    callback.on_success(formatted_address)
                return formatted_address
        else:
            msg = f"Empty address. Error: {self.parse_error(json)}"
            if callback is not None:
                callback.on_error(msg)
            else:
                logger.warning(msg)

        return None

    def get_address(self, latitude: float, longitude: float, callback: Geocoder.ReverseGeocoderCallback = None) -> Optional[str]:
        if cache.get(f"{latitude}:{longitude}") is not None:
            cached_address: str = cache.get(f"{latitude}:{longitude}")
            if callback:
                callback.on_success(cached_address)
            return cached_address

        if self.statitics_manager:
            self.statitics_manager.register_geocoder_request()

        url = self.url.format(latitude, longitude)
        response = requests.get(url)

        if response.status_code == 200:
            json = response.json()
            return self.handle_response(latitude, longitude, json, callback)
        else:
            logger.warning("Geocoder network error")

        return None

    def parse_address(self, json: Dict[str, Any]) -> Optional[Address]:
        return None

    def parse_error(self, json: Dict[str, Any]):
        return None
