import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM as PgEnum

from .base import BaseTable
from exchange.common.transactions_enum import Leverage


class UserORM(BaseTable):
    __tablename__ = 'users'

    token: Mapped[str] = mapped_column(sa.String, nullable=False)
    username: Mapped[str] = mapped_column(sa.String, nullable=False)
    balance: Mapped[float] = mapped_column(sa.Float, nullable=False)
    stock_quantity: Mapped[int] = mapped_column(sa.Integer, nullable=False, default=0)
    leverage: Mapped[Leverage] = mapped_column(PgEnum(Leverage, name='Leverage'), nullable=True)
    is_blocked: Mapped[bool] = mapped_column(sa.Boolean, nullable=False, default=0)
