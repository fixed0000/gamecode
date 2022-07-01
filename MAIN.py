import os
import sys
import locale
import threading, time

# -*- coding: utf-8 -*-

def clear(): print ("\n" * 50)
clear() 
from LANGUAGE import *
from enum import Enum
from NEWCODE import name_function, language_function, class_function, mainchoice_function, racechoice_, _,createfunction
from stats import inputNumber

language_function()

def MainMenu():
    print (_('gamemenu'))
    menutext = input()
    if menutext == "1":
        clear()
        createfunction()
    elif menutext == "2":
        clear()
        print (_('notreadyyet'))
    elif menutext == "3":
       clear()
       surefunction()

def surefunction():
        clear()
        print ("Are you sure?")
        answer = input ()
        if answer.lower() == "yes":
           reallysurefunction()
        elif answer.lower() == "no":
           MainMenu()
        else:
            surefunction()
def reallysurefunction():
        clear()
        print ("Are you really sure?")
        answer = input ()
        if answer.lower() == "yes":
           t3 = threading.Timer(3.00, print ("Wait"))
           t3.start()
           time.sleep(2.9)
           t3.cancel()
           clear()
           print ("Press Alt+F4 to exit")
        elif answer.lower() == "no":
           MainMenu()
        else:
            reallysurefunction()

MainMenu()