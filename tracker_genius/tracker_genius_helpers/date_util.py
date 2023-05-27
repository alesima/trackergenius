import datetime
from typing import List, Dict, Any, Optional


class DateUtil:
    @staticmethod
    def correct_day(guess: datetime.datetime) -> datetime.datetime:
        return DateUtil.correct_date(datetime.datetime.now(), guess, datetime.datetime.now().day)

    @staticmethod
    def correct_date(now: datetime.datetime, guess: datetime.datetime, field: int) -> datetime.datetime:
        if guess > now:
            previous = DateUtil.date_add(guess, field, -1)
            if now - previous < guess - now:
                return previous
        elif guess < now:
            next = DateUtil.date_add(guess, field, 1)
            if next - now < now - guess:
                return next

        return guess

    @staticmethod
    def date_add(date: datetime.datetime, field: int, amount: int) -> datetime.datetime:
        return (date + datetime.timedelta(**{f"{field}s": amount}))

    @staticmethod
    def parse_date(value: str) -> datetime.datetime:
        return datetime.datetime.fromisoformat(value).astimezone()

    @staticmethod
    def format_date(date: datetime.datetime, zoned: bool = True) -> str:
        if zoned:
            return date.isoformat()
        return date.strftime("%Y-%m-%d %H:%M:%S")
