__str__
##inner str method: print, str, or text method could call it
__repr__

class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return 'a {sel.color} car'.format(self=self)
    def __repr__(self):
        return '__repr__ for Car'
   

my_car=Car('red',37281)
my_car
#__repr__ for Car
repr(my_car)
'__repr__ for Car'

#__str__ vs __repre__
#__str__: easy read info of a class
#__repre__: unambiguous, should be a python code to recreate the object 

import datetime

today=datetime.da.today()

>>> str(today)
'2019-07-19'
>>> repr(today)
'datetime.date(2019, 7, 19)'

class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __repr__(self):
        return '{self.__class__.__name__}({self.color},{self.mileage})'.format(self=self)
    def __str__(self):
        return 'a {self.color} car'.format(self=self)

>>> my_car=Car('red',223)
>>> str(my_car)
'a red car'
>>> my_car
Car(red,223)
>>> repr(my_car)
'Car(red,223)'
>>> print(my_car)
a red car
