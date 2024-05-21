from time import sleep

import pygsheets
from paho.mqtt import client as mqtt

from toolbox import log

key: any
sheet: any
worksheet: any
row: int
temp: int
sam_status: bool = False
client: any


def last_row() -> int:
    global worksheet
    i: int = 0
    while True:
        i += 1
        cell = worksheet.cell(f'A{i}').value
        if cell == '':
            return i - 1


def check_press() -> bool:
    global worksheet, row
    if worksheet.cell(f'A{row}') != worksheet.cell(f'A{row - 1}') and worksheet.cell(f'B{row}') == 'true':
        return True
    elif worksheet.cell(f'A{row}') != worksheet.cell(f'A{row - 1}') and worksheet.cell(f'B{row}') == 'false':
        return False


def on_connect(cli, _, __, rc) -> None:
    log(0, 2, f'已連線至 MQTT Broker，結果代碼 {rc}')


def check_diff() -> bool:
    return True if sam_status != temp else False


def check_n_pub() -> None:
    global row, temp, sam_status
    row = last_row()
    if row <= 1:
        return
    temp = check_press()
    if check_diff():
        sam_status = temp
        client.publish('alert', 'override')


def main() -> None:
    global key, sheet, worksheet, row, client, sam_status, temp
    client = mqtt.Client()
    client.on_connect = on_connect
    client.username_pw_set('letsgomqtt', 'letsgooooo')
    client.connect('t20111a2.ala.asia-southeast1.emqxsl.com', 8883)
    key = pygsheets.authorize(service_file='./apikey.json')
    sheet = key.open_by_key('1ha7BqjG4fp5xTt_1_Qs-iC7H4ENWoutN3YyUZxKqqLo')
    worksheet = sheet.worksheet_by_title('工作表1')
    while True:
        check_n_pub()
        sleep(5)


if __name__ == '__main__':
    main()
