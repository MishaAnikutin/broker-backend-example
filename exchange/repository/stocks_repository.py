from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from exchange.database.orm.stocks_orm import StockORM
from exchange.database.orm.transactions_orm import TransactionORM
from sqlalchemy import and_, func


class StockRepository:

    __slots__ = ('_transaction', )

    start_date = '2024-07-24'

    def __init__(self, transaction: AsyncSession):
        self._transaction = transaction

    async def get(self) -> StockORM:
        (await self._transaction.execute(
            select(StockORM)
            # .where(StockORM.date)
            .limit(1))).fetchone()
