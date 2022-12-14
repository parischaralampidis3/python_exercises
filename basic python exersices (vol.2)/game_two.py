from sys import exit
print("Welcome to the farm.")
print("Name a famr animal")

def welcome ():
    decision = input ( "> ")
    animals = ['horse', 'goat', 'hen', "pig"]

    for i in animals:
        if decision == animals[0]:
            print("This is also a farm animal",i)
            
welcome()

