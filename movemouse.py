import sys
import time
import pyautogui as pg
import random

def checkCoordinates(_X, _Y):
    return ((_X in range(0, pg.size()[0])) and (_Y in range(0, pg.size()[1])))

if (len(sys.argv) < 2):
	print("Usage: python mousemove.py speed sleeptime")
	sys.exit()

# Get parameters from the command line
speed = int(sys.argv[1])
sleepT = int(sys.argv[2])
# If parameters ou of range, then exit the program
if(speed > 30 or sleepT > 600 or speed < 0 or sleepT < 0):
    print("speed MUST be in [0:30]s\nsleep time Must be in [0:600]s")
    sys.exit()
# get current mouse positions
x, y = pg.position()
screenX, screenY = pg.size()
print(screenX, screenY)
try:
    while True:
        # Move the mouse at random positions
        x += random.randint(-x, screenX - x)
        y += random.randint(-y, screenY - y)
        print("coordinates of the mouse {}, {}".format(x, y))
        if(checkCoordinates(x, y)):
            pg.moveTo(x, y, speed)
        pg.press('f15')
        time.sleep(sleepT)
except KeyboardInterrupt:
    print("Program exited")