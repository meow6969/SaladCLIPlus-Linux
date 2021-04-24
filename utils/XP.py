import os
import requests
import sys
import time
import json


def Salad_XP():
    sys.stdout.write("\x1b]2;Experience\x07")
    color = "\033[32m"  # like u would type "color 0A" into cmd / leave empty for default - this color is green

    with open('config.json') as f:
        js = json.load(f)
    salad_auth = js['salad_key']
    cookie = {
        "Salad.Authentication": salad_auth
    }
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Salad/0.4.2'
                      ' Chrome/78.0.3904.130 Electron/7.1.9 Safari/537.36'
    }
    with open('utils/art.txt', encoding='utf-8') as f:
        art = f.read()
    os.system('echo ' + color)

    os.system('clear')
    rxp = requests.get(url='https://app-api.salad.io/api/v1/profile/xp', headers=headers, cookies=cookie)

    rxp = rxp.json()

    print(art)

    print('Experience: ' + str(rxp['lifetimeXp']) + 'XP')
    print(' ')
    print('-------------------------------------')

    input()
