
from init_db import init_db
from db_functions import *

init_db()
while True:
    print("Выберете действие\n"
          "1-Добавить заказчика\n"
          "2-Удалить заказчика\n"
          "3-Показать всех заказчиков\n"
          "\n"
          "4-Добавить товар\n"
          "5-Удалить товар\n"
          "6-Показать все товары\n"
          "\n"
          "7-Добавить заказ\n"
          "8-Удалить заказ\n"
          "9-Показать все заказы\n"
          "\n"
          "10-Добавить товар в заказ\n"
          "11-Удалить товар из заказа\n"
          "12-Показать все товары в заказе\n")

    user_input = int(input("Действие: "))
    print()

    match(user_input):
        case 1:
            print("######################################\n")
            name = input("Введите имя заказчика - ")
            email = input("Введите email заказчика - ")
            address = input("Введите адрес заказчика - ")
            add_user(name, email, address)
            print("######################################\n")
        case 2:
            print("######################################\n")
            user_id = input("Введите ID заказчика которого хотите удалить - ")
            delete_user(user_id)
            print("######################################\n")
        case 3:
            users = get_all_users()
            print("######################################\n")
            print("Список заказчиков:")
            if not users:
                print("Заказчики не найдены")
            for user in users:
                print(f"ID: {user[0]}, NAME: {user[1]}, EMAIL: {user[2]}, ADDRESS: {user[3]}")
            print()
            print("######################################\n")
        case 4:
            print("######################################\n")
            name = input("Введите название товара - ")
            price = input("Введите цену товара - ")
            add_product(name, price)
            print("######################################\n")
        case 5:
            print("######################################\n")
            product_id = input("Введите ID товара который хотите удалить - ")
            delete_product(product_id)
            print("######################################\n")
        case 6:
            products = get_all_products()
            print("######################################\n")
            print("Список товаров:")
            if not products:
                print("Товары не найдены")
            for product in products:
                print(f"ID: {product[0]}, NAME: {product[1]}, PRICE: {product[2]}")
            print()
            print("######################################\n")
        case 7:
            print("######################################\n")
            orderer_id = int(input("Введите ID заказчика - "))
            delivery_address = input("Введите адрес доставки - ")
            add_order(orderer_id, delivery_address)
            print("######################################\n")
        case 8:
            print("######################################\n")
            order_id = input("Введите ID заказа который хотите удалить - ")
            delete_order(order_id)
            print("######################################\n")
        case 9:
            orders = get_all_orders()
            print("######################################\n")
            print("Список заказов:")
            if not orders:
                print("Заказы не найдены")
            for order in orders:
                orderer_name = get_user_by_id(order[1]) if get_user_by_id(order[1]) else ["None","Deleted"]
                print(f"ID: {order[0]}, ORDERER_NAME: {orderer_name[1]} (id:{orderer_name[0]}), DATE: {order[2]}, DELIVERY_ADDRESS: {order[3]}")
            print()
            print("######################################\n")
        case 10:
            print("######################################\n")
            order_id = int(input("Введите ID заказа - "))
            product_id = input("Введите ID товара который хотите добавить - ")
            amount = int(input("Введите кол-во товара - "))
            add_order_unit(order_id, product_id, amount)
            print("######################################\n")
        case 11:
            print("######################################\n")
            order_id = int(input("Введите ID заказа - "))
            product_id = input("Введите ID товара который хотите удалить - ")
            delete_order_unit(order_id)
            print("######################################\n")
        case 12:
            print("######################################\n")
            order_id = int(input("Введите ID заказа - "))
            units = get_all_order_units(order_id)
            print(f"Список товаров в заказе ID:{order_id}:")
            if not units:
                print("Товары не найдены")
            for unit in units:
                unit_name = get_product_by_id(unit[2])
                print(f"COST: {unit_name[2]}, AMOUNT: {unit[3]} | {unit_name[1]}")
            print()
            print("######################################\n")