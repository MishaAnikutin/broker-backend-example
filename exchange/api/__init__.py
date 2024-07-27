from fastapi import APIRouter

from .user_handlers import user_router
from .broker_handlers import broker_router
from .stocks_handler import stock_router


router = APIRouter(prefix='/api')

router.include_router(user_router)
router.include_router(broker_router)
router.include_router(stock_router)
