from setupRouter import SetupRouter
from setupComputer import SetupComputer
import time as t

while True:
    choice = input("To setup router type 'r' \nto set up computer type 'c' \nto exit type 'e'\n")
    if choice.strip().lower() == "r":
        have = int(input("How many do you currently have?"))
        runs = int(input("How many do you want?"))
        if have != 0:
            count = have * 2
        else:
            count = 0
        t.sleep(4)
        offset = 0
        for i in range(1,runs+1):
            SetupRouter(offset,count)
            offset += 50
            count += 2
            
    elif choice.strip().lower() == "c":
        runs = int(input("How many do you want?"))
        baseIP = int(input("What is the base ip? e.g. 192.168.x.0"))
        have = int(input("How many do you currently have with that base IP?"))
        dfgw = input("Do you want a default gateway? y/n")

        if dfgw.strip().lower() == "y":
            dfgwIP = int(input("What is the default gateway number 192.168.x.1 (the x)"))
            dfgw = f"192.168.{dfgwIP}.1"
            dfgwBool = True
        else:
            dfgwBool = False

        if have != 0:
            count = have
        else:
            count = 0

        t.sleep(4)
        offset = 0
        for i in range(1,runs+1):
            count += 1
            SetupComputer(offset,count,baseIP,dfgwBool,dfgw)
            offset += 50
    elif choice.strip().lower() == "e":
        break
