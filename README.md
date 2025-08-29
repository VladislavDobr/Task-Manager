FastAPI CRUD Application
Описание проекта
Это пример реализации CRUD-приложения на базе FastAPI с использованием SQLAlchemy для работы с базой данных.

## Установка
###  Клонирование репозитория
- git clone <ссылка на репозиторий>

###  Установка зависимостей
- pip install -r requirements.txt

###  Запуск приложения

- uvicorn main:app --reload

### Структура проекта
```
/app
    /models
        __init__.py
        base.py
        task.py
    /schemas
        __init__.py
        task.py
    /crud
        __init__.py
        task.py
    main.py
/tests
    conftest.py
    test_task.py
requirements.txt
README.md
```
###  Основные компоненты
```
# Модели
- Task - основная модель для работы с задачами
- Base - базовая модель для всех ORM-моделей
```
```
# Схемы
- TaskCreate - схема для создания задачи
- TaskUpdate - схема для обновления задачи
- Task - схема для представления задачи в ответе
- CRUD операции
- Создание задачи
- Получение задачи
- Обновление задачи
- Удаление задачи
```
###  Запуск тестов
- pytest

###  Документация
Документация доступна по адресу:

http://127.0.0.1:8000/docs

###  Требования
- Python 3.11+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- PostgreSQL/SQLite

## Контактная информация
Для вопросов и предложений обращайтесь:

Email: dobryakov.vladislav@yandex.ru

GitHub: https://github.com/VladislavDobr

### Автор проекта
**Dobryakov Vladislav** 