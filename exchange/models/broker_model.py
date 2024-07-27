from pydantic import BaseModel, Field

from exchange.common.transactions_enum import Leverage, Actions


class LongRequest(BaseModel):
    token: str
    value: int
    leverage: Leverage = Field(default=Leverage.x1)


class ShortRequest(BaseModel):
    token: str
    value: int
    leverage: Leverage = Field(default=Leverage.x1)
