'''class Author:
    def __init__(self,name):
        self.name = name

    def book(self,title):
        return Book(title,self)
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def info(self):
        return f'{self.title} wrought {self.author.name}'

author = Author('Joanne Rowling')
book = author.book('Harry Potter')
print(book.info()) '''

import random
class Human:
    def __init__(self,name='Human',job=None,home=None,car=None):
        self.name = name
        self.money = 10
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

def get_home(self):
    pass

def get_car(self):
    pass

def get_job(self):
    pass

def eat(self):
    pass

def work(self):
    pass

def shopping(self,manage):
    pass

def chill(self):
    pass

def clean_home(self):
    pass

def to_repair(self):
    pass

def days_indexes(self, day):
    pass

def is_alive(self):
    pass

def live(self,day):
    pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        pass
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

brands_of_car = {
    'КАМАЗ':{'fuel': 50,'strength': 300, 'consumption': 2},
    'Богдан':{'fuel': 180,'strength': 270, 'consumption': 5},
    'Lada':{'fuel': 2,'strength': 40, 'consumption': 6},
    'Lambrgumbr':{'fuel': 40,'strength': 80, 'consumption': 6},
    'Mercedes':{'fuel': 50,'strength': 350, 'consumption': 20}}

job_list = {
    'Farmer':{'salary':30,'gladness_less':25},
    'FreeLancer':{'salary':35,'gladness_less':15},
                  'Pyton develomper':{'salary':50,'gladness_less':20},
                  'FreeLancer':{'salary':32,'gladness_less':25},
                  'Delivery man':{'salary':40,'gladness_less':20}}

class Job:
    def __init__(self,job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list(self.job)['salary']
        self.gladness_less = job_list(self.job)['gladness_less']