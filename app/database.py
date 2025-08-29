"""
Настройка подключения к базе данных SQLite и создание сессии
Этот модуль отвечает за создание подключения к базе данных SQLite
и настройку фабрики сессий для работы с ORM.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# URL подключения к базе данных
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Создание движка (engine) для работы с базой данных
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False  # Разрешение одновременного доступа
    }
)

# Создание фабрики сессий с заданными параметрами
SessionLocal = sessionmaker(
    autocommit=False,  # Отключение автоматического коммита
    autoflush=False,   # Отключение автоматического сброса изменений
    bind=engine        # Привязка к созданному движку
)

"""
Параметры сессии:
* autocommit=False: требуется явный вызов commit() для сохранения изменений
* autoflush=False: требуется явный вызов flush() для сброса изменений
* bind=engine: привязка к конкретному движку базы данных
"""
