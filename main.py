import sys
import os
from utils import *


sys.stdout.write("\x1b]2;Salad CLI+ SETUP\x07")
python = input("\nEnter the name of your python prefix (for example \"python3\"): ")
os.system(f"{python} -m pip install --upgrade pip")
os.system(f"{python} -m pip install pyperclip")
os.system(f"{python} -m pip install python-dateutil")
os.system(f"{python} -m pip install argparse")
os.system(f"{python} -m pip install requests")
