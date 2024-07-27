from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from exchange.common.stocks_enum import Timedelta


class Stock(BaseModel):
    price_max: float
    price_min: float
    price_open: float
    price_close: float
    timedelta: Timedelta = Field(default=5)
    date: Optional[datetime] = Field(default=None)
