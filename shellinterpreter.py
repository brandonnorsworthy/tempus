import subprocess
import random
import time
import math
from sys import argv

script, loop_amount, reset_camera = argv

emulator_port = int(5555) #hard coded for testing allows for all emulators to be interacted with apon change
resolution_width = int(960)
resolution_height = int(540)

#auto crunch area

def sleep(amount): #sleeps for a specific amount of time
    time.sleep(amount)

def sleepRandom(min, max): #sleeps for a random amount of time within a range
    tempmax = max * random.random()
    time.sleep(min + tempmax)

def hexToRGB(hex_value): #converts hex color to RGB values format: (255, 255, 255)
    if not len(hex_value) == 6:
        print("hexToRGB(): Warning! Parameter hex_value is not 6 characters!")
        return "(255, 255, 255)"
    return (tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4)))

def shadeVariationTest(hex_value_current, hex_value_goal, threshold): #tests wether a hex or rgb value is within a certain shade of the color given
    shadeWithinThreshold = True
    hex_value_goal = str(hex_value_goal)

    #trim the RGB format eg (255, 255, 255) to only numbers and put into an array to be usable for threshold comparison
    rgb_current = str(hexToRGB(hex_value_current)) 
    rgb_current = rgb_current[1:len(rgb_current)-1].replace(',','',2).split()
    rgb_goal = str(hexToRGB(hex_value_goal)) 
    rgb_goal = rgb_goal[1:len(rgb_goal)-1].replace(',','',2).split()

    for x in range(0,3):
        if not (int(rgb_goal[x]) - threshold <= int(rgb_current[x]) <= int(rgb_goal[x]) + threshold): #if rgb value is under threshold of goal rgb
            shadeWithinThreshold = False

    return shadeWithinThreshold


#SHELL INTERACTIONS [tap, swipe, text, pixel-search]

def click(interact_x, interact_y): #sends a Tap input at the given location
    #shellinputtap.bat PARAMETER FORMAT argv = %1 = port, %2 = x, %3 = y
    item = subprocess.Popen(["shellinputtap.bat", str(emulator_port), #Gives all parameters to the ADB shell to be processessed as an input
        str(interact_x), str(interact_y)], shell=True, stdout=subprocess.PIPE)

def clickRandom(min_x, min_y, max_x, max_y): #sends a Tap input in a random location within the range
    #shellinputtap.bat PARAMETER FORMAT argv = %1 = port, %2 = x, %3 = y
    item = subprocess.Popen(["shellinputtap.bat", str(emulator_port), #Gives all parameters to the ADB shell to be processessed as an input
        str(min_x + ((max_x - min_x) * random.random())), str(min_y + ((max_y - min_y) * random.random()))], shell=True, stdout=subprocess.PIPE)

def clickDragDown(min_x, min_y, max_x, max_y, min_distance, max_distance): #sends a Swipe input in a random location within the range
    #shellinputdrag.bat PARAMETER FORMAT argv = %1 = port, %2 = x1, %3 = y1, %4 = x2, %5 = y2
    tempx = min_x + ((max_x - min_x) * random.random())
    tempy = min_y + ((max_y - min_y) * random.random())
    item = subprocess.Popen(["shellinputdrag.bat", str(emulator_port), #Gives all parameters to the ADB shell to be processessed as an input
        str(tempx), str(tempy), str(tempx), str(tempy + min_distance + ((max_distance - min_distance) * random.random()))], shell=True, stdout=subprocess.PIPE)

def pixelSearch(interact_x, interact_y): #Looks at the given pixel and returns the hex color value
    stdoutlineformatted = "" #formatted byte string from byte variable stdoutline

    if interact_x > resolution_width or interact_y > resolution_height:
        print("pixelSearch(): interaction location exceeds the resolution of the screen!")

    item = subprocess.Popen(["shellcolorgrabber.bat", str(emulator_port), str(resolution_width * interact_y + interact_x)], shell=True, stdout=subprocess.PIPE) #launch subprocess to send commands to adb using .bat files
    for stdoutline in item.stdout:
        stdoutlineformatted += str(stdoutline, 'utf-8')

    temp = "".join(stdoutlineformatted[stdoutlineformatted.find('00000000') + 10:stdoutlineformatted.find('ff')].split()) #grab the bytes only needed which are RGB seperated by spaces and strip the whitespace
    return temp


#BOT CAPABILITY [actions, settings, inventory-management...]

def centerCamera(): #Orients the camera to the North using the compass
    clickRandom(789, 38, 759, 10) #Clicks on the compass
    sleepRandom(0.5, 4)
    clickDragDown(100, 51, 700, 360, 120, 200) #Drags down to have the camera point as far down as possible to the character
    sleepRandom(1, 3)

