
import requests
from config import FT_QQ_KEY


msg_list = []


def notify_wx(msg):
    global msg_list
    if msg in msg_list:
        return
    msg_list.append(msg)
    send_result(msg)
    clear_list()
    print(f'send msg: {msg}')


def clear_list():
    global msg_list
    if len(msg_list) > 1000:
        msg_list = msg_list[500:]


def send_result(content, skey=FT_QQ_KEY):
    url = 'https://sc.ftqq.com/%s.send' % skey
    data = {
        'text': '什么值得买',
        'desp': content
    }
    resp = requests.get(url, data)
    print('执行结束', resp.status_code, resp.json())
