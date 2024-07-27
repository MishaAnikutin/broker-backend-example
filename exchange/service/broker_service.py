from result import Err, OkErr

from exchange.common.transactions_enum import Leverage
from exchange.database.session import Transaction
from exchange.repository import StockRepository, UserRepository


# TODO: добавить декораторов для читаемости
class BrokerService:

    __slots__ = ('_token', 'users', 'stocks')

    def __init__(self, token: str):
        self._token = token

    async def long_buy(self, value: int, leverage: Leverage) -> OkErr:
        async with Transaction() as transaction:
            users = UserRepository(transaction=transaction)
            stocks = StockRepository(transaction=transaction)

            if (user := await users.get_by_token(token=self._token)) is None:
                return Err("Пользователя не существует")

            if leverage != user.leverage and user.leverage is not None:
                return Err("Нельзя менять плечо от транзакции к транзакции")

            balance = user.balance
            new_quantity = user.stock_quantity + value
            price = await stocks.get_open()

            if (new_balance := balance - leverage.value * value * price) < 0:
                return Err('Нехватает денег')

            return await users.set(
                transaction=transaction,
                new_balance=new_balance,
                leverage=leverage,
                stock_quantity=new_quantity
            )

    async def long_sell(self, value: int) -> OkErr:
        async with Transaction() as transaction:
            users = UserRepository(transaction=transaction)
            stocks = StockRepository(transaction=transaction)

            if (user := await users.get_by_token(token=self._token)) is None:
                return Err("Пользователя не существует")

            balance = user.balance
            leverage = user.leverage
            stock_quantity = user.stock_quantity

            if stock_quantity < 0:
                return Err("В шорте нельзя продавать акции")

            new_value = stock_quantity - value
            price = await stocks.get_close()
            new_balance = balance + value * price * leverage
            new_leverage = leverage if new_value != 0 else None

            return await users.set(
                transaction=transaction,
                new_balance=new_balance,
                stock_quantity=new_value,
                leverage=new_leverage
            )

    async def take_short(self, value: int, leverage: Leverage) -> OkErr:
        async with Transaction() as transaction:
            users = UserRepository(transaction=transaction)
            stocks = StockRepository(transaction=transaction)

            if (user := await users.get_by_token(token=self._token)) is None:
                return Err("Пользователя не существует")

            if leverage != user.leverage and user.leverage is not None:
                return Err("Нельзя менять плечо от транзакции к транзакции")

            price = await stocks.get_open()
            balance = user.balance
            new_quantity = user.stock_quantity - value
            new_balance = balance + value * price * leverage

            if new_quantity < -100:  # TODO: лучше брать из settings.py
                return Err("Максимум можно встать в шорт на 100 акциях")

            return await users.set(
                transaction=transaction,
                new_balance=new_balance,
                leverage=leverage,
                stock_quantity=new_quantity
            )

    async def refund_short(self, value: int) -> OkErr:
        async with Transaction() as transaction:
            users = UserRepository(transaction=transaction)
            stocks = StockRepository(transaction=transaction)

            if (user := await users.get_by_token(token=self._token)) is None:
                return Err("Пользователя не существует")

            price = await stocks.get_close()
            leverage = user.leverage

            new_quantity = user.stock_quantity + value
            new_balance = user.balance - value * price * leverage
            new_leverage = leverage if new_quantity != 0 else None

            return await users.set(
                token=self._token,
                new_balance=new_balance,
                leverage=new_leverage,
                stock_quantity=new_quantity
            )
