from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Базовый класс для всех моделей ORM в приложении.
    Представляет базовую структуру для декларативного определения моделей.
    """


class Task(Base):
    """
    Модель для представления задачи в системе управления задачами.

    Эта модель описывает структуру задачи, включая её основные атрибуты
    и ограничения на уровне базы данных.
    """
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        doc="Уникальный идентификатор задачи в системе"
    )

    title: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        doc="Заголовок задачи (должен быть уникальным, до 255 символов)"
    )

    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
        doc="Подробное описание задачи (до 1000 символов, может быть пустым)"
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="CREATED",
        doc="Текущий статус задачи "
            "(возможные значения: CREATED, "
            "IN_PROGRESS, DONE)"
    )
