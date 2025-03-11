import pyautogui as auto
import time as t

def selectComp(row=1):
    x = 40 * row
    auto.moveTo(187+x,947)
    t.sleep(0.1)

def selectDevice(row=1):
    x = 35 * row
    auto.moveTo(-20+x,958)
    t.sleep(0.1)

def moveFromCurrent(x,y):
    x += auto.position().x
    y += auto.position().y
    auto.moveTo(x,y)
    t.sleep(0.1)

def click():
    auto.click()
    t.sleep(0.1)
    
def goto(x,y):
    auto.moveTo(x,y)
    t.sleep(0.1)

def write(thing):
    auto.write(thing)
