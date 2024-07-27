from result import Err, Ok, Result

from exchange.database.orm.users_orm import UserORM
from exchange.database.session import Transaction
from exchange.models.stock_model import Stock
from exchange.models.user_model import User
from exchange.repository import UserRepository
from exchange.repository.stocks_repository import StockRepository

from exchange.settings import configuration


class StocksService:

    __slots__ = ('_token', )

    def __init__(self, token: str = None):
        self._token = token

    async def get(self) -> Result:
        async with Transaction() as transaction:
            users = await UserRepository(transaction).get_by_token(self._token)

            if users is None:
                return Err('Invalid Token')

            stocks = StockRepository(transaction)

            stock_data = await stocks.get()

            return Stock(
                date=stock_data.date,
                price_max=stock_data.price_max,
                price_min=stock_data.price_min,
                price_close=stock_data.price_close,
                price_open=stock_data.price_open
            )
