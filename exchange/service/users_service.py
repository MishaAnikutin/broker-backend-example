import secrets
from typing import Optional

from result import Err, Ok, Result

from exchange.database.orm.users_orm import UserORM
from exchange.database.session import Transaction
from exchange.models.user_model import User
from exchange.repository.users_repository import UserRepository

from exchange.settings import configuration


class UserService:

    __slots__ = ('_token', )

    def __init__(self, token: str = None):
        self._token = token

    async def create_user(self, username: str) -> Result:
        self._token = await self._generate_token()

        async with Transaction() as transaction:
            users = UserRepository(transaction)

            if await users.get_by_name(username) is not None:
                return Err("Пользователь уже есть")

            return await users.add(
                user=UserORM(
                    token=self._token,
                    username=username,
                    balance=configuration.exchange.start_balance,
                    stock_quantity=0,
                    is_blocked=False
                )
            )

    async def get_user(self) -> Ok[User] | Err:
        async with Transaction() as transaction:
            users = await UserRepository(transaction).get_by_token(self._token)

            if users is None:
                return Err('Invalid Token')

            return Ok(User(
                username=users[0].username,
                token=users[0].token,
                balance=users[0].balance,
                stock_quantity=users[0].stock_quantity,
                leverage=users[0].leverage
            ))

    async def check_is_blocked(self) -> Result:
        async with Transaction() as transaction:
            return (Ok(user.is_blocked)
                    if (user := await UserRepository(transaction).get_by_token(self._token))
                    is not None
                    else Err("Пользователя не существует"))

    @staticmethod
    async def _generate_token() -> str:
        return secrets.token_hex(nbytes=20)  #TODO: лучше брать длинну из settings
