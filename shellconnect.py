import subprocess
import random
import time
from sys import argv

def connectToBluestacks():
    connections = []
    stdoutlineformatted = ""
    item = subprocess.Popen(["shellconnect.bat"], shell=True, stdout=subprocess.PIPE) #launch subprocess to send commands to adb using .bat files
    for stdoutline in item.stdout:
        stdoutlineformatted += str(stdoutline, 'utf-8')
    time.sleep(2)

    ##IF YOU SEND SHELLDEVICES IT RETURNS MULTIPLE LINES OF THE SAME PORT SO DISABLE IT SO IT DOESNT GET LOGGED TWICE
    #item = subprocess.Popen(["shelldevices.bat"], shell=True, stdout=subprocess.PIPE) #launch subprocess to send commands to adb using .bat files
    #for stdoutline in item.stdout:
    #    stdoutlineformatted += str(stdoutline, 'utf-8')

    if stdoutlineformatted.find('localhost') == -1:
        temp = ''
    else:
        temp = stdoutlineformatted[stdoutlineformatted.find('localhost') + 10:len(stdoutlineformatted)-1].split('localhost:') #grab only the ports
    for x in range(0,len(temp)):
        trim = temp[x]
        connections.insert(x,int(trim[0:4]))
    return connections