from fastapi import FastAPI
from routers.books import router as book_router
from contextlib import asynccontextmanager
from database import engine, Model
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # КОД ПРИ СТАРТЕ
    logger.info("Создание таблиц БД...")
    # Создаем все таблицы через движок
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

    logger.info("База данных готова к работе")

    yield   # Разделяю старт и финиш

    # Код на выключении
    logger.info("Выключение сервера")


app = FastAPI(lifespan=lifespan)
app.include_router(book_router)