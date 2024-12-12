
import sqlite3
from datetime import datetime


def add_user(name, email, address):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (user_name, user_email, user_address)
        VALUES (?, ?, ?)
    ''', (name, email, address))
    conn.commit()
    conn.close()
    print(f"\nЗаказчик успешно добавлен\n")

def delete_user(user_id):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT user_id FROM users WHERE user_id = {user_id}")
    user_exist = cursor.fetchone()
    if not user_exist:
        print(f"\nЗаказчик не найден\n")
        conn.close()
        return

    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"\nЗаказчик успешно удален\n")

def get_all_users():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def get_user_by_id(user_id):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
    user = cursor.fetchone()
    conn.close()
    return user




def add_product(name, price):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (product_name, product_price)
        VALUES (?, ?)
    ''', (name, price,))
    conn.commit()
    conn.close()
    print(f"\nТовар успешно добавлен\n")


def delete_product(product_id):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT product_id FROM products WHERE product_id = {product_id}")
    product_exist = cursor.fetchone()
    if not product_exist:
        print(f"\nТовар не найден\n")
        conn.close()
        return

    cursor.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
    conn.commit()
    conn.close()
    print(f"\nТовар успешно удален\n")

def get_all_products():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def get_product_by_id(product_id):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM products WHERE product_id = {product_id}")
    product = cursor.fetchone()
    conn.close()
    return product




def add_order(user_id, delivery_address):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT user_id FROM users WHERE user_id = {user_id}")
    user_exist = cursor.fetchone()
    if not user_exist:
        print(f"\nЗаказчик не найден\n")
        conn.close()
        return

    order_date = datetime.now().strftime("%H:%M:%S | %d-%m-%Y")
    cursor.execute('''
            INSERT INTO orders (user_id, order_date, delivery_address)
            VALUES (?, ?, ?)
        ''', (user_id, order_date, delivery_address))
    conn.commit()
    cursor.execute("SELECT order_id FROM orders WHERE user_id = ? AND order_date = ? AND delivery_address = ?", (user_id, order_date, delivery_address))
    order_id = cursor.fetchone()
    conn.close()
    print(f"\nЗаказ успешно создан\nID заказа - {order_id[0]}")

def delete_order(order_id):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT order_id FROM orders WHERE order_id = {order_id}")
    order_exist = cursor.fetchone()
    if not order_exist:
        print(f"\nЗаказ не найден\n")
        conn.close()
        return

    cursor.execute(f"DELETE FROM orders WHERE order_id = {order_id}")
    conn.commit()
    conn.close()
    print(f"\nТовар успешно удален\n")

def get_all_orders():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return orders





def add_order_unit(order_id, product_id, amount):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT order_id FROM orders WHERE order_id = {order_id}")
    order_exist = cursor.fetchone()
    if not order_exist:
        print(f"\nЗаказ не найден\n")
        conn.close()
        return

    cursor.execute(f"SELECT product_id FROM products WHERE product_id = {product_id}")
    product_exist = cursor.fetchone()
    if not product_exist:
        print(f"\nТовар не найден\n")
        conn.close()
        return

    cursor.execute('''
                INSERT INTO order_units (order_id, product_id, quantity)
                VALUES (?, ?, ?)
            ''', (order_id, product_id, amount))
    conn.commit()
    conn.close()
    print(f"\nТовар успешно добавлен в заказ - {order_id}\n")

def delete_order_unit(order_id, product_id):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT order_id FROM orders WHERE order_id = {order_id}")
    order_exist = cursor.fetchone()
    if not order_exist:
        print(f"\nЗаказ не найден\n")
        conn.close()
        return

    cursor.execute(f"SELECT product_id FROM products WHERE product_id = {product_id}")
    product_exist = cursor.fetchone()
    if not product_exist:
        print(f"\nТовар не найден\n")
        conn.close()
        return

    cursor.execute(f"DELETE FROM order_units WHERE order_id = {order_id} AND product_id = {product_id}")
    conn.commit()
    conn.close()
    print(f"\nТовар успешно удален из заказа\n")

def get_all_order_units(order_id):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT order_id FROM orders WHERE order_id = {order_id}")
    order_exist = cursor.fetchone()
    if not order_exist:
        print(f"\nЗаказ не найден\n")
        conn.close()
        return

    cursor.execute(f"SELECT * FROM order_units WHERE order_id = {order_id}")
    units = cursor.fetchall()
    conn.close()
    return units

