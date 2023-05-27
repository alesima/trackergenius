class UnitsConverter:
    KNOTS_TO_KPH_RATIO = 0.539957
    KNOTS_TO_MPH_RATIO = 0.868976
    KNOTS_TO_MPS_RATIO = 1.943844
    KNOTS_TO_CPS_RATIO = 0.0194384449
    METERS_TO_FEET_RATIO = 0.3048
    METERS_TO_MILE_RATIO = 1609.34
    MILLLISECONDS_TO_HOURS_RATIO = 3600000
    MILLLISECONDS_TO_MINUTES_RATIO = 60000

    @staticmethod
    def knots_from_kph(value: float) -> float:
        return value * UnitsConverter.KNOTS_TO_KPH_RATIO

    @staticmethod
    def khp_from_knots(value: float) -> float:
        return value / UnitsConverter.KNOTS_TO_KPH_RATIO

    @staticmethod
    def knots_from_mph(value: float) -> float:
        return value * UnitsConverter.KNOTS_TO_MPH_RATIO

    @staticmethod
    def mph_from_knots(value: float) -> float:
        return value / UnitsConverter.KNOTS_TO_MPH_RATIO

    @staticmethod
    def knots_from_mps(value: float) -> float:
        return value * UnitsConverter.KNOTS_TO_MPS_RATIO

    @staticmethod
    def mps_from_knots(value: float) -> float:
        return value / UnitsConverter.KNOTS_TO_MPS_RATIO

    @staticmethod
    def knots_from_cps(value: float) -> float:
        return value * UnitsConverter.KNOTS_TO_CPS_RATIO

    @staticmethod
    def feet_from_meters(value: float) -> float:
        return value * UnitsConverter.METERS_TO_FEET_RATIO

    @staticmethod
    def meters_from_feet(value: float) -> float:
        return value / UnitsConverter.METERS_TO_FEET_RATIO

    @staticmethod
    def miles_from_meters(value: float) -> float:
        return value * UnitsConverter.METERS_TO_MILE_RATIO

    @staticmethod
    def meters_from_miles(value: float) -> float:
        return value / UnitsConverter.METERS_TO_MILE_RATIO

    @staticmethod
    def ms_from_hours(value: float) -> float:
        return value * UnitsConverter.MILLLISECONDS_TO_HOURS_RATIO

    @staticmethod
    def ms_from_minutes(value: float) -> float:
        return value * UnitsConverter.MILLLISECONDS_TO_MINUTES_RATIO
