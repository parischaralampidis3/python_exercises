import random 
import math


print(random.random())

s = 'geeksforgeeks'
L = [1,2,3,4,5,6,7,8,9,10]

print (random.choice(s))
print ( random.choice(L))


a = 3.5

#returning the ceil of 3.5

print("The ceil of 3.5 is: ", end = "" )
print (math.ceil(a))

#returning the floor of 3.5

print("The floor of 3.5 is ", end = " ")
print (math.floor(a))

print ("The value of 3.5**2 is : ",end="")
print (pow(a,2))

#find the power 
print ( "The value of log2 of 3.5 is: ", end = " ")
print ( math.log2(a))

#print the square root of 3.5

print( "The value of sqrt of 3.5 is: ", end = " ")
print ( math.sqrt(a))

#return the value of sine of 3.5

print ("The value of sine is : ", end =" ")
print (math.sin(a))


