from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, DeclarativeBase


class BaseTable(DeclarativeBase):
    """Abstract model with declarative base functionality."""
    __abstract__ = True
    __allow_unmapped__ = False

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}"

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
