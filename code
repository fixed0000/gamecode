import os
import locale

#global name
global race_
global ruclass_
global enclass_
global jpclass_
global back_
global rumagechoice
global magechoice
global jpmagechoice
global warriorchoice
global all_points
global charisma_int
global points_int
global points 
global strength_int
global points1
global strength_ 
global points1_int
global agility_int
global points2_int
global points2
global intelligence_int
global points3

from appearance import *
from _endescription import *

# -*- coding: utf-8 -*-
# coding: utf8

def clear(): print ("\n" * 50)
clear() 

#name = input()
#print ("hello " + name)

def class_function(language):
 if language == "russian":
  print (u"""выберите свой класс (маг, воин, клерк)
Загрузка… ████████████████████████ 00%
класс маг - редкий и изолированный от общества класс. имеет несколько способностей, которые можно выбрать
класс воин - самый могущественный класс. имеет возможность выбора одного из специальных социальных статусов
класс клерк - самый распространенный класс. не имеет никаких спобсоностей или статуса, сложен для игры
Загрузка… ████████████████████████ 00%""")
  ruclass_ = input()
  if ruclass_ == "воин" or ruclass_ == "маг" or ruclass_ == "клерк":
        clear()
        print (u"вы выбрали класс " + ruclass_)
  else:
        clear()
        print ("выберите еще раз")
        class_function()
 elif language == "english":
      # from lang_en import text2
      print ("""choose your class (mage,warrior,clerck)
Loading… ████████████████████████ 00%
mage class - rare and isolated from others class. have some special abilities which you can choose
warrior class - the most powerful class. have an option to choose one of special social statuses
clerck class - the most common class. have no special abilities or status and hard to play
Loading… ████████████████████████ 00%""")
      enclass_ = input()
      if enclass_ == "warrior" or enclass_ == "mage" or enclass_ == "clerck":
        clear()
        print ("you have chosen " + enclass_ + " class")
      else:
        clear()
        print ("choose again")
        class_function(language)
 else:
      # from lang_jp import text2
      print (u"""クラスを選んでください（魔法使い、戦士、店員）
読み込み中... ████████████████████████ 00%
魔法使いクラス - 珍しい遠隔のクラス。
████████████████████████ 00%""")
      jpclass_ = input()
      if jpclass_ == "戦士" or jpclass_ == "魔法使い" or jpclass_ == "店員":
        clear()
        print (u"%sを選びました" % jpclass_)
      else:
        clear()
        print (u"もう一度選んでください")
        class_function(language)

#class_function(language)
def rudescription_elemfunction(language):
            print (u"""это способность позволяющая использовать 4 стихии: воду, землю, огонь и воздух. это может быть полезно в боях
напишите 'return' если хотите вернуться назад""")
            back_ = input()
def rudescription_telefunction(language): 
            print (u"""это способность позволяющая читать мысли людей и других существ, это может быть полезной особенностью в общении с другими
напишите 'return' если хотите вернуться назад""")
            back_ = input()
def rudescription_scrofunction(language):
            print (u"""это способность позволяющая использовать свитки, но она абсолютно бесполезна если не знать где найти их
напишите 'return' если хотите вернуться назад""")
            back_ = input()
def jpdescription_elemfunction(language):
            print (u"""that's ability that allows you to use four elements: water, earth, fire and air. it may be a good trait at fighting
write 'return' if you want to return""")
            back_ = input()
def jpdescription_telefunction(language): 
            print (u"""that's ability that allows you to read people's and other creatures'thoughts, it may be a good trait at talking to others
write 'return' if you want to return""")
            back_ = input()
def jpdescription_scrofunction(language):
            print (u"""that's ability to use scrolls, but it's completely useless if you don't know where to find them
write 'return' if you want to return""")
            back_ = input()

