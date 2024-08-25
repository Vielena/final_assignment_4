# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в контейнер
COPY data.csv .
COPY app.py .

# Устанавливаем необходимые библиотеки
RUN pip install pandas

# Запускаем приложение
CMD ["python", "app.py"]
