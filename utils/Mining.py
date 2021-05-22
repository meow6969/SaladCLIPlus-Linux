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
    select = input("Select miner! \n"
                   "1. Phoenixminer 5.5c (Nvidia-GPU) \n"
                   "2. XMRig 6.11.2 (CPU) \n"
                   "3. T-rex (Nvidia-GPU) \n"
                   "4. ethminer (AMD-GPU) \n"
                   "5. Return \nSelect: ")
    if select == "1" or select.lower() == "phoenixminer":
        os.system('clear')
        sys.stdout.write("\x1b]2;Mining ethash with PhoenixMiner\x07")
        os.system(
            r"miners/PhoenixMiner/PhoenixMiner -logfile phoenixlog.txt -rmode 0 -rvram 1 -pool"
            r" stratum+tcp://daggerhashimoto.usa.nicehash.com:3353 -pool2"
            r" stratum+tcp://daggerhashimoto.eu.nicehash.com:3353 -ewal " + (
                wallet) + " -esm 3 -allpools 1 -allcoins 0")

    elif select == "2" or select.lower() == "xmrig":
        os.system("clear")
        sys.stdout.write("\x1b]2;Mining monero with XMRig miner\x07")
        os.system(
            r"miners/XMRig/xmrig --donate-level=1 -o stratum+tcp://randomxmonero.usa.nicehash.com:3380"
            rf" --coin=monero -u {wallet} -k --nicehash -o stratum+tcp://randomxmonero")

    elif select == "3" or select.lower() == "t-rex" or select.lower() == "trex":
        os.system("clear")
        sys.stdout.write("\x1b]2;Mining ethash with T-Rex miner\x07")
        os.system(
            r"miners/t-rex/t-rex -a ethash -o"
            r" stratum+tcp://daggerhashimoto.usa.nicehash.com:3353"
            rf" -u {wallet}")
    elif select == "4" or select.lower() == "ethminer":
        os.system("clear")
        sys.stdout.write("\x1b]2;Mining ethash with ethminer\x07")
        os.system(rf"miners/ethminer/ethminer -P stratum2+tcp://{wallet}@daggerhashimoto.usa-west.nicehash.com:3353 -G")
    else:
        print("Quitting...")
        time.sleep(1)
