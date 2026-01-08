Учебное API для управления библиотекой книг, построенное на FastAPI с использованием асинхронной SQLAlchemy и SQLite.

## Описание

Это REST API позволяет выполнять основные CRUD операции с книгами:
- Создание новой книги
- Получение списка всех книг
- Получение информации о конкретной книге по ID
- Обновление информации о книге по ID
- Удаление книги по ID

## Технологии

- **FastAPI** - современный веб-фреймворк для создания API
- **SQLAlchemy 2.0** - асинхронный ORM для работы с базой данных
- **SQLite** - легковесная реляционная база данных
- **Uvicorn** - ASGI сервер для запуска приложения
- **Pydantic v2** - валидация данных и схемы
- **Docker** - контейнеризация приложения
- **Полный CRUD** - операции создания, чтения, обновления, удаления

## Требования

- Python 3.8+
- Virtual environment (рекомендуется)

## Установка

1. Клонируйте репозиторий:
   ```bash
   mkdir library
   cd library
   git clone <repository-url>
   ```

2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   ```

3. Активируйте виртуальное окружение:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
5. Создайте файл .env на основе .env.example:
   ```bash
   cp .env.example .env
   ```

## Запуск приложения
### Запуск через Uvicorn
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### С использованием Docker
#### Запуск контейнеров:
```bash
docker compose up 
```

#### Остановка контейнеров:
```bash
docker compose down
```

Приложение будет доступно по адресу: http://localhost:8000

## API Документация

FastAPI автоматически генерирует интерактивную документацию:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://0.0.0.0:8000/redoc

## Структура проекта

```
library-api/
├── main.py                 # Точка входа в приложение
├── database.py             # Настройка подключения к БД
├── requirements.txt        # Зависимости проекта
├── .gitignore              # Игнорируемые файлы
├── repository.py           # Слой доступа к данным БД
├── Dockerfile              # Описание образа
├── docker-compose.yml      # Для запуска сервисов
├── .env.example            # Пример .env файла
├── models/
│   ├── __init__.py
│   └── books.py            # Модель данных книги для БД
├── schemas/
│   ├── __init__.py
│   └── books.py            # Pydantic схемы для валидации
├── routers/
│   ├── __init__.py
│   └── books.py            # Маршруты для книг
└── 
```


## Эндпоинты API

| Метод | Путь         | Описание                  |
|-------|--------------|---------------------------|
| POST  | /books       | Создание новой книги      |
| GET   | /books       | Получение списка всех книг|
| GET   | /books/{id}  | Получение книги по ID     |
| PUT   | /books/{id}  | Обновление книги по ID    |
| DELETE| /books/{id}  | Удаление книги по ID      |

## Примеры использования

### Создание книги
```bash
curl -X POST "http://0.0.0.0:8000/books" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Война и мир",
    "author": "Лев Толстой",
    "year": 1869,
    "pages": 1225,
    "is_read": false
  }'
```

### Получение всех книг
```bash
curl -X GET "http://0.0.0.0:8000/books"
```

### Получение книги по ID
```bash
curl -X GET "http://0.0.0.0:8000/books/1"
```

### Обновление книги
```bash
curl -X PUT "http://0.0.0.0:8000/books/1" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Война и мир",
    "author": "Лев Николаевич Толстой",
    "year": 1869,
    "pages": 1225,
    "is_read": true
  }'
```

### Удаление книги
```bash
curl -X DELETE "http://0.0.0.0:8000/books/1"
```


## База данных

Проект использует SQLite базу данных, которая автоматически создается при первом запуске приложения в файле `library.db`.


## Лицензия

Этот проект предназначен для образовательных целей.
