import pygsheets
import requests


def send_line_notify(final: bool, data: any) -> None:
    if not final:
        requests.post(
            'https://notify-api.line.me/api/notify',
            headers={
                'Authorization': 'Bearer 0RyvLiVjY7SpHEEohpnNKkQyFrOy2NCublkZOlKI6JB'
            },
            data={
                'message':
                    f'\n　　車主{data}先生／小姐您好，\n中央氣象署已發布陸上颱風警報，\n提醒您請盡速將停放於「百齡橋堤\n外停車場」的愛車移動至河堤內。'
                    f'\n\n　　亦或是稍晚管理處將聯絡拖吊\n車業者，協助拖吊至附近停車場，\n謝謝你的配合。'
                    f'\n\n　停車場管理處　關心您　♥',
                'stickerPackageId': 11539,
                'stickerId': 52114110
            })
    else:
        requests.post(
            'https://notify-api.line.me/api/notify',
            headers={
                'Authorization': 'Bearer 0RyvLiVjY7SpHEEohpnNKkQyFrOy2NCublkZOlKI6JB'
            },
            data={
                'message':
                    f'\n　　車主{data}先生／小姐您好，\n您的愛車已請拖吊車業者協助移動\n至「社中街平面停車場」。請盡早\n前往該停車場取車！'
                    f'\n\n📍社中街平面停車場'
                    f'\n- 地址：臺北市士林區社中街 96 號'
                    f'\n- 參考地圖：https://lurl.cc/RHuEWD'
                    f'\n\n　停車場管理處　關心您　♥',
                'stickerPackageId': 11539,
                'stickerId': 52114110
            })


def main(final: bool) -> None:
    gc = pygsheets.authorize(service_file='./apikey.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1oOXiGIKsZaeckzPxZSUjAzNiLEC5CgEnqusLuRHMfao')
    card = sheet.worksheet_by_title('card')
    parking = sheet.worksheet_by_title('parking')
    row: int = 1
    while card.get_value((row, 0)) != '':
        row += 1
    row -= 1
    for i in range(row):
        # cardid = card.get_value((i + 1, 1))
        name = parking.get_value((i + 1, 3))
        send_line_notify(final, name)


if __name__ == '__main__':
    main(False)