def magechoice_function(language):
    if language == "russian":
        print (u"""Loading… []]]]]]]████████████████ 30%
для вашего класса есть несколько вариантов способностей (4 стихии, телепатия, свитки)
если вы хотите узнать детали, напишите 'read about' и выберите вариант о котором хотите узнать подробнее. если вы готовы продолжить, напишите вариант, который вы выбрали
Loading… []]]]]]]████████████████ 30%""")
        rumagechoice = input()
        if rumagechoice == "4 стихии" or rumagechoice == "телепатия" or rumagechoice == "свитки":
         clear()
         print (u"вы выбрали способность %s" % (rumagechoice))
        elif rumagechoice == "read about 4 стихии":
         clear()
         rudescription_elemfunction(language)
         if back_ == "return":
            clear()
            magechoice_function(language)
         else:
            print ("неправильный ввод. напишите снова")
            rudescription_elemfunction(language)
        elif rumagechoice == "read about телепатия":
            clear()
            rudescription_telefunction(language)
            if back_ == "return":
                clear()
                magechoice_function(language)
            else:
                clear()
                print ("неправильный ввод. напишите снова")
        elif rumagechoice == "read about свитки":
            clear()
            rudescription_scrofunction(language)
            if back_ == "return":
             clear()
             magechoice_function(language)
            else:
                clear()
                print ("неправильный ввод. напишите снова")
        else:
            clear()
            print ("неправильный ввод. напишите снова")
            magechoice_function(language)
    elif language == "english":
       def enmagechoice_function():
        print ("""Loading… []]]]]]]████████████████ 30%
you have several options in magic abilities for your class (four elements, telepathy, scrolls)
if you want to check details of any option, write 'read about' and choose an option which you want to check. if you're ready to choose, write an option what you want to choose
Loading… []]]]]]]████████████████ 30%""")
        magechoice = input()
        if magechoice == "four elements" or magechoice == "telepathy" or magechoice == "scrolls":
         clear()
         print ("you have chosen %s ability" % (magechoice))
        elif magechoice == "read about four elements":
         clear()
         endescription_elemfunction(language)
         if back_ == "return":
            clear()
            magechoice_function(language)
         else:
            print ("incorrect. write again")
            endescription_elemfunction(language)
        elif magechoice == "read about telepathy":
            clear()
            jpdescription_telefunction(language)
            if back_ == "return":
                clear()
                magechoice_function(language)
            else:
                clear()
                print ("incorrect. write again")
        elif magechoice == "read about scrolls":
            clear()
            endescription_scrofunction(language)
            if back_ == "return":
             clear()
             magechoice_function(language)
            else:
                clear()
                print ("incorrect. write again")
        else:
            clear()
            print ("write again")
            magechoice_function(language)
       enmagechoice_function()
    else:
        print (u"""Loading… []]]]]]]████████████████ 30%
クラスがいくつかのオプションを持っています (四大, 以心伝心, スクロール)
if you want to check details of any option, write 'read about' and choose an option which you want to check. if you're ready to choose, write an option what you want to choose
Loading… []]]]]]]████████████████ 30%""")
        jpmagechoice = input()
        if jpmagechoice == "四大" or jpmagechoice == "以心伝心" or jpmagechoice == "スクロール":
         clear()
         print ("you have chosen %s ability" % (jpmagechoice))
        elif magechoice == "read about 四大":
         clear()
         endescription_elemfunction(language)
         if back_ == "return":
            clear()
            magechoice_function(language)
         else:
            print ("incorrect. write again")
            endescription_elemfunction(language)
        elif magechoice == "read about 以心伝心":
            clear()
            endescription_telefunction(language)
            if back_ == "return":
                clear()
                magechoice_function(language)
            else:
                clear()
                print ("incorrect. write again")
        elif jpmagechoice == "read about スクロール":
            clear()
            endescription_scrofunction(language)
            if back_ == "return":
             clear()
             magechoice_function(language)
            else:
                clear()
                print ("incorrect. write again")
        else:
            clear()
            print ("write again")
            magechoice_function(language)

def warriorchoice_function(language):
    print ("""you have several options in warrior's social status (high class, low class, criminal)
if you want to check details of any option, write 'read about' and choose an option which you want to check. if you're ready to choose, write an option what you want to choose""")
    warriorchoice = input()
    if warriorchoice == "high class" or warriorchoice == "low class" or warriorchoice == "criminal":
        print ("you have chosen %s social status" % (warriorchoice))
    elif warriorchoice == "read about high class":
       des_warhigh(language)
       if back_ == "return":
        clear()
        warriorchoice_function(language)
       else:
        print ("incorrect. write again")
        des_warhigh(language)
    elif warriorchoice == "read about low class":
       des_warlow()
       if back_ == "return":
        clear()
        warriorchoice_function(language)
       else:
        print ("incorrect. write again")
        des_warlow(language)
    elif warriorchoice == "read about criminal":
       des_warcrim(language)
       if back_ == "return":
        clear()
        warriorchoice_function(language)
       else:
        print ("incorrect. write again")
        des_warcrim()
    else:
        clear()
        print ("write again")
        warriorchoice_function(language)

