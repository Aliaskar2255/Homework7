import sqlite3


# Функция для удаления товара по id
def delete_product_by_id(product_id):
    # Подключаемся к базе данных
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    try:
        # Удаляем товар из таблицы products по его id
        cursor.execute('''
            DELETE FROM products
            WHERE id = ?
        ''', (product_id,))

        # Проверяем, была ли хотя бы одна строка удалена
        if cursor.rowcount > 0:
            print(f"Товар с id {product_id} успешно удален из базы данных.")
        else:
            print(f"Товар с id {product_id} не найден в базе данных.")

        # Коммит изменений в базе данных
        conn.commit()

    except sqlite3.Error as e:
        print(f"Ошибка при удалении товара: {e}")

    finally:
        # Закрываем соединение с базой данных
        conn.close()


# Пример вызова функции для удаления товара
delete_product_by_id(1)  # Удаляем товар с id=1