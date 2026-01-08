from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models.books import BooksModel
from schemas.books import SBookAdd


class BookRepository:

    @classmethod
    async def add_one_book(cls, data: SBookAdd, session: AsyncSession
    ) -> BooksModel:
        # 1. Перевел данные из pydantic в словарь
        book_dict = data.model_dump()

        # 2. Создал объект модели
        book = BooksModel(**book_dict)

        # 3. Добавляем и сохраняяем
        session.add(book)
        await session.commit()
        await session.refresh(book)

        # 4. Вернул обновленный объект
        return book
    
    
    @classmethod
    async def get_all_books(cls, session: AsyncSession) -> list[BooksModel]:
        query = select(BooksModel)
        result = await session.execute(query)
        books_models = result.scalars().all()

        return books_models
    
    
    @classmethod
    async def get_one_book(cls, book_id: int, 
                           session: AsyncSession
    ) -> BooksModel:
        query = select(BooksModel).where(BooksModel.id == book_id)
        result = await session.execute(query)
        book = result.scalars().one_or_none()
    
        return book
    

    @classmethod
    async def update_one_book(cls, book_id: int, 
                              data: SBookAdd, 
                              session: AsyncSession
    ) -> BooksModel:
        book_dict = data.model_dump()
        query = update(BooksModel).where(BooksModel.id == book_id).values(**book_dict).returning(BooksModel)
        result = await session.execute(query)
        await session.commit()

        updated_book = result.scalar_one()
        await session.refresh(updated_book)
        return updated_book
    

    @classmethod
    async def delete_one_book(cls, book_id: int, 
                              session: AsyncSession
    ) -> None:
        query = delete(BooksModel).where(BooksModel.id == book_id)
        await session.execute(query)
        await session.commit()