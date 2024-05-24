import sqlite3

from toolbox import unix_timestamp


def check_database(uuid) -> bool:
    con = sqlite3.connect('./../backend.db')
    cur = con.cursor()
    print(uuid)
    cur.execute(f'SELECT * FROM cardinfo WHERE uuid = ?', (str(uuid),))
    result = cur.fetchall()
    print(result)
    return True if result else False


def add_parking(uuid) -> None:
    con = sqlite3.connect('./../backend.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM cardinfo WHERE uuid = ?', (str(uuid),))
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
