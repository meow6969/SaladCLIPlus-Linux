import os
import time
import requests
import sys
from time import sleep
import json

os.system(cmd)
sys.stdout.write("\x1b]2;Choose miner...\x07")
refresh_time = 15  # seconds
color = '0A'  # like u would type "color 0A" into cmd / leave empty for default

os.system('color ' + color)
select = input("Select miner! \n1. Phoenixminer 5.4c (GPU) \n2. XMRig 6.7.0 (CPU) \n3. Return to main menu \nSelect: ")
if select == "1" or select == "Phoenixminer":
	os.system("cls")
	sys.stdout.write("\x1b]2;Enter Wallet...\x07")	
	phoenixwallet = input("Enter Wallet Adress: ")
#	print("%appdata%\salad\plugin-bin\PhoenixMiner-5.4c\PhoenixMiner.exe -rmode 0 -rvram 1 -pool stratum+tcp://daggerhashimoto.usa.nicehash.com:3353 -pool2 stratum+tcp://daggerhashimoto.eu.nicehash.com:3353 -ewal "+ (phoenixwallet) + " -esm 3 -allpools 1 -allcoins 0")
#	time.sleep(1100000)
	os.system("mode 230,60")	
	os.system("%appdata%\salad\plugin-bin\PhoenixMiner-5.4c\PhoenixMiner.exe -logfile phoenixlog.txt -rmode 0 -rvram 1 -pool stratum+tcp://daggerhashimoto.usa.nicehash.com:3353 -pool2 stratum+tcp://daggerhashimoto.eu.nicehash.com:3353 -ewal "+ (phoenixwallet) + " -esm 3 -allpools 1 -allcoins 0")
if select == "2" or select == "XMrig":
	os.system("cls")
	sys.stdout.write("\x1b]2;Enter Wallet...\x07")
	xmrwallet = input ("Enter Wallet Adress: ")
#	print(r"%appdata%\salad\plugin-bin\XMRig-CPU-6.7.0\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero.usa.nicehash.com:3380 --coin=monero -u "+ (xmrwallet) + " -k --nicehash -o stratum+tcp://randomxmonero")
#	time.sleep(1100000)
	os.system("mode 230,60")
	os.system(r"%appdata%\salad\plugin-bin\XMRig-CPU-6.7.0\xmrig.exe --donate-level=1 -o stratum+tcp://randomxmonero.usa.nicehash.com:3380 --coin=monero -u "+ (xmrwallet) + " -k --nicehash -o stratum+tcp://randomxmonero")

if select == "3" or select == "Return":
	print("Quiting...")
	time.sleep(1)
	os.system("py Start.py")
