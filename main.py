#class Student:
    #print('Hi!')
    #def __init__(self):
   #     self.mark = 12
  #      print('It is exellent')
 #
#first_student = Student()
#second_student = Student(mark=2)
#print(first_student.mark)
#print(second_student.mark)

import random

class Student:
    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.gladness -= 0.01
        self.progress += 0.05

    def to_sleep(self):
            print('I will sleep')
            self.gladness += 1.5

    def is_alive(self):
        if self.progress < -0.5:
           print('Cast out...')
           self.alive = False
        elif self.gladness <= 0:
            print('Depression')
            self.alive = False
        elif self.progress > 5:
            print('Passed externally...')
            self.alive = False
    def end_of_day(self):
        print(f'Gladness ={self.gladness}')
        print(f'Gladness ={round(self.progress,2)}')
    def live(self,day):
        day = 'Day' + str(day) + 'of' + self.name  + 'life'
        print(f'{day:^50}')
        life_cube = random.randint(1,3)
        if  life_cube == 1:
            self.to_chill()
        elif  life_cube == 2:
            self.to_sleep()
        elif  life_cube == 3:
            self.to_study()
            self.end_of_day()
            self.is_alive()
    nick = Student(name='Andrew')
    for day in range(366):
        if nick.alive == False:
            break

