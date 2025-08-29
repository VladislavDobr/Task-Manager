# Используем официальный образ Python как базовый
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY . .

# Устанавливаем переменные окружения
ENV DATABASE_URL=postgresql://user:password@db:5432/mydatabase
ENV SECRET_KEY=your_secret_key

# Открываем порт
EXPOSE 8000

# Определяем команду запуска
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
