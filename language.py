import os
import locale
from enum import Enum


class Language(Enum):
    RUSSIAN = 0
    ENGLISH = 1
    JAPANEESE = 2


class Localizer:
    _lang = Language.RUSSIAN

    dictionary = {
        'nametext': ["напишите имя вашего персонажа", "write your character's name", "キャラクターの名前を書き込んでください"],
        'hellotext': ["добро пожаловать, ", "welcome, ", "いらっしゃい、"],
        'mage': ["маг", "mage", "魔法使い"],
        'warrior': ["воин", "warrior", "戦士"],
        'clerck': ["клерк", "clerck", "店員"],
        'errortext': ["ошибка. введите снова", "incorrect. write again", "もう一度書き込んでください"],
        'magetext': [
            "класс маг - редкий и изолированный от общества класс. имеет несколько способностей, которые можно выбрать",
            "mage class - rare and isolated from others class. have some special abilities which you can choose",
            "魔法使いクラス ー 珍しい遠隔のクラス。いくつかの能力があります。"],
        'warriortext': [
            "класс воин - самый могущественный класс. имеет возможность выбора одного из специальных социальных статусов",
            "warrior class - the most powerful class. have an option to choose one of special social statuses",
            "戦士クラス ー 一番強力なクラス。 スペシャル地位があります。"],
        'clercktext': [
            "класс клерк - самый распространенный класс. не имеет никаких спобсоностей или статуса, сложен для игры",
            "clerck class - the most common class. have no special abilities or status and hard to play",
            "店員クラス ー　一番平凡なクラス。 なんか強力とか地位とかがありません。"],
        'clchoosetext': ["""Загрузка… ███████████████████████ 00%
выберите свой класс (маг, воин, клерк).
чтобы узнать подробности о классе напишите 'check' и название выбранного класса
Загрузка… ███████████████████████ 00%""",
                         "Loading… ███████████████████████ 00%\nchoose your class (mage,warrior,clerck)\nto check details about any class write 'check' and option you want to choose\nLoading… ███████████████████████ 00%",
                         """Loading… ███████████████████████ 00%\nクラスを選んでください（魔法使い、戦士、店員）。
                         詳細を知りたいと、’check’と選んだオプションを書き込んでください\nLoading… ███████████████████████ 00%"""],
        'clchosentext': ["вы выбрали опцию ","you have chosen ","オプションを選びました"],
        'elementstext': ["""это способность позволяющая использовать 4 стихии: воду, землю, огонь и воздух. это может быть полезно в боях
напишите 'return' если хотите вернуться назад""","""that's ability that allows you to use four elements: water, earth, fire and air. it may be a good trait at fighting
write 'return' if you want to return""","""それは四大を使うことができる能力です、戦闘でその能力は役に立つことができる
帰りたいと’return’を書き込んでください"""],
        'telepathytext': ["""это способность позволяющая читать мысли людей и других существ, это может быть полезной особенностью в общении с другими
напишите 'return' если хотите вернуться назад""","""that's ability that allows you to read people's and other creatures'thoughts, it may be a good trait at talking to others
write 'return' if you want to return""","""それは人と他の生物の心を読むことができる、会話でその能力は役に立つことができる
帰りたいと’return’を書き込んでください"""],
        'scrollstext': ["""это способность позволяющая использовать свитки, но она абсолютно бесполезна если не знать где найти их
напишите 'return' если хотите вернуться назад""","""that's ability to use scrolls, but it's completely useless if you don't know where to find them
write 'return' if you want to return""","""それはスクロールを使うことができる能力です、でもスクロールがある場所を分からなくてその能力は全然役に立たない
帰りたいと’return’を書き込んでください"""],
        'magechoicetext': ["""Загрузка… []]]]]]]████████████████ 30%
для вашего класса есть несколько вариантов способностей (4 стихии, телепатия, свитки)
если вы хотите узнать детали, напишите 'check' и выберите вариант о котором хотите узнать подробнее. если вы готовы продолжить, напишите вариант, который вы выбрали
Загрузка… []]]]]]]████████████████ 30%""","""Loading… []]]]]]]████████████████ 30%
you have several options in magic abilities for your class (four elements, telepathy, scrolls)
if you want to check details of any option, write 'check' and choose an option which you want to check. if you're ready to choose, write an option what you want to choose
Loading… []]]]]]]████████████████ 30%""","""Loading… []]]]]]]████████████████ 30%
        クラスがいくつかのオプションを持っています (四大, 以心伝心, スクロール)
        if you want to check details of any option, write 'check' and choose an option which you want to check. if you're ready to choose, write an option what you want to choose
        Loading… []]]]]]]████████████████ 30%"""],
        'elements': ["4 стихии","four elements","四大"],
        'telepathy': ["телепатия","telepathy","以心伝心"],
        'scrolls': ["свитки","scrolls","スクロール"],
        'highclasstext': ["""этот класс имеет кучу обязанностей и никакой свободы. он обязан выполнять миссии своего ранга каждую неделю, иначе социальный статус изменится на "вне закона"
на какое-то время и изменится на "преступник" позже. в любом случае, все обязаны уважать этот класс. также у него в инвентаре есть оружие
напишите 'return' если хотите вернуться назад""","""that's class with no freedom and a lot of duties. this class must complete their rank's missions every week, otherwise your social status will change to illegal
for time and change to criminal later. anyway, everyone must admire this class. also you have some gear in your inventory
write 'return' if you want to return""","""そのクラスが自由を持たなくてもたくさんの義務を持ちます。好評のクラスがランクのミッションは毎週を済まさなくてはならない。それ以外は地位は"""],
        'lowclasstext': ["""that's standart social status of warrior. this class must complete their rank's missions every two weeks, otherwise your social status will change to illegal for time
and change to criminal later. anyway, people admire this class even if low class's warriors are weaker than others classes. also you have some gear in you inventory
напишите 'return' если хотите вернуться назад""","""that's standart social status of warrior. this class must complete their rank's missions every two weeks, otherwise your social status will change to illegal for time
and change to criminal later. anyway, people admire this class even if low class's warriors are weaker than others classes. also you have some gear in you inventory
write 'return' if you want to return""","""japanese text"""],
        'criminaltext': ["""that's not rectricted by any duties class, but you need to hide from time to time. also you have some high quality gear in your inventory. this class shouldn't wait 
for help from others, because noone wants to help criminals
напишите 'return' если хотите вернуться назад""","""that's not rectricted by any duties class, but you need to hide from time to time. also you have some high quality gear in your inventory. this class shouldn't wait 
for help from others, because noone wants to help criminals
write 'return' if you want to return""","""japanese"""],
        'warriorchoicetext': ["""Загрузка… []]]]]]]████████████████ 30%
для вашего класса есть несколько вариантов статуса (высший класс, низкий класс, преступник)
если вы хотите узнать детали, напишите 'check' и выберите вариант о котором хотите узнать подробнее. если вы готовы продолжить, напишите вариант, который вы выбрали
Загрузка… []]]]]]]████████████████ 30%""","""Loading… []]]]]]]████████████████ 30%
you have several options in warrior's social status (high class, low class, criminal)
if you want to check details of any option, write 'check' and choose an option which you want to check. if you're ready to choose, write an option what you want to choose
Loading… []]]]]]]████████████████ 30%""","""Loading… []]]]]]]████████████████ 30%
クラスがいくつかのオプションを持っています  (好評, 平均, 犯罪者)
if you want to check details of any option, write 'check' and choose an option which you want to check. if you're ready to choose, write an option what you want to choose
Loading… []]]]]]]████████████████ 30%"""],
        'highclass': ["высший класс","high class","好評"],
        'lowclass': ["низкий класс","low class","平均"],
        'criminal': ["преступник","criminal","犯罪者"],
        'chclercktext': ["этот класс не имеет каких-либо дополнительных особенностей","this class don't have any additional traits","そのクラスはなんかスペシャル能力を持ちません"],
        'chooseracetext': ["выберите расу (человек, горячий человек, холодный человек)","choose your race (human, hot human, cold human)","人種を選んでください (人間, 熱い人間, 冷たい人間)"],
        'human': ["человек","human","人間"],
        'hothuman': ["горячий человек","hot human","熱い人間"],
        'coldhuman': ["холодный человек","cold human","冷たい人間"]
    }

    def __init__(self, lang):
        self._lang = lang

    def localize(self, text):
        if text in self.dictionary:
            return self.dictionary[text][self._lang.value]
        else:
            return text
        
# Usage Example
#localizer = Localizer(Language.RUSSIAN)
#def _(text): localizer.localize(text)
#print(_('nametext'))
