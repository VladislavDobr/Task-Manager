import os
import sys
import time
from pathlib import Path

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.models import Base, Task


@pytest.fixture(autouse=True)
def clean_db(db_session: Session):
    """
    Фикстура для очистки базы данных перед каждым тестом
    Удаляет все записи из таблицы задач перед и после выполнения теста
    """
    db_session.query(Task).delete()
    db_session.commit()
    yield
    db_session.query(Task).delete()
    db_session.commit()


@pytest.fixture(scope='session')
def test_engine():
    """
    Фикстура для создания тестовой базы данных
    Создает SQLite базу данных для тестирования
    и удаляет её после завершения тестов
    """
    test_db_path = 'test.db'
    if os.path.exists(test_db_path):
        os.remove(test_db_path)

    engine = create_engine(
        'sqlite:///test.db',
        connect_args={"check_same_thread": False}
    )

    Base.metadata.create_all(bind=engine)

    try:
        yield engine
    finally:
        engine.dispose()
        Base.metadata.drop_all(bind=engine)
        time.sleep(1)
        attempts = 5
        while attempts > 0:
            try:
                if os.path.exists(test_db_path):
                    os.remove(test_db_path)
                break
            except PermissionError:
                time.sleep(0.5)
                attempts -= 1
            except OSError as e:
                print(f"Ошибка при удалении файла: {e}")
                attempts -= 1
        else:
            print(
                f"Не удалось удалить файл {test_db_path} "
                f"после {attempts} попыток"
            )


@pytest.fixture
def db_session(test_engine):
    """
    Фикстура для создания сессии базы данных
    Создает новую сессию для каждого теста
    и обеспечивает её корректное закрытие
    """
    Session = sessionmaker(bind=test_engine)
    session = Session()
    try:
        yield session
    finally:
        session.rollback()
        session.close()
