from datetime import datetime

import pygsheets

gc = pygsheets.authorize(service_file='./apikey.json')
sam_sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/16NM4tjs9V8XxfTkYGW9Ouf-EFt7-5bwGagYKCyhGuOY')
sam_worksheet = sam_sheet[0]
db_sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1oOXiGIKsZaeckzPxZSUjAzNiLEC5CgEnqusLuRHMfao')
db_worksheet = db_sheet.worksheet_by_title('sam')

data: any = 'disable'
statue: bool = False


def last_row() -> int:
    row: int = 1
    while sam_worksheet.get_value((row, 0)) != '':
        row += 1
    return row - 1


def unix() -> int:
    return round((datetime.now() - datetime(1970, 1, 1)).total_seconds())


def main():
    while True:
        global data, statue
        row = last_row()
        value = sam_worksheet.get_value((row, 0))
        # print(row, value)
        # print(sam_worksheet.get_value(f'A{last_row()}'))
        print('222')
        if value == data:
            continue
        print('111')
        if value == 'enable' and not statue:
            statue = True
            data = value
            db_worksheet.append_table(values=[unix(), 'enable'])
        elif value == 'disable' and statue:
            statue = False
            data = value
            db_worksheet.append_table(values=[unix(), 'disable'])

        # time.sleep(1)


if __name__ == '__main__':
    main()
...

# import time
# import pygsheet
# import toolbox
#
# key: any
# sheet: any
# worksheet: any
# row: int
# temp: int
# sam_status: bool = False
# client: any
#
#
# def last_row() -> int:
#     global worksheet
#     i: int = 0
#     while True:
#         i += 1
#         cell = worksheet.cell(f'A{i}').value
#         if cell == '':
#             return i - 1
#
#
# def check_press() -> bool:
#     global worksheet, row
#     if worksheet.cell(f'A{row}') != worksheet.cell(f'A{row - 1}') and worksheet.cell(f'B{row}') == 'true':
#         return True
#     elif worksheet.cell(f'A{row}') != worksheet.cell(f'A{row - 1}') and worksheet.cell(f'B{row}') == 'false':
#         return False
#
#
# # def on_connect(cli, _, __, rc) -> None:
# #     log(0, 2, f'已連線至 MQTT Broker，結果代碼 {rc}')
#
#
# def check_diff() -> bool:
#     return True if sam_status != temp else False
#
#
# def check_n_pub() -> None:
#     global row, temp, sam_status
#     row = last_row()
#     if row <= 1:
#         return
#     temp = check_press()
#     if check_diff():
#         sam_status = temp
#         client.publish('noefly/mqtt/alert', 'override')
#
#
# def main() -> None:
#     global key, sheet, worksheet, row, client, sam_status, temp
#     client = mqtt.Client()
#     client.on_connect = on_connect
#     # client.username_pw_set('letsgomqtt', 'letsgooooo')
#     client.connect('test.mosquitto.org', 1883)
#     key = pygsheets.authorize(service_file='./apikey.json')
#     sheet = key.open_by_key('1ha7BqjG4fp5xTt_1_Qs-iC7H4ENWoutN3YyUZxKqqLo')
#     worksheet = sheet.worksheet_by_title('工作表1')
#     while True:
#         check_n_pub()
#         sleep(5)
#
#
# if __name__ == '__main__':
#     main()
