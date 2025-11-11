import os
import sys
import subprocess


def main():
    # Активируем виртуальное окружение (если есть)
    if os.path.exists('venv'):
        if sys.platform == "win32":
            activate_script = os.path.join('venv', 'Scripts', 'activate.bat')
            subprocess.call([activate_script], shell=True)
        else:
            activate_script = os.path.join('venv', 'bin', 'activate')
            subprocess.call(['source', activate_script], shell=True)

    # Устанавливаем зависимости
    print("Установка зависимостей...")
    #subprocess.call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

    # Применяем миграции
    print("Применение миграций...")
    subprocess.call([sys.executable, 'manage.py', 'migrate'])

    # Загружаем тестовые данные
    print("Загрузка тестовых данных...")
    subprocess.call([sys.executable, 'manage.py', 'seed_data'])

    # Запускаем сервер
    print("Запуск сервера разработки...")
    subprocess.call([sys.executable, 'manage.py', 'runserver', '0.0.0.0:8000'])


if __name__ == '__main__':
    main()