from flask import Flask
import random
from datetime import datetime, timedelta
import os
import re

app = Flask(__name__)

# =========================
# Глобальные переменные
# =========================

# Список машин
CARS_LIST = ["Chevrolet", "Renault", "Ford", "Lada"]

# Список пород кошек
CATS_LIST = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]

# Путь к книге "Война и мир"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

def load_words(file_path):
    """Читает текст и возвращает список слов без знаков препинания"""
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        words = re.findall(r'\b\w+\b', text)
    return words

WORDS_LIST = load_words(BOOK_FILE)

# Счётчик посещений
counter_visits = 0


# =========================
# Endpoints
# =========================

@app.route("/hello_world")
def hello_world():
    return "Привет, мир!"

@app.route("/cars")
def cars():
    return ", ".join(CARS_LIST)

@app.route("/cats")
def cats():
    return random.choice(CATS_LIST)

@app.route("/get_time/now")
def get_time_now():
    current_time = datetime.now()
    return f"Точное время: {current_time}"

@app.route("/get_time/future")
def get_time_future():
    current_time_after_hour = datetime.now() + timedelta(hours=1)
    return f"Точное время через час будет {current_time_after_hour}"

@app.route("/get_random_word")
def get_random_word():
    return random.choice(WORDS_LIST)

@app.route("/counter")
def counter():
    global counter_visits
    counter_visits += 1
    return str(counter_visits)


# =========================
# Запуск сервера
# =========================
if __name__ == "__main__":
    app.run(port=12345, debug=True)
