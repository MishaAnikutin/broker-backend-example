from datetime import datetime

from fastapi import APIRouter

from exchange.models.stock_model import Stock
from exchange.service.stocks_data_service import StocksService

stock_router = APIRouter(
    prefix="/stocks",
    tags=["stocks"]
)


@stock_router.get("/price/")
async def price(token: str) -> Stock:
    return await StocksService(token=token).get()


# @broker_router.get("/data/")
# async def data(token: str, date_end: datetime, date_start: datetime = None):
#     return
