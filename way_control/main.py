from datetime import datetime

import pygsheets

from alert import main as send_alert

# import ButterFly
gc = pygsheets.authorize(service_file='./apikey.json')
sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1oOXiGIKsZaeckzPxZSUjAzNiLEC5CgEnqusLuRHMfao')
status = sheet.worksheet_by_title('status')
water = sheet.worksheet_by_title('water')
rfid0 = sheet.worksheet_by_title('rfid0')
rfid1 = sheet.worksheet_by_title('rfid1')
sam = sheet.worksheet_by_title('sam')
parking = sheet.worksheet_by_title('parking')
card = sheet.worksheet_by_title('card')
rfid0_time: str = ''
rfid1_time: str = ''
sam_time: str = ''
lockdown: bool = False
print('初始化完成')


def last_row(wks: int) -> int:
    global rfid0, rfid1, sam
    row: int = 1
    if wks == 0:
        while rfid0.get_value((row, 0)) != '':
            row += 1
    elif wks == 1:
        while rfid1.get_value((row, 0)) != '':
            row += 1
    elif wks == 2:
        while sam.get_value((row, 0)) != '':
            row += 1
    return row - 1


def unix() -> int:
    return round((datetime.now() - datetime(1970, 1, 1)).total_seconds())


def sam_pressed() -> bool:
    global sam, sam_time
    sam_value = sam.get_value(f'A{last_row(2)}')
    if sam_value != sam_time:
        sam_time = sam_value
        return True
    else:
        return False


def handle_wayin():
    print('[wayin] 開始處理資料')
    global rfid0, card, status
    # 處理入口 RFID
    rfid0_value = rfid0.get_value((last_row(0), 2))
    locate = card.find(rfid0_value)
    # print(rfid0_value, locate)
    if not locate:
        return
    status.update_value('B5', 'action')
    uid = card.get_value((locate[0].row, 1))
    carid = card.get_value((locate[0].row, 2))
    name = card.get_value((locate[0].row, 3))
    parking.append_table(values=[f'{uid}', f'{carid}', f'{name}'])
    rfid0.append_table(values=['----', '已處理資料'])
    print('[wayin] 已發送開啟指令')


def handle_wayout():
    print('[wayout] 開始處理資料')
    global rfid1, card, status
    # 處理入口 RFID
    rfid1_value = rfid1.get_value((last_row(1), 2))
    locate = card.find(rfid1_value)
    # print(rfid0_value, locate)
    if not locate:
        return
    status.update_value('B5', 'action')
    parking.delete_rows(2)
    rfid0.append_table(values=['----', '已處理資料'])
    print('[wayout] 已發送開啟指令')


def handle_lockdown():
    # lockdown
    global lockdown
    print('[lockdown] 開始處理資料')
    if sam_pressed():
        print('[lockdown] SamLabs 被按下')
        if not lockdown:
            status.update_value('B4', 'override')
            lockdown = True
            sam.append_table(values=['-----', '已處理資料'])
            send_alert(True)
        else:
            status.update_value('B4', 'unlock')
            lockdown = False
            sam.append_table(values=['-----', '已處理資料'])


def main() -> None:
    while True:
        handle_wayin()
        handle_wayout()
        handle_lockdown()
        print()
        # time.sleep(1)


if __name__ == '__main__':
    main()
