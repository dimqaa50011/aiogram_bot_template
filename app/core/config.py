from pathlib import Path
from typing import Tuple
from dataclasses import dataclass

from pydantic import BaseSettings, PostgresDsn, validator
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

@dataclass
class BotConfig:
    ADMINS: Tuple = tuple(env.list("ADMINS"))
    BOT_TOKEN: str = env.str("BOT_TOKEN")
    USE_REDIS: bool = env.bool("USE_REDIS")


@dataclass
class Settings:
    db_conf: DBConfig = DBConfig()
    bot_config: BotConfig = BotConfig()