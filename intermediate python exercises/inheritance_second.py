class Product (object):
    #constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


    #child class

class Product_List(Product):

    def __init__(self, name,idnumber, category, price):

        self.category = category
        self.price = price

    
        Product.__init__(self, name,idnumber)


product_result1 = Product_List("Iphone",12000,"phone", "800" )
product_result2 = Product_List("samsung galaxy",12001,"phone", "800" )

product_result1.display()
product_result2.display()