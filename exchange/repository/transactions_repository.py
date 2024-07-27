from sqlalchemy.ext.asyncio import AsyncSession
from result import Result

from exchange.database.orm.transactions_orm import TransactionORM
from exchange.database.orm.users_orm import UserORM


class TransactionRepository:
    async def create(self, user: UserORM, session: AsyncSession) -> Result:
        (session.add(TransactionORM()))
