

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


def _required_env(name: str) -> str:
    value = os.getenv(name)
    if value in (None, ""):
        raise RuntimeError(f"Missing required database env var: {name}")
    return value


engine = create_engine(
     "sqlite+libsql:///embedded.db",
     connect_args={
         "sync_url": _required_env("DATABASE_SYNC_URL"),
         "auth_token": _required_env("DATABASE_AUTH_TOKEN"),
     },
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()

