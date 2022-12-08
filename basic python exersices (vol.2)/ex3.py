the_count = [ 1,2,3,4,5 ]
fruits = [ "pears", "apple", "orange", "banana" ]
change = [ 1,"penies", 2, "dimes", 3, "quarters"]


#this first kind of for loop goes through a list


for number in the_count:
    print("This is count :%d "% number)
 

#same as above

for fruit in fruits:
    print("A fruit type of : %s"% fruit)

#also we can go through mixed lists too
#n notice we have to use %r since we don't know what's in it.


for i in change:
    print("i ve got %r "% i)

