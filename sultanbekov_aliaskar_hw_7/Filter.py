import sqlite3

def print_products_below_price_and_above_quantity_limit(price_limit, quantity_limit):
    try:
        # Подключение к базе данных
        conn = sqlite3.connect('hw.db')
        cursor = conn.cursor()

        # SQL-запрос для выбора товаров
        sql_query = """
                    SELECT product_title, price, quantity 
                    FROM products
                    WHERE price < ? AND quantity > ?
                    """
        cursor.execute(sql_query, (price_limit, quantity_limit))

        # Получение результатов запроса
        products = cursor.fetchall()

        # Вывод результатов в консоль
        if products:
            print("Товары дешевле {} сом и с количеством больше {} шт:".format(price_limit, quantity_limit))
            for product in products:
                print("Название: {}, Цена: {} сом, Количество: {} шт".format(product[1], product[100],
                                                                             product[50]))
        else:
            print("Нет товаров, который вам нужен.")

    except sqlite3.Error as e:
        print("Ошибка при работе с базой данных:", e)

    finally:
        if conn:
            conn.close()

# Пример использования функции
if __name__ == "__main__":
    price_limit = 100
    quantity_limit = 5
    print_products_below_price_and_above_quantity_limit(price_limit, quantity_limit)
