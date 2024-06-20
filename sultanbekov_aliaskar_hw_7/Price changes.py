import sqlite3


# Функция для изменения цены товара по id
def update_product_price(product_id, new_price):
    # Подключаемся к базе данных
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    try:
        # Обновляем цену товара в таблице products
        cursor.execute('''
            UPDATE products
            SET price = ?
            WHERE id = ?
        ''', (new_price, product_id))

        # Проверяем, была ли хотя бы одна строка изменена
        if cursor.rowcount > 0:
            print(f"Цена товара с id {product_id} успешно обновлена на {new_price}.")
        else:
            print(f"Товар с id {product_id} не найден в базе данных.")

        # Коммит изменений в базе данных
        conn.commit()

    except sqlite3.Error as e:
        print(f"Ошибка при обновлении цены товара: {e}")

    finally:
        # Закрываем соединение с базой данных
        conn.close()


# Пример вызова функции для обновления цены товара
update_product_price(1, 1999.99)  # Изменяем цену товара с id=1 на 1999.99