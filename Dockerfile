# Вибір базового образу
FROM python:3.10

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо всі файли в контейнер
COPY . .

# Встановлюємо залежності
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Запускаємо основний файл
CMD ["python", "main.py"]
