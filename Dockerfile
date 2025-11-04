FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Минимальные системные зависимости
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости и устанавливаем их
COPY backend/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY backend/ /app/

# Создаем необходимые папки
RUN mkdir -p static media

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]