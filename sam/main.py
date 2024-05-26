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