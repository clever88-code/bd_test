import sqlite3
import unittest
import time

#Тест на устойчивость



# Функция для создания таблицы
def create_table():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT,
                       email TEXT)''')
    conn.commit()
    conn.close()

# Функция для вставки данных в таблицу
def insert_data(username, email):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
    conn.commit()
    conn.close()

# Функция для выборки данных из таблицы
def select_data():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    conn.close()
    return data

# Тестовый класс
class TestSQLiteDatabaseDelay(unittest.TestCase):

    def setUp(self):
        create_table()

    def tearDown(self):
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS users')
        conn.commit()
        conn.close()

    def test_query_delay(self):
        # Вставляем данные
        insert_data('user1', 'user1@example.com')

        # Повторно выполняем запрос на выборку данных 5 раз с измерением задержки
        delays = []
        for _ in range(5):
            start_time = time.time()  # Запускаем таймер
            data = select_data()
            end_time = time.time()  # Останавливаем таймер

            # Вычисляем задержку в миллисекундах
            delay = (end_time - start_time) * 1000
            delays.append(delay)

            # Проверяем, что результат не пустой
            self.assertTrue(len(data) > 0)

        # Выводим задержки для каждого запроса
        print("Delays (in milliseconds):", delays)

if __name__ == '__main__':
    unittest.main()
