import datetime


class DateBuilder:
    def __init__(self, time=None, timezone=None):
        self.calendar = datetime.datetime(
            1970, 1, 1, tzinfo=timezone or datetime.timezone.utc)

        if time:
            self.calendar = time.astimezone(timezone or datetime.timezone.utc)

    def set_year(self, year):
        if year < 100:
            year += 2000
        self.calendar = self.calendar.replace(year=year)
        return self

    def set_month(self, month):
        self.calendar = self.calendar.replace(month=month)
        return self

    def set_day(self, day):
        self.calendar = self.calendar.replace(day=day)
        return self

    def set_date(self, year, month, day):
        return self.set_year(year).set_month(month).set_day(day)

    def set_date_reverse(self, day, month, year):
        return self.set_date(year, month, day)

    def set_hour(self, hour):
        self.calendar = self.calendar.replace(hour=hour)
        return self

    def set_minute(self, minute):
        self.calendar = self.calendar.replace(minute=minute)
        return self

    def add_minutes(self, minutes):
        self.calendar += datetime.timedelta(minutes=minutes)
        return self

    def set_second(self, second):
        self.calendar = self.calendar.replace(second=second)
        return self

    def add_seconds(self, seconds):
        self.calendar += datetime.timedelta(seconds=seconds)

    def set_millis(self, millis):
        self.calendar = self.calendar.replace(microsecond=millis)
        return self

    def add_millis(self, millis):
        self.calendar += datetime.timedelta(milliseconds=millis)
        return self

    def set_time(self, hour, minute, second):
        return self.set_hour(hour).set_minute(minute).set_second(second)

    def set_time_reverse(self, second, minute, hour):
        return self.set_time(hour, minute, second)

    def set_time(self, hour, minute, second, millis):
        return self.set_hour(hour).set_minute(minute).set_second(second).set_millis(millis)

    def get_date(self):
        return self.calendar
