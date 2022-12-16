class Fruit(object):

    def __init__(self, fruits):

        self.fruits = fruits

    def basket_of_fruits(self):
       print(self.fruits)
            

result = Fruit("tangerine")
fruit_salad = Fruit("apple")


result.basket_of_fruits()
fruit_salad.basket_of_fruits()
