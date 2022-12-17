class Fruit(object):

    def __init__(self, fruits):

        self.fruits = fruits

    def basket_of_fruits(self):
       print(self.fruits)
            

result = Fruit("tangerine")
fruit_salad = Fruit("apple")


result.basket_of_fruits()
fruit_salad.basket_of_fruits()



"""
class Dog:

    attr1 = "mammal"
    attr2 = "dog"

    def fun(self):

        print("I'm a ", self.attr1)
        print("I'm a ", self.attr2) 

Rodger = Dog()

print( Rodger.attr1)
Rodger.fun()

"""
"""   
class Person(object):
  
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print(self.name)
    


name1 = Person("Paris")

name1.say_hi()

"""

class Person(object):
  
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hi(self):
        print("My name is", self.name, "and my age is", self.age)


info = Person("Paris", 38)

info2  = Person("Valentina","25")

info.say_hi()
info2.say_hi()









