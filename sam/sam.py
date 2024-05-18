import pygsheets

from toolbox import log

key: any
sheet: any
worksheet: any
row: int
sam_status: bool = False
temp: bool = False


def last_row() -> int:
    global worksheet
    i: int = 0
    while True:
        i += 1
        cell = worksheet.cell(f'A{i}')
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


def main() -> None:
    global key, sheet, worksheet, row
    key = pygsheets.authorize('./creative-113-280a2ba283f9.json')
    sheet = key.open_by_key('1ha7BqjG4fp5xTt_1_Qs-iC7H4ENWoutN3YyUZxKqqLo')
    worksheet = sheet.worksheet_by_title('工作表1')
    row = last_row()
    temp = check_press()
    if check_diff():
