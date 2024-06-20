import sqlite3


# Функция для изменения количества товара по id
def update_product_quantity(product_id, new_quantity):
    # Подключаемся к базе данных
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    try:
        # Обновляем количество товара в таблице products
        cursor.execute('''
            UPDATE products
            SET quantity = ?
            WHERE id = ?
        ''', (new_quantity, product_id))

        # Проверяем, была ли хотя бы одна строка изменена
        if cursor.rowcount > 0:
            print(f"Количество товара с id {product_id} успешно обновлено на {new_quantity}.")
        else:
            print(f"Товар с id {product_id} не найден в базе данных.")

        # Коммит изменений в базе данных
        conn.commit()

    except sqlite3.Error as e:
        print(f"Ошибка при обновлении количества товара: {e}")

    finally:
        # Закрываем соединение с базой данных
        conn.close()


# Вызов функции для обновления количества товара
update_product_quantity(1, 50)  # Изменяем количество товара с id=1 на 50