def clerckchoice_function(language):
    print ("""you don't have any additional traits in this class""")

def mainchoice_function(language, ruclass_, enclass_, jpclass_):
    if language == "russian":
        if ruclass_ == "маг":
            magechoice_function(language)
        elif ruclass_ == "воин":
            warriorchoice_function(language)
        elif ruclass_ == "клерк":
            clerckchoice_function(language)
    elif language == "english":
        if enclass_ == "mage":
            magechoice_function(language)
        elif enclass_ == "warrior":
            warriorchoice_function(language)
        elif enclass_ == "clerck":
            clerckchoice_function(language)
    else:
        if jpclass_ == "魔法使い":
            magechoice_function(language)
        elif jpclass_ == "戦士":
            warriorchoice_function(language)
        elif jpclass_ == "店員":
            clerckchoice_function(language)

def race_function(language):
    if language == "russian":
        print ("выберите расу (человек, горячий человек, холодный человек)")
        race_ = input()
        if race_ == "человек" or race_ == "горячий человек" or race_ == "холодный человек":
            print ("вы выбрали расу "+ race_)
        else:
            clear()
            print ("выберите снова")
            race_function(language)
    elif language == "english":
        print ("choose your race (human, hot human, cold human)")
        race_ = input()
        if race_ == "human" or race_ == "hot human" or race_ == "cold human":
            print ("you have chosen "+ race_ + " race")
        else:
            clear()
            print ("choose again")
            race_function(language)
    else:
        print ("choose your race (human, hot human, cold human)")
        race_ = input()
        if race_ == "human" or race_ == "hot human" or race_ == "cold human":
            print ("you have chosen "+ race_ + " race")
        else:
            clear()
            print ("choose again")
            race_function(language)

#race_function(language)

all_points = 20

def charisma_function(language):
    print ("you have 20 points. set you charisma level from 0 to 20")
    charisma_int = input()
    if charisma_int.isdigit():
        if int(charisma_int) >-1 and int(charisma_int) <21:
         points_int = all_points - int(charisma_int)
         points = str(points_int)
         print ("you have " + str(charisma_int) + " points in charisma")
        else:
         clear()
         print ("incorrect amount of points. set again")
         charisma_function(language)
    else:
        clear()
        print ("stop doing cringe. this isn't number you dumb. write again")
        charisma_function(language)

#clear()
#charisma_function(language)

def strength_function(language):
    print ("you have " + points + " points. set you strength level from 0 to 20")
    strength_int = input()
    if strength_int.isdigit():
        strength_ = str(strength_int)
        if int(strength_int) >-1 and int(strength_int)<=points_int:
         points1_int = points_int - int(strength_int)
         points1 = str(points_int)
         print ("you have " + strength_int + " points in strength")
        else:
          print ("incorrect amount of points. set again")
          clear()
          strength_function(language)
    else:
        clear()
        print ("stop doing cringe. this isn't number you dumb. write again")
        strength_function(language)

#clear()
#strength_function(language)

def agility_function(language):
    print ("you have " + points1 + " points. set you agility level from 0 to 20")

    agility_int = input()
    if agility_int.isdigit():
        if int(agility_int) >-1 and int(agility_int) <=points1_int:
         points2_int = int(points1) - int(agility_int)
         points2 = str(points2_int)
         print ("you have " + agility_int + " points in agility")
        else:
         clear()
         print ("incorrect amount of points. set again")
         agility_function(language)
    else:
        clear()
        print ("stop doing cringe. this isn't number you dumb. write again")
        agility_function(language)

#clear()
#agility_function(language)

def intelligence_function(language):
    print ("you have " + points2 + " points. set you intelligence level from 0 to 20")
    intelligence_int = input()
    if intelligence_int.isdigit():
        if int(intelligence_int) >-1 and int(intelligence_int) <=points2_int:
         points3 = int(points2) - int(intelligence_int)
        else:
            print ("incorrect amount of points. set again")
            clear()
            intelligence_function(language)
            print ("you have " + intelligence_int + " points in intelligence")
    else:
        clear()
        print ("stop doing cringe. this isn't number you dumb. write again")
        intelligence_function(language)

#clear()
#intelligence_function(language)

#appearance_function()
#upperclothes_function(language)
