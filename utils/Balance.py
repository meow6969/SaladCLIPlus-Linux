import os
import time
import requests
import sys
from time import sleep
import json


def Salad_Balance():
    sys.stdout.write("\x1b]2;Current Balance\x07")
    color = "\033[32m"  # like u would type "color 0A" into cmd / leave empty for default - this is green

    with open('config.json') as f:
        js = json.load(f)
    salad_auth = js['salad_key']
    salad_refresh_token = js['salad_refresh_token']
    cookie = {
        "sAccessToken": salad_auth,
        "sIdRefreshToken": salad_refresh_token
    }
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Salad/0.4.2 Chrome/78.0.3904.130 Electron/7.1.9 Safari/537.36'
    }
    with open('utils/art.txt', encoding='utf-8') as f:
        art = f.read()
    os.system('echo ' + color)

    os.system('clear')
    rbal = requests.get(url='https://app-api.salad.io/api/v1/profile/balance', headers=headers, cookies=cookie)
    if rbal.status_code != 200:
        print('REPLACE YOUR SALAD AUTH CODE!')
        input()
        exit()
    rbal = rbal.json()

    print(art)

    print('Current balance: $' + str(rbal['currentBalance']))
    print(' ')
    print('-------------------------------------')

    input()

