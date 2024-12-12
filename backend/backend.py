from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db_functions import *

app = FastAPI(
    title="SQLite DB manager"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Cookie", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
    expose_headers=["Content-Type", "Cookie", "Set-Cookie"]
)

@app.post('/add_user', tags=["User"])
def serv_add_user(name: str, email: str, address: str):
    add_user(name, email, address)

def serv_delete_user(user_id: int):
    delete_user(user_id)

@app.get('/get_all_users', tags=["User"])
def serv_get_all_users():
    result = []
    for i in get_all_users():
        result.append({
            "user_id": i[0],
            "user_name": i[1],
            "user_email": i[2],
            "user_address": i[3]
        })
    return result

@app.get('/get_user_by_id/{user_id}', tags=["User"])
def serv_get_user_by_id(user_id: int):
    return get_user_by_id(user_id)




@app.post('/add_product', tags=["Product"])
def serv_add_product(name: str, price: float):
    add_product(name, price)


@app.delete('/delete_product/{product_id}', tags=["Product"])
def serv_delete_product(product_id: int):
    delete_product(product_id)


@app.get('/get_all_products', tags=["Product"])
def serv_get_all_products():
    result = []
    for i in get_all_products():
        result.append({
            "product_id": i[0],
            "product_name": i[1],
            "product_price": i[2]
        })
    return result


@app.get('/get_product_by_id/{product_id}', tags=["Product"])
def serv_get_product_by_id(product_id: int):
    return get_product_by_id(product_id)




@app.post('/add_order', tags=["Order"])
def serv_add_order(user_id: int, delivery_address: str):
    add_order(user_id, delivery_address)


@app.delete('/delete_order/{order_id}', tags=["Order"])
def serv_delete_order(order_id: int):
    delete_order(order_id)


@app.get('/get_all_orders', tags=["Order"])
def serv_get_all_orders():
    result = []
    for i in get_all_orders():
        name = get_user_by_id(i[1])
        result.append({
            "order_id": i[0],
            "user_id": i[1],
            "user_name": (name[1] if name else "Deleted"),
            "order_date": i[2],
            "delivery_address": i[3]
        })
    return result




@app.post('/add_order_units', tags=["Order_Unit"])
def serv_add_order_unit(order_id: int, product_id: int, amount: int):
    add_order_unit(order_id, product_id, amount)


@app.delete('/delete_order_units/{order_id}/{product_id}', tags=["Order_Unit"])
def serv_delete_order_units(order_id: int, product_id: int):
    delete_order_unit(order_id, product_id)


@app.get('/get_all_order_units/{order_id}', tags=["Order_Unit"])
def serv_get_all_order_units(order_id: int):
    units = get_all_order_units(order_id)
    result = []
    for unit in units:
        unit_name = get_product_by_id(unit[2])
        result.append({"id": unit_name[0],
                       "name": unit_name[1],
                       "cost": unit_name[2],
                       "amount": unit[3]})
    return result


