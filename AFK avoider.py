#AFK avoider
import pyautogui as pgui
import random
import time

def ismoving():
    initial=pgui.position()
    time.sleep(1)
    final=pgui.position()
    if initial==final:
        return False
    else:
        return True

#make this so it moves after checking if the mouse has moved for a certain amount of time and have a breakout function
while True:
    x=random.randint(800,1000)
    y=random.randint(400,600)
    pgui.moveTo(x,y,0.5)#check functioning
    time.sleep(5)


