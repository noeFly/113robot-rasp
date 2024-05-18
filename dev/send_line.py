import requests


def send_line_notify(message, token):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }
    data = {
        "message": message
    }
    response = requests.post(url, headers=headers, data=data)
    return response.status_code


# 您的 Line Notify Access Token
access_token = 'X4xlqEByG0H1LGsfXn2SbR8fveV339tcqh54fwynptb'
# message = f'\n我   報\n想   告\n下   ，\n班   靈\n。   芝\n晚   領\n安   主\n    ！'
message = ' '

# 發送訊息
status_code = send_line_notify(message, access_token)
if status_code == 200:
    print('Message sent successfully!')
else:
    print('Failed to send message. Status code:', status_code)
