import os

from dotenv import load_dotenv
from dataclasses import dataclass
from sqlalchemy.engine import URL


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


@dataclass
class DatabaseConfig:
    DB_HOST = os.environ.get("POSTGRES_HOST", "localhost")
    DB_PORT = os.environ.get("POSTGRES_PORT", 5432)
    DB_NAME = os.environ.get("POSTGRES_DATABASE", "postgres")
    DB_USER = os.environ.get("POSTGRES_USER", "postgres")
    DB_PASS = os.environ.get("POSTGRES_PASSWORD", "postgres")

    DATABASE_URL = URL.create(
        drivername="postgresql+asyncpg",
        username=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )

    DATABASE_URL_STRING = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

@dataclass
class AppConfig:
    """Bot configuration."""

    title = "Fake Stock Exchange"
    description = "Фейковый REST API для работы с биржей акций"
    version = "1.0"


@dataclass
class ExchangeConfig:
    start_balance = 100_000


@dataclass
class Configuration:
    db = DatabaseConfig()
    app = AppConfig()
    exchange = ExchangeConfig()


configuration = Configuration()
