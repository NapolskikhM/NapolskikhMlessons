# aiogram 2.25.1 python 3.10
import sqlite3


def initiate_db():

    # создаем таблицу
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

