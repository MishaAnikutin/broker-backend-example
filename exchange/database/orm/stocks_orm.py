from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseTable


class StockORM(BaseTable):
    __tablename__ = 'stocks'

    price_open: Mapped[float] = mapped_column(sa.Float, nullable=False)
    price_close: Mapped[float] = mapped_column(sa.Float, nullable=False)
    price_max: Mapped[float] = mapped_column(sa.Float, nullable=False)
    price_min: Mapped[float] = mapped_column(sa.Float, nullable=False)
    date: Mapped[datetime] = mapped_column(sa.DateTime, nullable=False)
