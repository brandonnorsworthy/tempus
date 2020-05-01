import subprocess
import random
from sys import argv

script, interact_x, interact_y = argv

emulator_port = int(5555) #hard coded for testing allows for all emulators to be interacted with apon change
interact_x = int(interact_x)
interact_y = int(interact_y)
resolution_width = int(960)
resolution_height = int(540)
stdoutlineformatted = "" #formatted byte string from byte variable stdoutline

if interact_x > resolution_width or interact_y > resolution_height:
    print("Interaction location to great!")

item = subprocess.Popen(["shellcolorgrabber.bat", str(emulator_port), str(resolution_width * interact_y + interact_x)], shell=True, stdout=subprocess.PIPE) #launch subprocess to send commands to adb using .bat files
for stdoutline in item.stdout:
    stdoutlineformatted += str(stdoutline, 'utf-8')

temp = "".join(stdoutlineformatted[stdoutlineformatted.find('00000000') + 10:stdoutlineformatted.find('ff')].split()) #grab the bytes only needed which are RGB seperated by spaces and strip the whitespace

if temp == '5a3a2e':
    item = subprocess.Popen(["shellinputtap.bat", str(emulator_port), str(interact_x), str(interact_y)], shell=True, stdout=subprocess.PIPE)

print(temp)