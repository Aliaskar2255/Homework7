import sqlite3


# Функция для добавления товаров в таблицу products
def add_products():
    # Список с различными товарами (product_title, price)
    products = [
        ("Ноутбук Dell XPS 15", 1799.99),
        ("Смартфон iPhone 13 Pro", 1199.00),
        ("Наушники Sony WH-1000XM4", 349.99),
        ("Кофемашина DeLonghi Magnifica", 799.00),
        ("Телевизор LG OLED55C1", 1499.99),
        ("Игровая консоль PlayStation 5", 499.00),
        ("Электрический самокат Xiaomi Mi Electric Scooter Pro 2", 599.99),
        ("Фитнес-браслет Fitbit Charge 5", 179.95),
        ("Камера Canon EOS R6", 2499.00),
        ("Пылесос Dyson V11", 599.00),
        ("Планшет Samsung Galaxy Tab S7", 649.99),
        ("Умные часы Apple Watch Series 7", 399.00),
        ("Гарнитура Logitech G Pro X", 129.99),
        ("Электрический чайник Xiaomi Mi Smart Kettle Pro", 49.99),
        ("Беспроводная колонка JBL Charge 5", 179.95)
    ]

    # Подключаемся к базе данных
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    try:
        # Вставляем каждый товар из списка в таблицу products
        for product in products:
            cursor.execute('''
                INSERT INTO products (product_title, price)
                VALUES (?, ?)
            ''', product)

        # Коммит изменений в базе данных
        conn.commit()
        print("Добавлено 15 различных товаров в таблицу 'products'.")

    except sqlite3.Error as e:
        print(f"Ошибка при добавлении товаров: {e}")

    finally:
        # Закрываем соединение с базой данных
        conn.close()


# Вызов функции для добавления товаров
add_products()