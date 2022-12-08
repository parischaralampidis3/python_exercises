
#loops and lists
#while loop 

count = 0

while (count < 3):
    count = count + 1
    print("Hello Geek!")
#using else statement whith while loops
else:
    print("In else block")
                             


n = 4 

for i in range( 0, n ):
    print(i)

#iterating over a list
print("List Iteration")

l = ["geeks", "for", "geeks"]

for i in l:
    print(i)

#iterating over a tuple
print("Tuple Iteration")
t = ("geeks", "for", "geeks")

for i in l:
    print(t)


#iterating over a string 
print("String Iteration")
s = "Geeks" 

for i in s :
    print(i)


#iterating over a dictionary

#dict() -> new empty dictionary dict(mapping)
#  -> new dictionary initialized from a mapping object's
#(key, value) pairs
print("\nDictionary Iteration")
d = dict()

d['xyz'] = 123
d['abc'] = 345

for  i in d:
    print( "%s" "%d" % (i, d [i]))


#iterating over a set 
print ( "\nSet Iteration")

set1 = { 1,2,3,4,5,6 }
for i in set1:
    print(i)