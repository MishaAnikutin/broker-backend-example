from enum import Enum


class Purchase(str, Enum):
    long: str = 'long'
    short: str = 'short'


class Actions(str, Enum):
    get: str = 'get'
    refund: str = 'refund'


class Leverage(str, Enum):
    x1: int = 1
    x5: int = 5
    x10: int = 10
    x20: int = 20