def setZoomLevel(): #Opens settings and adjusts zoom to an exact setting, in the middle of the bar
    #go to settings
    clickRandom(909, 426, 943, 465)
    sleepRandom(1,3)
    #click middle of zoom bar
    click(810, 295)
    sleepRandom(1,3)
    #close settings
    clickRandom(909, 426, 943, 465)
    sleepRandom(1,3)

def dropItem(itemSlotToDrop): #drops an item from a specific slot in the backpack
    #put the last slot at the front of the array so when you do a modulous division anything in the last slot returns 0 which
    #still will give the correct slot value without logic
    inventoryCoords = [[850, 715, 760, 805, 850], #top left x
            [468, 236, 275, 313, 352, 391, 429, 468], #top left y
            [877, 742, 787, 832, 877], #bottom right x
            [491, 262, 301, 339, 375, 414, 452, 491]] #bottom right y

    clickRandom((inventoryCoords[0][(itemSlotToDrop % 4)]), 
        (inventoryCoords[1][math.ceil(itemSlotToDrop / 4)]), 
        (inventoryCoords[2][(itemSlotToDrop % 4)]), 
        (inventoryCoords[3][math.ceil(itemSlotToDrop / 4)]))    

def dropInventory(itemSlotsToSkip): #drops all items in invetory skipping first slots up to a set amount //  can be set to 0 to clear inventory completely
    for x in range(itemSlotsToSkip, 29):
        dropItem(x)
        sleepRandom(0.15, 1.15)

def mineRock(oreColorThreshold, maxWaitAmount, oreHexColorString, color_X, color_Y, clickArea_x1, clickArea_y1, clickArea_x2, clickArea_y2): #harvest any resource given the custom arguments
    depleted = False
    shouldBreak = False
    for x in range(1, maxWaitAmount): #wait for rock to not be depleted of ore
        if shadeVariationTest(pixelSearch(color_X, color_Y), oreHexColorString, oreColorThreshold):
            break
        else:
            if x == maxWaitAmount - 1:
                depleted = True
                print('mineRock(): rocks I am mining seem to be depleted.')
            sleep(0.5)
            continue
    if not depleted:
        clickRandom(clickArea_x1, clickArea_y1, clickArea_x2, clickArea_y2) #click respawned ore
        sleepRandom(0.25,1) #wait for mining
        for x in range(1, maxWaitAmount): #wait for rock to be depleted of ore
            if not shadeVariationTest(pixelSearch(color_X, color_Y), oreHexColorString, oreColorThreshold):
                for y in range(1, 4):
                    if not shadeVariationTest(pixelSearch(color_X, color_Y), oreHexColorString, oreColorThreshold):
                        shouldBreak = True
                    else:
                        sleep(0.5)
                        continue
                if shouldBreak:
                    break
            else:
                sleep(0.5)
                continue


#BOTTING SCRIPTS [skilling, money-makers...]

def mineIronOreSouthWestVarrock(): #Mine South-West of Varrock contains two close iron rocks, stand between both iron rocks, one on the West, one to the North
    mineRock(10, 15, '795545', 440, 285, 426, 258, 452, 289) #West iron rock
    mineRock(10, 15, '765143', 463, 225, 466, 219, 496, 244) #North iron rock

def main():
    #TODO call python script specifically for that emulator(port)
    #TODO when sending RANDOM variables to a batch file format them to 1 decimal place maximum [reduce memory sent]
    #TODO random circle ontop of randomness [multiple layers of randomness]
    #TODO add area support to pixelSearch instead of a single pixel
    #TODO toggle the run off automatically on start
    #TODO add new capability walking to the bank from SW varrock
    #TODO add support for lumbridge tin and copper
    #TODO add support for SW varrock tin and copper
    #TODO add option for either droping materials or banking them


    if reset_camera == 'True': #second argument on script startup, if true will reset camera; True/False
        centerCamera()
        setZoomLevel()

    for current_loop in range(0,int(loop_amount)): #first argument on script startup, loops the queued scripts until set limit is reached, can be set to any integer
        if ((current_loop % 14) == 0) and (current_loop != 0):
            dropInventory(0)
        if ((current_loop % (math.floor(int(loop_amount) / 4))) == 0):
            print("main(): Current Loop is: " + str(current_loop) + " out of " + str(loop_amount))
        
        #SCRIPT QUEUE
        mineIronOreSouthWestVarrock()

    print("\n######################\n#######finished#######\n######################\n")

main()