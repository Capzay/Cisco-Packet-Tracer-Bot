import time as t
from moveFuncs import *

def SetupComputer(offset,count,base,dfgwBool,dfgw):
    selectDevice(2)
    click()
    selectComp()
    click()
    moveFromCurrent(0,-200-offset)
    click()
    goto(134,917)
    for i in range(5):
        click()
    goto(227,747-offset)
    click()
    goto(773,268)
    click()
    moveFromCurrent(0,110)
    click()
    goto(1115,474)
    click()
    write(f"192.168.{base}.{count}")
    moveFromCurrent(0,300)
    click()
    goto(755,323)
    click()
    if dfgwBool:
        goto(1014,489)
        click()
        write(f"{dfgw}")
    goto(1348,228)
    click()


