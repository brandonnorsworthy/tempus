import subprocess
import random
import time
from sys import argv

script, loop_amount = argv

emulator_port = int(5555) #hard coded for testing allows for all emulators to be interacted with apon change
interact_x = int(471)
interact_y = int(322)
resolution_width = int(960)
resolution_height = int(540)
stdoutlineformatted = "" #formatted byte string from byte variable stdoutline

def sleeper(min, max):
    tempmax = max * random.random()
    time.sleep(min + tempmax)
    print(tempmax)

def pixelsearch(interact_x, interact_y):
    if interact_x > resolution_width or interact_y > resolution_height:
        print("Interaction location to great!")

    item = subprocess.Popen(["shellcolorgrabber.bat", str(emulator_port), str(resolution_width * interact_y + interact_x)], shell=True, stdout=subprocess.PIPE) #launch subprocess to send commands to adb using .bat files
    for stdoutline in item.stdout:
        stdoutlineformatted += str(stdoutline, 'utf-8')

    temp = "".join(stdoutlineformatted[stdoutlineformatted.find('00000000') + 10:stdoutlineformatted.find('ff')].split()) #grab the bytes only needed which are RGB seperated by spaces and strip the whitespace

    return item

#def click(interact_x, interact_y):

def clickDrag(min_x, min_y, max_x, max_y, duration):
    #port, x, y, duration
    item = subprocess.Popen(["shellinputdrag.bat", str(emulator_port), str(interact_x), str(interact_y), str(duration)], shell=True, stdout=subprocess.PIPE)

def clickRandom(min_x, min_y, max_x, max_y):
    #port, x, y
    item = subprocess.Popen(["shellinputtap.bat", str(emulator_port), str(min_x + ((max_x - min_x) * random.random())), str(min_y + ((max_y - min_y) * random.random()))], shell=True, stdout=subprocess.PIPE)

def main():
    #call python script specifically for that emulator(port)

    #click on compass
    clickRandom(789, 38, 759, 10) 
    #drag up to center camera

    #go to settings and click middle of zoom

    #while(oredepleted=false):
    #colorgrab the ore and see if its depleted
        #if yes wait
    #mine non depleted ore until depleted
    print("ran\n")

main()