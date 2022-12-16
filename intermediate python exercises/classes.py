class Fruit(object):

    def __init__(self, fruits):

        self.fruits = fruits

    def basket_of_fruits(self):
       print(self.fruits)
            

result = Fruit("tangerine")
fruit_salad = Fruit("apple")


result.basket_of_fruits()
fruit_salad.basket_of_fruits()


class Dog:

    attr1 = "mammal"
    attr2 = "dog"

    def fun(self):

        print("I'm a ", self.attr1)
        print("I'm a ", self.attr2) 

Rodger = Dog()

print( Rodger.attr1)
Rodger.fun()