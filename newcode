# -*- coding: utf-8 -*-
import os

def clear(): print ("\n" * 50)
clear() 

class cllanguage:
    pass
russian = cllanguage()
english = cllanguage()
japanese = cllanguage()

def language_function():
 print ("select language (russian, english, japanese)")
 language = input()
 print ("you have selected %s" % language)
 return language

from _rudescription import *
from _endescription import *
from _jpdescription import *

def name_function():
    print (nametext)
    pname = input()
    x = pname.isalpha()
    if x is True:
        print (hellotext + pname)
        return pname
    else:
        print (errortext)
        name_function()

class jobtype:
    def datamage_function(self, mana):
        self.name = ""
        self.mana = mana
        self.hp = 1

mage_cl = jobtype()
warrior_cl =  jobtype()
clerck_cl  =  jobtype()

telemage = jobtype()
telemage.mana = 50
telemage.hp = 100
elemage = jobtype()
elemage.mana = 100
telemage.hp = 50
scromage = jobtype()
scromage.mana = 50
scromage.hp = 100

def class_function():
        print (clchoosetext)
        trueinput = True
        while trueinput:
            classtype = input()
            if classtype == mage or classtype == warrior or classtype == clerck:
            #x = isinstance(classtype,jobtype)
            #if x == True:
                clear()
                print ((clchosentext) + classtype)
                trueinput = False
                return classtype
            else:
                clear()
                print (errortext)

def magechoice_function():
    print (magechoicetext)
    magechoice = input()
    if magechoice == elements or magechoice == telepathy or magechoice == scrolls:
        clear()
        print (clchosentext + magechoice)
    elif magechoice == "check" + elements:
        clear()
        print (elementstext)
        trueback = True
        while trueback:
            back_ = input()
            if back_ == "return":
                clear()
                magechoice_function()
                trueback = False
            else:
                print (errortext)
    elif magechoice == "check" + telepathy:
        clear()
        print (telepathytext)
        trueback = True
        while trueback:
            back_ = input()
            if back_ == "return":
                clear()
                magechoice_function()
                trueback = False
        else:
            print (errortext)
    elif magechoice == "check" + scrolls:
        clear()
        print (scrollstext)
        trueback = True
        while trueback:
            back_ = input()
            if back_ == "return":
                clear()
                magechoice_function()
                trueback = False
        else:
            print (errortext)

def warriorchoice_function():
    print (warriorchoicetext)
    warriorchoice = input()
    if warriorchoice == highclass or warriorchoice == lowclass or warriorchoice == criminal:
        clear()
        print (clchosentext) + warriorchoice
    elif warriorchoice == "check" + highclass:
        clear()
        print (highclasstext)
        trueback = True
        while trueback:
            back_ = input()
            if back_ == "return":
                clear()
                warriorchoice_function()
                trueback = False
        else:
            clear()
            print (errortext)
    elif warriorchoice == "check" + lowclass:
        clear()
        print (lowclasstext)
        trueback = True
        while trueback:
            back_ = input()
            if back_ == "return":
                clear()
                warriorchoice_function()
                trueback = False
        else:
            print (errortext)
    elif warriorchoice == "check" + criminal:
        clear()
        print (criminaltext)
        trueback = True
        while trueback:
            back_ = input()
            if back_ == "return":
                clear()
                warriorchoice_function()
                trueback = False
        else:
            clear()
            print (errortext)

from FUNCTIONNEW import classtype
def mainchoice_function():
    if classtype == mage:
        magechoice_function()
    elif classtype == warrior:
        warriorchoice_function()
    elif classtype == clerck:
        print (chclercktext)
    else:
        print (classtype)

def racechoice_():
    race_ = input()
    if race_ == human or race_ == hothuman or race_ == coldhuman:
        clear()
        print (clchosentext) + race_
    else:
        clear()
        print (errortext)
        racechoice_()

class points:
    all_points = 20
