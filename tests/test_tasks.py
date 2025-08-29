from sqlalchemy import text
from sqlalchemy.orm import Session

from app.crud import create_task, get_task
from app.models import Task
from app.schemas import TaskCreate


def test_table_exists(test_engine):
    """
    Тест проверки существования таблицы tasks
    """
    with test_engine.connect() as connection:
        result = connection.execute(
            text("""
            SELECT name
            FROM sqlite_master
            WHERE type='table' AND name='tasks'
            """)
        )
        assert result.fetchone() is not None


def test_create_task(db_session: Session):
    """
    Тест создания задачи
    """
    task_data = TaskCreate(
        title="Test Task",
        description="This is a test task",
        status="CREATED"
    )
    created_task = create_task(db_session, task_data)
    assert created_task.title == "Test Task"
    assert created_task.description == "This is a test task"
    assert created_task.status == "CREATED"
    assert created_task.id is not None


def test_get_task(db_session: Session):
    """
    Тест получения задачи по ID
    """
    db_session.query(Task).delete()
    db_session.commit()

    task_data = TaskCreate(
        title="Test Task",
        description="This is a test task",
        status="CREATED"
    )
    created_task = create_task(db_session, task_data)

    fetched_task = get_task(db_session, created_task.id)

    assert fetched_task is not None
    if fetched_task:
        assert fetched_task.title == created_task.title
        assert fetched_task.description == created_task.description
        assert fetched_task.status == created_task.status
        assert fetched_task.id == created_task.id


def test_create_duplicate_task(db_session: Session):
    """
    Тест проверки уникальности заголовка задачи
    """
    task_data = TaskCreate(
        title="Test Task",
        description="This is a test task",
        status="CREATED"
    )
    create_task(db_session, task_data)

    try:
        create_task(db_session, task_data)
        assert False, "Дублирование задачи не должно быть возможно"
    except ValueError as e:
        assert str(e) == "Задача с таким заголовком уже существует"
