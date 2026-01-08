from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from dotenv import load_dotenv
import os


load_dotenv()   # Загружаю переменную из .env файла

DATABASE_URL = os.getenv("DATABASE_URL", default="sqlite+aiosqlite:///./library.db")
engine = create_async_engine(DATABASE_URL)
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(MappedAsDataclass, DeclarativeBase):
    pass


async def get_db():
    async with new_session() as session:
        yield session


# Создаем аннотацию для типа для переменной в ф-ии session: SessionDep
# Аннотация говорит: "Это переменная типа AsyncSession, 
# и чтобы её получить, нужно выполнить функцию get_db"
SessionDep = Annotated[AsyncSession, Depends(get_db)]   # Это тип переменной