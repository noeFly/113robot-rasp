import sqlite3


def main():
    con = sqlite3.connect('./../backend.db')
    cur = con.cursor()
    ####################################################################################################################
    cur.execute('CREATE TABLE IF NOT EXISTS cardinfo (uuid INT, name TEXT, phone TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS opendata (time INT, data TEXT)')
    cur.execute('CREATE TABLE IF NOT exists parking ( uuid INT, time INT,name TEXT, phone TEXT)')
    # ##################################################################################################################
    cur.execute('INSERT INTO cardinfo VALUES ("", "林偉哲", "0917-654-321")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "許雅文", "0986-123-456")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "張凱文", "0973-890-123")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "鄭家豪", "0925-678-901")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "溫佳慧", "0994-567-890")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "趙雅琳", "0932-109-876")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "許宗翰", "0958-432-109")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "蕭家瑄", "0906-543-210")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "賴怡婷", "0961-987-654")')
    cur.execute('INSERT INTO cardinfo VALUES ("123", "戴珈嚎", "0947-890-123")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "沈彥宇", "0913-456-789")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "許佳琪", "0975-678-901")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "陳信宏", "0982-109-876")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "郭雅文", "0936-543-210")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "謝怡君", "0950-987-654")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "黃佳慧", "0909-876-543")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "劉彥宇", "0924-321-098")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "林宗翰", "0968-765-432")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "楊怡婷", "0997-654-321")')
    cur.execute('INSERT INTO cardinfo VALUES ("", "王彥宇", "0941-234-567")')
    ####################################################################################################################
    con.commit()
    con.close()


if __name__ == '__main__':
    main()
