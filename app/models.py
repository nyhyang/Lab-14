import sqlite3 as sql

def insert_user(nickname, email):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO user (nickname, email) values (?, ?)", 
            (nickname, email))
        con.commit()


def insert_trip(user_id, destination, name_of_trip, trip_date, duration, budget, friend):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO trip (destination, name_of_trip, trip_date, duration, budget, friend) values (?, ?, ?, ?, ?, ?)", 
            (destination, name_of_trip, trip_date, duration, budget, friend))
        trip_id = cur.lastrowid
        cur.execute("INSERT INTO user_trip (user_id, trip_id) values (?, ?)", 
            (user_id, trip_id))
        con.commit()

def retrieve_trip(user_id):
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("select t.* from trip t, user_trip ut where t.trip_id= tu.trip_id and tu.user_id= ?", (user_id)).fetchall()
    return result

def delete_trip(trip_id):
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("delete from trip where trip_id=?", (trip_id))











