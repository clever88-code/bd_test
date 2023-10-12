import sqlite3
import unittest

# Функция для тестирования записи и удаление данных



# Функция для создания таблицы
def create_table():
    # Устанавливаем соединение с базой данных и создаем объект курсора
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    
    # Создаем таблицу "users" (если ее еще не существует)
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT,
                       email TEXT)''')
    
    # Применяем изменения в базе данных
    conn.commit()
    
    # Закрываем соединение с базой данных
    conn.close()

# Функция для вставки данных в таблицу
def insert_data(username, email):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    
    # Вставляем данные (username и email) в таблицу "users"
    cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
    
    # Применяем изменения в базе данных
    conn.commit()
    
    # Закрываем соединение с базой данных
    conn.close()

# Функция для выборки данных из таблицы
def select_data():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    
    # Выполняем SQL-запрос для выборки всех данных из таблицы "users"
    cursor.execute('SELECT * FROM users')
    
    # Получаем результат запроса
    data = cursor.fetchall()
    
    # Закрываем соединение с базой данных
    conn.close()
    
    return data

# Функция для удаления данных из таблицы
def delete_data(user_id):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    
    # Выполняем SQL-запрос для удаления записи с указанным идентификатором из таблицы "users"
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    
    # Применяем изменения в базе данных
    conn.commit()
    
    # Закрываем соединение с базой данных
    conn.close()

# Тестовый класс
class TestSQLiteDatabase(unittest.TestCase):

    def setUp(self):
        # Вызываем функцию create_table() перед каждым тестом для создания таблицы
        create_table()

    def tearDown(self):
        # Удаляем тестовую базу данных после каждого теста
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS users')
        conn.commit()
        conn.close()

    def test_insert_and_select_data(self):
        # Вставляем данные и проверяем, что они корректно сохранены в базе данных
        insert_data('user1', 'user1@example.com')
        insert_data('user2', 'user2@example.com')

        # Выбираем данные из базы данных
        data = select_data()

        # Проверяем результаты
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], (1, 'user1', 'user1@example.com'))
        self.assertEqual(data[1], (2, 'user2', 'user2@example.com'))

    def test_delete_data(self):
        # Вставляем данные и затем удаляем одну из записей
        insert_data('user1', 'user1@example.com')
        insert_data('user2', 'user2@example.com')

        delete_data(1)

        # Выбираем данные из базы данных
        data = select_data()

        # Проверяем результаты
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0], (2, 'user2', 'user2@example.com'))

if __name__ == '__main__':
    # Запуск тестового класса
    unittest.main()
