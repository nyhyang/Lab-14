import sqlite3 as sql

def insert_user(nickname, email):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO user (nickname, email) values (?, ?)", 
            (nickname, email))
        con.commit()


def insert_trip(name_of_part, manufacturer_of_part, customer_id):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO orders (name_of_part, manufacturer_of_part) values (?, ?)", 
            (name_of_part, manufacturer_of_part))
        order_id = cur.lastrowid
        cur.execute("INSERT INTO customer_order (order_id, customer_id) values (?, ?)", 
            (order_id, customer_id))
        con.commit()