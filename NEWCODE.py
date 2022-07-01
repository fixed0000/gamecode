# -*- coding: utf-8 -*-
import os
import sys

from LANGUAGE import *
from enum import Enum
from LANGUAGE import *
from Entities import *
sys.path.append('C:/Users/ssh21/source/repos/PythonApplication1/PythonApplication1/Entities/entity')
from Entities import Character
from stats import inputNumber

def clear(): print ("\n" * 50)
clear()

localizer = Localizer(Language.RUSSIAN)
def language_function():
 print ("select language (russian, english, japanese)")
 selectedLanguage = input()
 print ("you have selected %s" % selectedLanguage)
 if selectedLanguage.lower() == "russian":
        localizer._lang = Language.RUSSIAN
 elif selectedLanguage.lower() == "english":
        localizer._lang = Language.ENGLISH
 elif selectedLanguage.lower() == "japanese":
        localizer._lang = Language.JAPANESE
 else:
     clear()
     print ("incorrect. write again")
     language_function()

def _(textkey):
    return localizer.localize(textkey)

def name_function():
    print (_('nametext'))
    pname = input()
    x = pname.isalpha()
    if x is True:
        print (_('hellotext' + pname))
        return pname
    else:
        print (_('errortext'))
        name_function()

def class_function():
        print (_('clchoosetext'))
        classtype = input()
        trueinput = True
        while trueinput is False:
            if classtype == _('mage') or classtype == _('warrior') or classtype == _('clerck'):
                clear()
                print (_('clchosentext') + classtype)
            else:
                clear()
                print (_('errortext'))
                trueinput = False
        return classtype

def magechoice_function():
    print (_('magechoicetext'))
    magechoice = input()
    if magechoice == _('elements') or magechoice == _('telepathy') or magechoice == _('scrolls'):
        clear()
        print (_('clchosentext') + magechoice)
    elif magechoice == "check" + _('elements'):
        clear()
        print (_('elementstext'))
        trueback = True
        while trueback:
            back_ = input()
            if back_ == "return":
                clear()
                magechoice_function()
                trueback = False
            else:
                print (_('errortext'))
    elif magechoice == "check" + _('telepathy'):
        clear()
        print (_('telepathytext'))
        trueback = True
        while trueback:
            back_ = input()
            if back_ == "return":
                clear()
                magechoice_function()
                trueback = False
        else:
            print (_('errortext'))
    elif magechoice == "check" + _('scrolls'):
        clear()
        print (_('scrollstext'))
        trueback = True
        while trueback:
            back_ = input()
            if back_ == "return":
                clear()
                magechoice_function()
                trueback = False
        else:
            print (_('errortext'))

def warriorchoice_function():
    print (_('warriorchoicetext'))
    warriorchoice = input()
    if warriorchoice == _('highclass') or warriorchoice == _('lowclass') or warriorchoice == _('criminal'):
        clear()
        print (_('clchosentext')) + warriorchoice
    elif warriorchoice == "check" + _('highclass'):
        clear()
        print (_('highclasstext'))
        trueback = True
        while trueback:
            back_ = input()
            if back_ == "return":
                clear()
                warriorchoice_function()
                trueback = False
        else:
            clear()
            print (_('errortext'))
    elif warriorchoice == "check" + _('lowclass'):
        clear()
        print (_('lowclasstext'))
        trueback = True
        while trueback:
            back_ = input()
            if back_ == "return":
                clear()
                warriorchoice_function()
                trueback = False
        else:
            print (_('errortext'))
    elif warriorchoice == "check" + _('criminal'):
        clear()
        print (_('criminaltext'))
        trueback = True
        while trueback:
            back_ = input()
            if back_ == "return":
                clear()
                warriorchoice_function()
                trueback = False
        else:
            clear()
            print (_('errortext'))

def mainchoice_function():
    if class_function == _('mage'):
        magechoice_function()
    elif class_function == _('warrior'):
        warriorchoice_function()
    elif class_function == _('clerck'):
        print (_('chclercktext'))
    else:
        print (_('classtype'))

def racechoice_():
    race_ = input()
    if race_ == 'human' or race_ == 'hothuman' or race_ == 'coldhuman':
        clear()
        print ('clchosentext') + race_
    else:
        clear()
        print (_('errortext'))
        racechoice_()

def createfunction():
    name_function()
    class_function()
    mainchoice_function()
    racechoice_()
    Character.chr = inputNumber(0,20)