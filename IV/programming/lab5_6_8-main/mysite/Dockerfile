# Используем официальный образ Python в качестве базового образа
FROM python:3.9

# Устанавливаем переменную среды для отключения вывода байт-кодов Python
ENV PYTHONDONTWRITEBYTECODE 1
# Устанавливаем переменную среды для отключения буферизации вывода
ENV PYTHONUNBUFFERED 1

# Создаем директорию для приложения
RUN mkdir /app
# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей в директорию приложения
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем файлы проекта в директорию приложения
COPY . /app/

# Запускаем команду для создания миграций и сбора статических файлов Django
RUN python manage.py makemigrations
RUN python manage.py migrate

# Открываем порт, который будет доступен извне контейнера
EXPOSE 8000

# Запускаем команду для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]

