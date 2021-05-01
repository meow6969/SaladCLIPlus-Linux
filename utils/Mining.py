import os
import time
import sys
import json


def Salad_Mining():
    with open('config.json') as f:
        js = json.load(f)
    wallet = js['wallet']

    sys.stdout.write("\x1b]2;Choose miner...\x07")
    color = "\033[32m"  # this is green

    os.system('echo ' + color)
    select = input("Select miner! \n1. Phoenixminer 5.5c (GPU) \n2. XMRig 6.11.2 (CPU) \n4. t-rex (GPU) \n"
                   "3. Return \nSelect: ")
    if select == "1" or select.lower() == "phoenixminer":
        os.system('clear')
        sys.stdout.write("\x1b]2;Mining ethash with PhoenixMiner\x07")
        os.system(
            r"miners/PhoenixMiner-5.5c/PhoenixMiner -logfile phoenixlog.txt -rmode 0 -rvram 1 -pool"
            r" stratum+tcp://daggerhashimoto.usa.nicehash.com:3353 -pool2"
            r" stratum+tcp://daggerhashimoto.eu.nicehash.com:3353 -ewal " + (
                wallet) + " -esm 3 -allpools 1 -allcoins 0")

    elif select == "2" or select.lower() == "xmrig":
        os.system("clear")
        sys.stdout.write("\x1b]2;Mining monero with XMRig miner\x07")
        os.system(
            r"miners/XMRig-6.11.2/xmrig --donate-level=1 -o stratum+tcp://randomxmonero.usa.nicehash.com:3380"
            r" --coin=monero -u " + (
                wallet) + " -k --nicehash -o stratum+tcp://randomxmonero")

    elif select == "3" or select.lower() == "t-rex" or select.lower() == "trex":
        os.system("clear")
        sys.stdout.write("\x1b]2;Mining ethash with T-Rex miner\x07")
        os.system(
            r"miners/t-rex-0.20.3/t-rex -a ethash -o"
            r" stratum+tcp://daggerhashimoto.usa.nicehash.com:3353"
            r" -u " + (
                wallet))
    else:
        print("Quitting...")
        time.sleep(1)
