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
    self.home = House()

def get_car(self):
    self.car = Auto(brands_of_car)

def get_job(self):
    if self.car.drive():
        pass
    else:
        self.to_repair()
        return
    self.job = Job(job_list)

def eat(self):
    if self.home.food <= 0:
        self.shopping('food')
    else:
        if self.satiety >= 100:
            self.satiety = 100
            return
        self.satiety += 5
        self.home.food -= 5


def work(self):
    if self.car.drive():
        pass
    else:
        if self.car.fuel < 20:
            self.shopping('fuel')
            return
        else:
            self.to_repair
            return
    self.moneey += self.job.salary
    self.gladness -= self.job.gladness_less
    self.satiety -= 4


def shopping(self,manage):
    if self.car.drive():
        pass
    else:
        if self.car.fuel < 20:
            manage = 'fuel'
        else:
            self.to_repair()
            return
    if manage == 'fuel':
        print('I bought fuel')
        self.money -= 100
        self.car.fuel = 100
    elif manage == 'food':
        print('I bought food')
        self.money -= 50
        self.home.food += 50
    elif manage == 'delicacies' :
         self.gladness += 30
         self.satiety += 2
         self.money -= 15


def chill(self):
    self.gladness += 50
    self.home.mess += 15

def clean_home(self):
    self.gladness -= 10
    self.home.mess = 0

def to_repair(self):
    self.car.strength += 100
    self.money -= 50

def days_indexes(self, day):
    day = f'Today the{day} of {self.name} life'
    print(f'{day:=^50}','\n')
    human_indexes = self.name + 'indexes'
    print(f'{human_indexes:=^50}','\n')
    print(f'Money - {self.money}')
    print(f'Gladness - {self.gladness}')
    print(f'Satiety - {self.satiety}')
    car_indexes = f'{self.car.brand} car indexes'
    print(f'{car_indexes:=^50}', '\n')
    print(f'Strength - {self.car.strength}')
    print(f'Fuel - {self.car.fuel}')
    home_indexes = f'Home indexes'
    print(f'{home_indexes:=^50}', '\n')
    print(f'Food - {self.home.food}')
    print(f'Fuel - {self.home.mess}')

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