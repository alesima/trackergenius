class Address:
    def __init__(self):
        self._postcode = None
        self._country = None
        self._state = None
        self._district = None
        self._settlement = None
        self._suburb = None
        self._street = None
        self._house = None
        self._formatted_address = None

    @property
    def postcode(self):
        return self._postcode

    @postcode.setter
    def postcode(self, value):
        self._postcode = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value

    @property
    def settlement(self):
        return self._settlement

    @settlement.setter
    def settlement(self, value):
        self._settlement = value

    @property
    def suburb(self):
        return self._suburb

    @suburb.setter
    def suburb(self, value):
        self._suburb = value

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, value):
        self._house = value

    @property
    def formatted_address(self):
        return self._formatted_address

    @formatted_address.setter
    def formatted_address(self, value):
        self._formatted_address = value
