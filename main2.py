import tkinter
import requests
import random
import inspect
import sys

class Grandparent:
    height = 300
    hair = 'brown'
    eyes = 'blue'
    def __init__(self):
        print(self.height)
        print(self.hair)
        print(self.eyes)

class Parent(Grandparent):
    height = 800
    def __init__(self):
        print(self.height)
        print(self.hair)
        print(self.eyes)

class Child(Parent):
    eyes = 'green'
    def __init__(self):
        print(self.height)
        print(self.hair)
        print(self.eyes)

nick = Child()
nick = Grandparent()
nick = Parent()

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))

sig = inspect.signature(Child)
for parameter in sig.parameters.values ():
    print (parameter.name, parameter.default)

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)