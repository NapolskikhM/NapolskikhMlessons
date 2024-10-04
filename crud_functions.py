# aiogram 2.25.1 python 3.10

import sqlite3


def initiate_db():

    # создаем таблицу продукты
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(id INTEGER PRIMARY KEY, 
    title TEXT NOT NULL, description TEXT, price INTEGER NOT NULL)''')
    cursor.execute("CREATE INDEX IF NOT EXISTS index_Products ON Products(id)")

    # заполняем
    vitamins_ = [0, 'A', 'B', 'C', 'D']
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Витамин {vitamins_[i]}', f'Описание {i}', f'{i * 100}'))

    connection.commit()
    connection.close()

    # создаем таблицу пользователи
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY, 
        username TEXT NOT NULL, email TEXT NOT NULL, age INTEGER NOT NULL, balance INTEGER NOT NULL)''')
    cursor.execute("CREATE INDEX IF NOT EXISTS index_Users ON Users(id)")

    # заполняем
    for i in range(1, 5):
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                       (f'newuser {i}', f'newuser{i}@mail.ru', f'{i * 10 + 10}', 1000))

    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE  username=?', (username,))
    check_users = cursor.fetchall()
    if not check_users:
        connection.close()
        return False
    else:
        connection.close()
        return True


def get_all_products():

    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products_ = cursor.fetchall()
    connection.commit()
    connection.close()

    return products_


#initiate_db()
#get_all_products()

