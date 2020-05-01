import subprocess
import shlex
from subprocess import Popen
import time
import random
from sys import argv

def sleeper(min, max):
    tempmax = max * random.random()
    time.sleep(min + tempmax)
    print(tempmax)

def callSleeper():
    for i in range(5):
        time.sleep(2)
        sleeper(1,10)

script, x, y = argv
x, y = int(x), int(y)

#callSleeper()

#WIDTH * $Y + $X + 3 = <1/4 of max
offset = 960 * y + x + 3
print("Byte offset = " + str(offset))

#subprocess.run(['dir'], shell=True, cwd='tools')

#TODO make multilined commands eg
#go into shell and then screenshot
subprocess.run(['adb', '-s', 'localhost:5555', 'shell', 'input', 'tap', '300', '300'], shell=True, cwd='tools')
subprocess.run(['adb', '-s' ,'localhost:5555', 'shell', 'screencap', '/sdcard/screencap.dump'], shell=True, cwd='tools')
subprocess.run(['adb', '-s' ,'localhost:5555', 'shell', 'dd', 'if=\"/sdcard/screencap.dump\"', 'bs=4', 'count=1', f'skip={offset}', '2>/dev/null', '|', 'hexdump', '-C'], shell=True, cwd='tools')

#Popen("adb -s localhost:5555 shell input tap 300 300",shell=True, cwd='tools')