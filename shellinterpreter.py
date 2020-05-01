import subprocess
import random
from sys import argv

interact_x, interact_y = argv

emulator_port = 5555 #hard coded for testing allows for all emulators to be interacted with apon change
resolution_width = 960
resolution_height = 540
stdoutlineformatted = "" #formatted byte string from byte variable stdoutline

item = subprocess.Popen(["shellcolorgrabber.bat", str(emulator_port), str(interact_x),str(interact_y),str(resolution_width * interact_x + interact_y)] , 
                         shell=True, stdout=subprocess.PIPE) #launch subprocess to send commands to adb using .bat files
for stdoutline in item.stdout:
    stdoutlineformatted += str(stdoutline, 'utf-8')

temp = "".join(stdoutlineformatted[10:18].split()) #grab the bytes only needed which are RGB seperated by spaces and strip the whitespace
print(temp)