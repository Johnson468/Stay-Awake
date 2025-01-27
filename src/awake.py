import pyautogui
import time
import sys
from datetime import datetime
from screeninfo import get_monitors
pyautogui.FAILSAFE = False
numMin = None
xDirection = 0
aspectRatio = 0

if ((len(sys.argv) <2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 3
else:
    numMin = int(sys.argv[1])

if ((len(sys.argv) < 3) or sys.argv[2].isalpha() or int(sys.argv[1] <0)):
    xDirection = 0
else:
    xDirection = abs(int(sys.argv[2]))


def determineAspectRatio():
    monitors = get_monitors()
    primaryMonitor = None
    for monitor in monitors:
        if (monitor.is_primary):
            primaryMonitor = monitor
    return primaryMonitor.width/primaryMonitor.height

def move():
        while(True):
            x=0
            while(x<numMin):
                x+=1
            for i in range(0,200):
                pyautogui.moveTo(((xDirection+i)*aspectRatio),240+(i*aspectRatio))
                print(str(pyautogui.position()))
            pyautogui.moveTo(1,1)
            for i in range(0,3):
                pyautogui.press("shift")
            print("Movement made at {}".format(datetime.now().time()))
            time.sleep(60)


aspectRatio = determineAspectRatio()
move()
