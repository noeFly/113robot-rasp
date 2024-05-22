import sqlite3

import requests


def send_line_notify(final: bool, data: any) -> None:
    if not final:
        requests.post(
            'https://notify-api.line.me/api/notify',
            headers={
                'Authorization': 'Bearer X4xlqEByG0H1LGsfXn2SbR8fveV339tcqh54fwynptb'
            },
            data={
                'message':
                    f'\n　　車主{data[2]}先生／小姐您好，\n中央氣象署已發布陸上颱風警報，\n提醒您請盡速將停放於「百齡橋堤\n外停車場」的愛車移動至河堤內。'
                    f'\n\n　　亦或是稍晚管理處將聯絡拖吊\n車業者，協助拖吊至附近停車場，\n謝謝你的配合。'
                    f'\n\n　停車場管理處　關心您　♥',
                'stickerPackageId': 11539,
                'stickerId': 52114110
            })
    else:
        requests.post(
            'https://notify-api.line.me/api/notify',
            headers={
                'Authorization': 'Bearer X4xlqEByG0H1LGsfXn2SbR8fveV339tcqh54fwynptb'
            },
            data={
                'message':
                    f'\n　　車主{data[2]}先生／小姐您好，\n您的愛車已請拖吊車業者協助移動\n至「社中街平面停車場」。請盡早\n前往該停車場取車！'
                    f'\n\n📍社中街平面停車場'
                    f'\n- 地　　址：臺北市士林區社中街 96 號'
                    f'\n- 參考地圖：https://lurl.cc/RHuEWD'
                    f'\n\n　停車場管理處　關心您　♥',
                'stickerPackageId': 11539,
                'stickerId': 52114110
            })


def main(final: bool) -> None:
    con = sqlite3.connect('./../backend.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM parking')
    parker = cur.fetchall()
    for i in range(len(parker)):
        send_line_notify(final, parker[i])


if __name__ == '__main__':
    main()
