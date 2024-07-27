from typing import Optional

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from result import Result, Ok, Err

from exchange.database.orm.users_orm import UserORM


class UserRepository:

    __slots__ = ('_transaction', )

    def __init__(self, transaction: AsyncSession):
        self._transaction = transaction

    async def add(self, user: UserORM) -> Result:
        try:
            self._transaction.add(user)

        except Exception as exc:
            return Err(exc)

        return Ok('success!')

    async def get_by_token(self, token: str):
        return (await self._transaction.execute(
                        select(UserORM)
                        .where(UserORM.token == token))).fetchone()

    async def get_by_name(self, username: str) -> Optional[UserORM]:
        return (await self._transaction.execute(
                        select(UserORM)
                        .where(UserORM.username == username))).fetchone()

    async def set(self, token: str, **values) -> Result:
        try:
            (await self._transaction.execute(
                update(UserORM)
                .where(UserORM.token == token)
                .values(**values)))

        except Exception as exc:
            return Err(exc)

        else:
            return Ok("Success!")

    async def block_user(self, token: str):
        (await self._transaction.execute(
            update(UserORM)
            .where(UserORM.token == token)
            .values(is_blocked=True)))
