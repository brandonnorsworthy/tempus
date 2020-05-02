import subprocess
import random
import time
from sys import argv

script, loop_amount = argv

emulator_port = int(5555) #hard coded for testing allows for all emulators to be interacted with apon change
resolution_width = int(960)
resolution_height = int(540)
stdoutlineformatted = "" #formatted byte string from byte variable stdoutline

#auto crunch area

def sleep(min, max): #sleeps for a random amount of time within a range
    tempmax = max * random.random()
    time.sleep(min + tempmax)

def pixelsearch(interact_x, interact_y): #looks at a specific pixel and gives the hex color value
    if interact_x > resolution_width or interact_y > resolution_height:
        print("Interaction location to great!")

    item = subprocess.Popen(["shellcolorgrabber.bat", str(emulator_port), str(resolution_width * interact_y + interact_x)], shell=True, stdout=subprocess.PIPE) #launch subprocess to send commands to adb using .bat files
    for stdoutline in item.stdout:
        stdoutlineformatted += str(stdoutline, 'utf-8')

    temp = "".join(stdoutlineformatted[stdoutlineformatted.find('00000000') + 10:stdoutlineformatted.find('ff')].split()) #grab the bytes only needed which are RGB seperated by spaces and strip the whitespace

    return item

#interactions

def click(interact_x, interact_y): #clicks at a specific spot
    #port, x, y
    item = subprocess.Popen(["shellinputtap.bat", str(emulator_port), str(interact_x), str(interact_y)], shell=True, stdout=subprocess.PIPE)

def clickRandom(min_x, min_y, max_x, max_y): #clicks a random spot within a range
    #port, x, y
    item = subprocess.Popen(["shellinputtap.bat", str(emulator_port), str(min_x + ((max_x - min_x) * random.random())), str(min_y + ((max_y - min_y) * random.random()))], shell=True, stdout=subprocess.PIPE)

def clickDragDown(min_x, min_y, max_x, max_y, min_distance, max_distance): #drags the mouse down at a random spot within a range
    #port, x1, y1, x2, y2
    tempx = min_x + ((max_x - min_x) * random.random())
    tempy = min_y + ((max_y - min_y) * random.random())
    item = subprocess.Popen(["shellinputdrag.bat", str(emulator_port), str(tempx), str(tempy), 
    str(tempx), str(tempy + min_distance + ((max_distance - min_distance) * random.random()))], shell=True, stdout=subprocess.PIPE)

#bot sections

def centerCamera(): #sets camera to north and zoom to exact setting
    #click on compass
    clickRandom(789, 38, 759, 10)
    sleep(0.5, 4)
    #drag up to center camera
    clickDragDown(100, 51, 700, 360, 120, 200)
    sleep(1, 3)
    #go to settings
    clickRandom(909, 426, 943, 465)
    sleep(1,3)
    #click middle of zoom bar
    click(810, 295)
    sleep(1,3)
    #close settings
    clickRandom(909, 426, 943, 465)
    sleep(1,3)

def main():
    #TODO call python script specifically for that emulator(port)
    #TODO when sending RANDOM variables to a batch file format them to 1 decimal place maximum

    #loop based on how many times chosen
    for amount in range(int(loop_amount)):


        #while(oredepleted=false):
        #colorgrab the ore and see if its depleted
            #if yes wait
        #mine non depleted ore until depleted

    print("finished\n")

main()