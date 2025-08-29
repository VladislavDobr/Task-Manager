from typing import Optional

from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    """
    Базовая модель для представления задачи

    Атрибуты:
        title: Заголовок задачи (обязательное поле)
        description: Описание задачи (опционально)
        status: Текущий статус задачи (обязательное поле)
    """
    title: str
    description: Optional[str] = None
    status: str

    model_config = ConfigDict(
        from_attributes=True
    )


class TaskCreate(TaskBase):
    """
    Модель для создания новой задачи

    Наследует все поля от TaskBase и не добавляет дополнительных полей
    """


class TaskUpdate(BaseModel):
    """
    Модель для обновления существующей задачи

    Все поля опциональны, можно обновлять только нужные поля
    """
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]


class Task(TaskBase):
    """
    Модель для представления полной информации о задаче

    Расширяет TaskBase, добавляя идентификатор задачи

    Атрибуты:
        id: Уникальный идентификатор задачи
    """
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )
