# Запуск проекта с Docker

### docker-compose up --build

# Запуск проекта без Docker

## Предварительные требования

### 1. Установите Python 3.11+
### 2. Установите Node.js 18+
### 3. Установите PostgreSQL
### 4. Создайте базу данных

CREATE DATABASE web_app;
CREATE USER web_user WITH PASSWORD 'web_password';
GRANT ALL PRIVILEGES ON DATABASE web_app TO web_user; 

### 5. Запустить файлы в разных терминалах
cd backend
python run.py

cd frontend
node run.js

# Доступ к приложению
Бэкенд: http://localhost:8000
Фронтенд: http://localhost:3000
Админка: http://localhost:8000/admin (admin/admin)