import sqlite3

from paho.mqtt import client as mqtt

from alert import main as line_notify
from db import add_parking, check_database, del_parking
from toolbox import log, unix_timestamp

client: any
wayin_car: bool = False
wayout_car: bool = False


def on_connect(cli, _, __, rc) -> None:
    log(0, 4, f'已連線至 MQTT Broker，結果代碼 {rc}')
    cli.subscribe('wayIn', 'wayOut', 'rfid0', 'rfid1', 'water')


def on_massage(_, __, message) -> None:
    global client, wayin_car, wayout_car
    if message.topic == 'wayIn':
        if message.payload == 'sonar.enable':
            wayin_car = True
        elif message.payload == 'sonar.disable':
            wayin_car = False
    elif message.topic == 'wayOut':
        if message.payload == 'sonar.enable':
            wayout_car = True
        elif message.payload == 'sonar.disable':
            wayout_car = False
    elif message.topic == 'rfid0':
        if not wayin_car:
            return
        if not check_database(message.payload):
            client.publish('wayIn', 'id.notfound')
            return
        client.publish('wayIn', 'gate.action')
        add_parking(message.payload)
    elif message.topic == 'rfid1':
        if not wayout_car:
            return
        if not check_database(message.payload):
            client.publish('wayOut', 'id.notfound')
            return
        client.publish('wayOut', 'gate.action')
        del_parking(message.payload)
    elif message.topic == 'water':
        con = sqlite3.connect('./../backend.db')
        cur = con.cursor()
        cur.execute('INSERT INTO water VALUES ( ?, ? )', (unix_timestamp(), message.payload))
        con.commit()
        con.close()
        if float(message.payload) >= 0:
            line_notify(False)

    # elif message.topic == 'alert':
    # if message.payload == 'override'
    # print(f'[{message.topic}]: {message.payload}')


def main() -> None:
    con = sqlite3.connect("./../backend.db")
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT exists parking (uuid INT, time INT,name TEXT, phone TEXT)')
    con.commit()
    con.close()
    global client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_massage = on_massage
    client.username_pw_set('letsgomqtt', 'letsgooooo')
    client.connect('t20111a2.ala.asia-southeast1.emqxsl.com', 8883)
    client.loop_forever()


if __name__ == '__main__':
    main()
