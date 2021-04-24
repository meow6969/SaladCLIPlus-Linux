import os
import time
import requests
import sys
import pyperclip
import json
import Balance
import Lifetime
import XP
import salad_earnings_update
import Mining

sys.stdout.write("\x1b]2;Salad CLI+\x07")
refresh_time = 15  # seconds
color = "\033[32m"  # like u would type "color 0A" into cmd / leave empty for default - this color is green

with open('config.json') as f:
    js = json.load(f)
salad_auth = js['salad_key']
cookie = {
    "Salad.Authentication": salad_auth
}
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Salad/0.4.2 Chrome/78.0.3904.130 Electron/7.1.9 Safari/537.36'
}
with open('Login screen.txt', encoding='utf-8') as f:
    loginscreen = f.read()
os.system('echo ' + color)

saladuser = requests.get(url='https://app-api.salad.io/api/v1/profile', headers=headers, cookies=cookie)
if saladuser.status_code != 200:
    print('REPLACE YOUR SALAD AUTH CODE!')
    input()
    exit()
saladuser = saladuser.json()

referral = requests.get(url='https://app-api.salad.io/api/v1/profile/referral-code', headers=headers, cookies=cookie)
if referral.status_code != 200:
    print('REPLACE YOUR SALAD AUTH CODE!')
    input()
    exit()
referral = referral.json()
while True:
    print(loginscreen)
    print('Username: ' + str(saladuser['username']))
    print('Email: ' + str(saladuser['email']))
    print('User id: ' + str(saladuser['id']))
    # print('Username: HIDDEN IN TEST MODE!')
    # print('Email: HIDDEN IN TEST MODE!')
    # print('User id: HIDDEN IN TEST MODE!')
    print("\n\n")

    # input selection
    select = input(
        "Select option! \n1. Balance \n2. Lifetime \n3. XP \n4. Earning History \n5. Copy Referral Code \n"
        "6. Start mining!"
        " \nSelect: ")
    if select == "1" or select == "Balance":
        Balance.Salad_Balance()

    if select == "2" or select == "Lifetime":
        Lifetime.Salad_Lifetime()

    if select == "3" or select == "XP":
        XP.Salad_XP()

    if select == "4" or select == "Earning History":
        salad_earnings_update.Salad_Earings()

    if select == "5" or select == "Copy Referral Code":
        pyperclip.copy(
            'Join me on Salad and use code ' + str(referral['code']) + ' for a 2x earning rate bonus! https://www.salad.io')
        print('Code copied to clipboard!')

    if select == "6" or select == "Start mining":
        Mining.Salad_Mining()
    time.sleep(2)
