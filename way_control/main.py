import sqlite3

from paho.mqtt import client as mqtt

from alert import main as line_notify
from db import add_parking, check_database, del_parking
from toolbox import log, unix_timestamp

client: any
wayin_car: bool = False
wayout_car: bool = False


def on_connect(cli, __, ___, rc) -> None:
    log(0, 4, f'已連線至 MQTT Broker，結果代碼 {rc}')
    topic = (
        'noefly/mqtt/wayIn',
        'noefly/mqtt/wayOut',
        'noefly/mqtt/rfid0',
        'noefly/mqtt/rfid1',
        'noefly/mqtt/water')
    global client
    for t in topic:
        client.subscribe(t)


def on_message(_, __, message) -> None:
    global client, wayin_car, wayout_car

    if message.topic == 'noefly/mqtt/wayIn':
        if message.payload == b'module.sonar.enable':
            wayin_car = True
        elif message.payload == b'module.sonar.disable':
            wayin_car = False
    elif message.topic == 'noefly/mqtt/wayOut':
        if message.payload == b'module.sonar.enable':
            wayout_car = True
        elif message.payload == b'module.sonar.disable':
            wayout_car = False
    elif message.topic == 'noefly/mqtt/rfid0':
        if not wayin_car:
            return
        if not check_database(message.payload):
            client.publish('noefly/mqtt/wayIn', 'id.notfound')
            return
        client.publish('noefly/mqtt/wayIn', 'gate.action')
        add_parking(message.payload)
    elif message.topic == 'noefly/mqtt/rfid1':
        if not wayout_car:
            return
        if not check_database(message.payload):
            client.publish('noefly/mqtt/wayOut', 'id.notfound')
            return
        client.publish('noefly/mqtt/wayOut', 'gate.action')
        del_parking(message.payload)
    elif message.topic == 'noefly/mqtt/water':
        con = sqlite3.connect('./../backend.db')
        cur = con.cursor()
        cur.execute('INSERT INTO water VALUES ( ?, ? )', (unix_timestamp(), message.payload))
        con.commit()
        con.close()
        if float(message.payload) >= 4000:
            line_notify(False)
    print(wayin_car)


def main() -> None:
    global client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message  # 註冊 on_message 回調函數
    client.username_pw_set("", "")
    client.connect('test.mosquitto.org', 1883)
    client.loop_start()  # 啟動非阻塞迴圈
    while True:
        pass  # 保持主程序運行


if __name__ == '__main__':
    main()
