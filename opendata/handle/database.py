import sqlite3

con: any
cur: any


def connect() -> None:
    global con, cur
    con = sqlite3.connect('./../backend.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS opendata (time INTEGER, data BLOB)')


def insert(time: int, data: any) -> None:
    global con, cur
    cur.execute(f'INSERT INTO opendata VALUES ({time}, "{data}")')
    con.commit()


def close() -> None:
    global con
    con.close()


def write_data(time: int, data: str) -> None:
    connect()
    insert(time, data)
    close()
