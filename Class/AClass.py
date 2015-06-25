__author__ = 'dimage01'

class Car:
    name = ""
    brand = ""
    count = 0
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand
        Car.count +=1



    def getName(self):
        return self.name


    def setName(self,name):
        self.name = name



car1 = Car('T430','Ferrari')
car2 = Car('X6','BMW')

print car1.getName()
print Car.count


car2.setName('x5')
print car2.getName()

var1 = 10
var2 = var1
del var1
# print(var1)
print(var2)


