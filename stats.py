from LANGUAGE import *
from NEWCODE import _
from Entities import Character

def clear(): print ("\n" * 50)
clear() 

all_points = 20

def inputNumber(minnum,maxnum):
    number = input()
    if number.isdigit():
        clear()
        print (_('errortext'))
        inputNumber(minnum,maxnum)
    elif number < minnum or number > maxnum:
        clear()
        print (_('errortext'))
        inputNumber(minnum,maxnum)
    else:
        return number