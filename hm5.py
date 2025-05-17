import tkinter
import requests
import random
import inspect
import sys

class Hominid:
    walk = 'four legs'
    brain = 'tiny'
    food = 'fruity'
    def __init__(self):
        print(self.walk)
        print(self.brain)
        print(self.food)

class Ardipithecus(Hominid):
    walk = 'half-upright'
    hands = 'grabby'
    place = 'jungle'
    def __init__(self):
        print(self.walk)
        print(self.hands)
        print(self.place)
class Australopithecus(Ardipithecus):
    walk = 'upright'
    tools = 'stone'
    brain = 'smallish'
    def __init__(self):
        print(self.walk)
        print(self.tools)
        print(self.brain)

class HomoHabilis(Australopithecus):
    tools = 'better tools'
    food = 'omnivore'
    brain = 'bigger'
    def __init__(self):
        print(self.tools)
        print(self.food)
        print(self.brain)

class HomoErectus(HomoHabilis):
    fire = 'yes'
    travel = 'left Africa'
    clothes = 'maybe'
    def __init__(self):
        print(self.food)
        print(self.travel)
        print(self.clothes)

class Neanderthal(HomoErectus):
    clothes = 'real clothes'
    care = 'help friends'
    brain = 'big'
    def __init__(self):
        print(self.clothes)
        print(self.care)
        print(self.brain)

class HomoSapiens(Neanderthal):
    speak = 'language'
    art = 'cool'
    brain = 'very big'
    def __init__(self):
        print(self.speak)
        print(self.art)
        print(self.brain)

nick = Hominid()
nick2 = Ardipithecus()
nick3 = Australopithecus()
nick4 = HomoHabilis()
nick5= HomoErectus()
nick6 = Neanderthal()
nick7 = HomoSapiens()

