import subprocess
import random
from sys import argv

item = subprocess.Popen(["shellconnect.bat"], shell=True, stdout=subprocess.PIPE) #launch subprocess to send commands to adb using .bat files