from sys import argv

#write a script similar to the last exercise that uses read and argv to read the fi le you just 
#created.

#set a variable for script and  file name

script, filename = argv

print ( "IF you dont want that, hit CTRL+C (^C).")

print ("If you want that.hit RETURN.")

input("?")


print ( "Opening file..")

target = open(filename)


print(target.read())

print ("do you want to close the file? if yes hit RETURN ")

input("?")



target.close()

print ("file is closed..Goodbye!")
