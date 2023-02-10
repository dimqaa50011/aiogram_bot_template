from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

from environs import Env

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = Env()
env.read_env(BASE_DIR / ".env")


@dataclass
class DBConfig:
    POSTGRES_PASSWORD: str = env.str("POSTGRES_PASSWORD")
    POSTGRES_USER: str = env.str("POSTGRES_USER")
    POSTGRES_HOST: str = env.str("POSTGRES_HOST")
    POSTGRES_DB: str = env.str("POSTGRES_DB")
    POSTGRES_PORT: str = env.str("POSTGRES_PORT")
    DB_SCHEMA: str = "postgresql+asyncpg"

    SQLALCHEMY_DATABASE_URI: str = f"{DB_SCHEMA}://{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                                   f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


@dataclass
class BotConfig:
    ADMINS: Tuple = tuple(env.list("ADMINS"))
    BOT_TOKEN: str = env.str("BOT_TOKEN")
    USE_REDIS: bool = env.bool("USE_REDIS")


@dataclass
class Settings:
    db_conf: DBConfig = DBConfig()
    bot_config: BotConfig = BotConfig()
