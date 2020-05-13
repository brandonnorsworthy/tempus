import subprocess
import random
import time
import math
from sys import argv

#TODO call python script specifically for that emulator(port)
#TODO webwalker interface
#TODO shows where all the connected bots are one a map
#TODO front end web face for bot control
#TODO when sending RANDOM variables to a batch file format them to 1 decimal place maximum [reduce memory sent]
#TODO random circle ontop of randomness [multiple layers of randomness]
#TODO add area support to pixelSearch instead of a single pixel
#TODO toggle the run off automatically on start
#TODO add new capability walking to the bank from SW varrock
#TODO add support for lumbridge tin and copper
#TODO add support for connecting automatically
#TODO add function for entering text from script
#TODO add basic UI so i dont have to type shit out
#TODO add more clarification to comments
#TODO ADD BREAKS WATCH YOUTUBE VIDEO FOR TIMES
#TODO go one by one through functions and see if they can be more efficent or smaller
#TODO add support for SW varrock tin and copper
#TODO add option for either droping materials or banking them
#TODO circle of randomness
#TODO add power woodcutting
#TODO add random ge purchases
#TODO add a distraction chance while performing a repetative action
    #TODO "accidentally" click a random hotbar
    #TODO move the camera around and then return it back
    #TODO stop interacting for a random period of time up to ~5 minutes

emulator_port = 5555 #hard coded for testing allows for all emulators to be interacted with apon change
resolution_width = 1280
resolution_height = 720
loop_amount = 0

#auto crunch area

def initiate(local_emulator_port, script, loop_amount):
    emulator_port = local_emulator_port
    print(emulator_port)

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

    #trim the RGB format eg (255, 255, 255) -> ['255','255','255'] to only numbers and put into an array to be usable for threshold comparison
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
    clickRandom(1029, 11, 1073, 54) #Clicks on the compass
    sleepRandom(0.5, 4)
    clickDragDown(200, 100, 700, 360, 168, 222) #Drags down to have the camera point as far down as possible to the character
    sleepRandom(1, 3)

def setZoomLevel(): #Opens settings and adjusts zoom to an exact setting, in the middle of the bar
    #go to settings
    clickRandom(1229, 570, 1276, 625)
    sleepRandom(1,3)
    #click middle of zoom bar
    clickRandom(1100, 385, 1100, 395)
    sleepRandom(1,3)
    #close settings
    clickRandom(1229, 570, 1276, 625)
    sleepRandom(1,3)

def clickItem(itemSlotToDrop): #clicks an item from a specific slot in the backpack
    #put the last slot at the front of the array so when you do a modulous division anything in the last slot returns 0 which
    #still will give the correct slot value without logic
    inventoryCoords = [[1152, 972, 1032, 1092, 1152], #top left x
        [627, 317, 368, 420, 472, 524, 574, 627], #top left y
        [1189, 1009, 1069, 1129, 1189], #bottom right x
        [656, 346, 396, 449, 502, 553, 604, 656]] #bottom right y

    clickRandom((inventoryCoords[0][(itemSlotToDrop % 4)]), 
        (inventoryCoords[1][math.ceil(itemSlotToDrop / 4)]), 
        (inventoryCoords[2][(itemSlotToDrop % 4)]), 
        (inventoryCoords[3][math.ceil(itemSlotToDrop / 4)]))    

def dropInventory(itemSlotsToSkip): #drops all items in invetory skipping first slots up to a set amount //  can be set to 0 to clear inventory completely
    for x in range(itemSlotsToSkip, 29):
        clickItem(x)
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
                print('mineRock(): The rocks I am mining seem to be depleted.')
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

def fixPositionVarrockEastBank():
    inTheCorrectPosition = False

    while not inTheCorrectPosition:
        leftSidePositionCorrect = bool(shadeVariationTest(pixelSearch(1146, 178), 'fcfc03', 10))
        rightSidePositionCorrect = bool(shadeVariationTest(pixelSearch(1175, 178), 'fcfc03', 10))
        #if in the right spot
        if (leftSidePositionCorrect and rightSidePositionCorrect):
            print("perfect")
            inTheCorrectPosition = True
            continue
        elif not leftSidePositionCorrect and rightSidePositionCorrect:
            click(1167, 120)
        elif leftSidePositionCorrect and not rightSidePositionCorrect:
            click(1157, 120)
        else:
            print("fixPositionVarrockEastBank(): got lost exiting script")
            exit()
        sleep(5)

def bankSettings():
    clickRandom()


#WEB WALKER

def walkToVarrockEastBankFromSouthEastMine(): #part of the web walker network with nodes
    click(1184, 24) #1
    sleep(8)
    click(1158, 14) #9
    sleep(9)
    click(1130, 24) #18
    sleep(9)
    click(1099, 38) #27
    sleep(10)
    click(1070, 108) #37
    sleep(8)
    click(1106, 111) #45
    sleep(9)

def walkToSouthEastMineFromVarrockEastBank(): #part of the web walker network with nodes
    click(1266, 122) #2
    sleep(7)
    click(1247, 172) #10
    sleep(6)
    click(1215, 201) #16
    sleep(5)
    click(1210, 204) #21
    sleep(7)
    click(1176, 212) #28
    sleep(5)
    click(1168, 219) #33
    sleep(6)
    click(1158, 204) #39
    sleep(8)
    click(1147, 171) #48
    sleep(9)


#BOTTING SCRIPTS [skilling, money-makers...]

def mineIronOreSouthEastVarrock(): #Mine South-East of Varrock contains two close iron rocks, stand between both iron rocks, one on the East, one to the North
    inventoryFull = False
    powerMining = False

    while not inventoryFull:
        mineRock(15, 15, '735041', 585, 390, 548, 355, 598, 401) #East iron rock
        if shadeVariationTest(pixelSearch(1175, 640), '5c3e2f', 10):
            inventoryFull = True
            print(inventoryFull)
            continue
        mineRock(15, 15, '735041', 622, 309, 606, 299, 652, 341) #North iron rock    
        if shadeVariationTest(pixelSearch(1175, 640), '5c3e2f', 10):
            inventoryFull = True
            print(inventoryFull)
            continue
    
    if not powerMining:
        click(1168, 119) #iron spot
        sleepRandom(1,3)
        walkToVarrockEastBankFromSouthEastMine()
        sleepRandom(10,20)
        fixPositionVarrockEastBank()
        sleep(2)
        bankAtVarrockEastBank()
        sleep(2)
        walkToSouthEastMineFromVarrockEastBank()
        sleep(3)
    return

def bankAtVarrockEastBank(): #bank items at varrock east bank needs expansion
    click(1161, 178) #click on minimap where tellers are
    sleepRandom(7,8)
    clickRandom(608, 400, 653, 440) #click on bank stall
    sleepRandom(7,8)
    clickItem(math.ceil(random.random() * 20) + 1) #deposit an item
    sleep(7)
    click(1162, 78) #walk back to the hotspot outside the bank
    sleep(7)

def main():

    for current_loop in range(1,int(loop_amount) - 1): #first argument on script startup, loops the queued scripts until set limit is reached, can be set to any integer
        if ((current_loop % (math.floor(int(loop_amount) / 4))) == 0): #Keep user updated on progress of current run
            print("main(): Current Loop is: " + str(current_loop) + " out of " + str(loop_amount))
        
        #SCRIPT QUEUE
        mineIronOreSouthEastVarrock()

    print("\n######################\n#######FINISHED#######\n######################\n")

main()