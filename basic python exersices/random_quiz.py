import random 
print( "Guess a number from 1-10..")


def guess_number():
    retries = 0

    while(True):
        retries += 1 

        question = int(input("Type your guess > "))
        list = [1,2,3,4,5,6,7,8,9,10]
        result = random.choice(list) 
        print(result)
        
        if retries == 2:
            print("You have still one shot!!")
        elif retries == 3:
            print("You are out of tries")
            print ("Game over!")
            break;
        elif question != result:
            print("Try again.." .format(question))
        elif question == result:
            print( "You guessed the correct number ".format(question))
            exit(0)
guess_number()