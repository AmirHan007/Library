from fastapi import APIRouter, status, HTTPException

from database import SessionDep
from schemas.books import SBook, SBookAdd
from repository import BookRepository


router = APIRouter(prefix='/books', tags=['Книги'])

@router.post("", response_model=SBook, status_code=status.HTTP_201_CREATED)
async def create_book(book: SBookAdd, session: SessionDep) -> SBook:
    book_model = await BookRepository.add_one_book(book, session)
    return book_model


@router.get("", response_model=list[SBook], status_code=status.HTTP_200_OK)
async def get_all_books(session: SessionDep) -> list[SBook]:
    books = await BookRepository.get_all_books(session)
    return books


@router.get("/{id}", response_model=SBook, status_code=status.HTTP_200_OK)
async def get_one_book(id: int, session: SessionDep) -> SBook:
    book = await BookRepository.get_one_book(id, session)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Книга не найдена')
    
    return book


@router.put("/{id}", response_model=SBook, status_code=status.HTTP_200_OK)
async def update_one_book(id: int, book: SBookAdd, session: SessionDep) -> SBook:
    old_book = await BookRepository.get_one_book(id, session)
    if not old_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Книга с id={id} не найдена")
    
    updated_book = await BookRepository.update_one_book(id, book, session)
    return updated_book


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def del_one_book(id: int, session: SessionDep) -> dict:
    book_to_del = await BookRepository.get_one_book(id, session)
    if not book_to_del:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Книга с id={id} не найдена")
    
    await BookRepository.delete_one_book(id, session)
    return {"msg":"book is deleted"}