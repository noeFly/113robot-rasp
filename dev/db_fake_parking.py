import sqlite3

from db_init import main as init


def main():
    init()
    con = sqlite3.connect('./../backend.db')
    cur = con.cursor()
    cur.execute('INSERT INTO parking VALUES (123, 123456789, "戴珈嚎", "0947-890-123")')
    # cur.execute('INSERT INTO parking VALUES (456, 123456789, "Pebble", "0947-890-123")')
    con.commit()
    con.close()


if __name__ == '__main__':
    main()
