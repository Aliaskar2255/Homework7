import sqlite3


# Функция для поиска товаров по частичному совпадению с названием
def search_products_by_name(search_term):
    # Подключаемся к базе данных
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    try:
        # Выполняем запрос для поиска товаров по частичному совпадению с названием
        cursor.execute('''
            SELECT * FROM products
            WHERE product_title LIKE ?
        ''', ('%' + search_term + '%',))

        # Получаем все строки с результатами запроса
        products = cursor.fetchall()

        # Выводим результаты в консоль
        if products:
            print(f"Результаты поиска по запросу '{search_term}':")
            for product in products:
                print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}")
        else:
            print(f"Нет товаров, соответствующих запросу '{search_term}'.")

    except sqlite3.Error as e:
        print(f"Ошибка при поиске товаров по названию: {e}")

    finally:
        # Закрываем соединение с базой данных
        conn.close()


# Пример вызова функции для поиска товаров по частичному совпадению с названием
search_term = "Наушники"
search_products_by_name(search_term)