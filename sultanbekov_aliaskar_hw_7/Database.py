import sqlite3

# Шаг 1: Подключаемся к базе данных или создаем её, если она не существует
conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

# Шаг 2: Модифицируем таблицу products, добавляя поле quantity
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
        price NUMERIC(10, 2) NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')

# Шаг 3: Сохраняем изменения в базе данных
conn.commit()

# Шаг 4: Закрываем соединение с базой данных
conn.close()
