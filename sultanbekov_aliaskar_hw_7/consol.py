import sqlite3


# Функция для выборки всех товаров из БД и вывода их в консоль
def print_all_products():
    # Подключаемся к базе данных
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    try:
        # Выполняем запрос для выборки всех товаров
        cursor.execute('''
            SELECT * FROM products
        ''')

        # Получаем все строки с результатами запроса
        products = cursor.fetchall()

        # Выводим результаты в консоль
        if products:
            print("Список всех товаров:")
            for product in products:
                print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}")
        else:
            print("В базе данных нет товаров.")

    except sqlite3.Error as e:
        print(f"Ошибка при выборке товаров из базы данных: {e}")

    finally:
        # Закрываем соединение с базой данных
        conn.close()


# Пример вызова функции для выборки всех товаров
print_all_products()