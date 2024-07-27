from typing import Optional

from pydantic import BaseModel

from exchange.common.transactions_enum import Leverage


class User(BaseModel):
    username: str
    token: str
    balance: float
    stock_quantity: int
    leverage: Optional[Leverage]
