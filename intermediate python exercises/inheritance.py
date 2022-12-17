"""
class Person(object):
#constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

#to check if this person is an employee
    def display(self):
        print(self.name, self.id)

#driver code 

emp = Person("Satyam", 102)

emp.display()


#child class
+
-+

class Emp(Person):
    def Print(self):
        print("Emp was called")

Emp_details = Emp("Mayank",103)

#calling parent class function
Emp_details.display()

#Calling child class fuction
Emp_details.Print()

"""

class Person(object):
    #constructor
    def __init__(self, name, idnumber):
      self.name = name
      self.idnumber = idnumber

    def display(self):
        print (self.name)
        print (self.idnumber)

    #chlid class

class Employee(Person):

    def __init__(self, name, idnumber, salary, post):

        self.salary = salary
        self.post = post

        #invoking the __init__ of the parent class

        Person.__init__(self, name, idnumber)

a = Employee("Paris", 8820000, 200000, "Intern")

a.display()
    
    