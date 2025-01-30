import sqlite3
from db import queries


#db = sqlite3.connect('db/store.sqlite3')
db = sqlite3.connect('db/order.sqlite3')
cursor = db.cursor()


async def create_db():
    if db:
        print('База данных подключена')
#    cursor.execute(queries.CREATE_TABLE_store)
    cursor.execute(queries.CREATE_TABLE_order)


async def sql_insert_store(name_product, size, price, photo, product_id):
    cursor.execute(queries.INSERT_store_query, (
        name_product, size, price, photo, product_id
    ))
    db.commit()


async def sql_insert_order(size, product_id, contact, quantity):
    cursor.execute(queries.INSERT_order_query, (
        size, product_id, contact, quantity
    ))
    db.commit()
    db.close()



