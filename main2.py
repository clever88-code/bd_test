import sqlite3

#создание 2 таблиц и заполнения их данными



# Функция для создания таблиц
def create_tables():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT,
                       email TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       price REAL)''')
    conn.commit()
    conn.close()

# Функция для вставки данных в таблицу пользователей
def insert_user(username, email):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
    conn.commit()
    conn.close()

# Функция для вставки данных в таблицу продуктов
def insert_product(name, price):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
    conn.commit()
    conn.close()

# Функция для выборки данных из таблицы пользователей
def select_users():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    conn.close()
    return data

# Функция для выборки данных из таблицы продуктов
def select_products():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    data = cursor.fetchall()
    conn.close()
    return data

if __name__ == '__main__':
    create_tables()

    # Вставляем данные в таблицу пользователей
    insert_user('user1', 'user1@example.com')
    insert_user('user2', 'user2@example.com')

    # Вставляем данные в таблицу продуктов
    insert_product('Product A', 10.99)
    insert_product('Product B', 19.99)

    # Выводим данные из таблицы пользователей
    users_data = select_users()
    print("Users:")
    for user in users_data:
        print(user)

    # Выводим данные из таблицы продуктов
    products_data = select_products()
    print("\nProducts:")
    for product in products_data:
        print(product)
