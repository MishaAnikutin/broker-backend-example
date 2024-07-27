from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM as PgEnum

from .base import BaseTable
from exchange.common.transactions_enum import Leverage, Purchase, Actions


class TransactionORM(BaseTable):
    __tablename__ = 'transactions'

    date: Mapped[datetime] = mapped_column(sa.DateTime, nullable=False)
    token: Mapped[str] = mapped_column(sa.String, nullable=False)
    purchase: Mapped[Purchase] = mapped_column(PgEnum(Purchase, name='Purchase'), nullable=False)
    action: Mapped[Actions] = mapped_column(PgEnum(Actions, name='Actions'), nullable=False)
    leverage: Mapped[Leverage] = mapped_column(PgEnum(Leverage, name='Leverage'), nullable=False)
    price: Mapped[float] = mapped_column(sa.Float, nullable=False)
    value: Mapped[int] = mapped_column(sa.Integer, nullable=False)
