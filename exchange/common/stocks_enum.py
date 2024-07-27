from enum import Enum


class Timedelta(str, Enum):
    second_5: str = '5-sec'
    second_30: str = '30-sec'
    minute: str = 'min'
    minute_5: str = '5-min'
