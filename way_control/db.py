import sqlite3

from toolbox import unix_timestamp


def check_database(uuid: int) -> bool:
    con = sqlite3.connect('./../backend.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM cardinfo WHERE uuid = ?', (uuid,))
    result = cur.fetchall()
    return True if result else False


def add_parking(uuid: int) -> None:
    con = sqlite3.connect('./../backend.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM cardinfo WHERE uuid = ?', (uuid,))
    result = cur.fetchall()
    print(result)
    cur.execute('INSERT INTO parking VALUES (?, ?, ?, ?)', (uuid, unix_timestamp(), result[0][1], result[0][2]))
    con.commit()
    con.close()


def del_parking(uuid: int) -> None:
    con = sqlite3.connect('./../backend.db')
    cur = con.cursor()
    cur.execute('DELETE FROM parking WHERE uuid = ?', (uuid,))
    con.commit()
    con.close()
