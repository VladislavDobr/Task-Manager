import logging
from typing import Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models import Task
from app.schemas import TaskCreate, TaskUpdate

logger = logging.getLogger(__name__)


def create_task(db: Session, task: TaskCreate) -> Task:
    """
    Создание новой задачи в базе данных

    Args:
        db (Session): сессия базы данных
        task (TaskCreate): данные для создания задачи

    Returns:
        Task: созданная задача

    Raises:
        ValueError: если задача с таким заголовком уже существует
    """
    try:
        if db.query(Task).filter(Task.title == task.title).first():
            raise ValueError("Задача с таким заголовком уже существует")

        db_task = Task(
            title=task.title,
            description=task.description,
            status=task.status
        )
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        logger.info("Задача успешно создана: %s", db_task.id)
        return db_task

    except IntegrityError as e:
        db.rollback()
        raise ValueError("Задача с таким заголовком уже существует") from e

    except ValueError as e:
        db.rollback()
        raise e

    except Exception as e:
        db.rollback()
        raise ValueError(
            f"Произошла ошибка при создании задачи: {str(e)}"
        ) from e


def get_task(db: Session, task_id: int) -> Optional[Task]:
    """
    Получение задачи по ID

    Args:
        db (Session): сессия базы данных
        task_id (int): ID задачи

    Returns:
        Optional[Task]: найденная задача или None
    """
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(
    db: Session, task_id: int, update_data: TaskUpdate
) -> Optional[Task]:
    """
    Обновление существующей задачи

    Args:
        db (Session): сессия базы данных
        task_id (int): ID задачи для обновления
        update_data (TaskUpdate): данные для обновления

    Returns:
        Optional[Task]: обновленная задача или None
    """
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        # Преобразуем в словарь только те поля, которые нужно обновить
        update_dict = update_data.dict(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(db_task, key, value)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    return None


def delete_task(db: Session, task_id: int) -> None:
    """
    Удаление задачи по ID

    Args:
        db (Session): сессия базы данных
        task_id (int): ID задачи для удаления
    """
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
