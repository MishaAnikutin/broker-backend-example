from fastapi import APIRouter

from exchange.service.broker_service import BrokerService
from exchange.models.broker_model import LongRequest, ShortRequest


broker_router = APIRouter(
    prefix="/broker",
    tags=["Broker"]
)


@broker_router.post("/long/buy")
async def long_buy(request: LongRequest) -> str:
    return ("success!" if
            (result := (await BrokerService(token=request.token)
                        .long_buy(value=request.value, leverage=request.leverage))
             .is_ok())
            else result.value)


@broker_router.post("/long/sell")
async def long_sell(request: LongRequest) -> str:
    return ("success!" if
            (result := (await BrokerService(token=request.token)
                        .long_sell(value=request.value))
             .is_ok())
            else result.value)


@broker_router.post("/short/take")
async def take_short(request: ShortRequest):
    return ("success!" if
            (result := (await BrokerService(token=request.token)
                        .take_short(value=request.value, leverage=request.leverage))
             .is_ok())
            else result.value)


@broker_router.post("/short/refund")
async def refund_short(request: ShortRequest):
    return ("success!" if
            (result := (await BrokerService(token=request.token)
                        .refund_short(value=request.value))
             .is_ok())
            else result.value)
