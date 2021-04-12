import os
import time
import sys
import json


def Salad_Mining():
    with open('config.json') as f:
        js = json.load(f)
    wallet = js['wallet']

    sys.stdout.write("\x1b]2;Choose miner...\x07")
    color = "\033[32m"  # like u would type "color 0A" into cmd / leave empty for default - this is green

    os.system('echo ' + color)
    select = input("Select miner! \n1. Phoenixminer 5.5c (GPU) \n2. XMRig 6.11.2 (CPU)\n3. Return \nSelect: ")
    if select == "1" or select == "Phoenixminer":
        os.system(
            r"PhoenixMiner-5.5c/PhoenixMiner -logfile phoenixlog.txt -rmode 0 -rvram 1 -pool"
            r" stratum+tcp://daggerhashimoto.usa.nicehash.com:3353 -pool2"
            r" stratum+tcp://daggerhashimoto.eu.nicehash.com:3353 -ewal " + (
                wallet) + " -esm 3 -allpools 1 -allcoins 0")
    if select == "2" or select == "XMRig":
        os.system("clear")
        os.system(
            r"XMRig-6.11.2/xmrig --donate-level=1 -o stratum+tcp://randomxmonero.usa.nicehash.com:3380"
            r" --coin=monero -u " + (
                wallet) + " -k --nicehash -o stratum+tcp://randomxmonero")
    if select == "3" or select == "Return":
        print("Quitting...")
        time.sleep(1)
