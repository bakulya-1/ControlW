CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    price TEXT,
    photo TEXT,
    size TEXT,
    product_id TEXT
    )
"""

INSERT_store_query = """
    INSERT INTO store (name_product, photo, product_id, price, size)
    VALUES (?, ?, ?, ?, ?)
"""



CREATE_TABLE_order = """
    CREATE TABLE IF NOT EXISTS order (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    size TEXT,
    product_id TEXT,
    quantity TEXT,
    contact TEXT
    )
"""

INSERT_order_query = """
    INSERT INTO store (product_id, size, quantity, contact)
    VALUES (?, ?, ?, ?)
"""



