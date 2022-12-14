#strings 


#What does \r mean Python?
#carriage return
#In Python strings, the backslash “\” is a special character, also called the “escape” character.
#It is used in representing certain whitespace characters: “\t” is a tab, “\n” is a newline, and “\r” is a carriage return.

#This is explained in the Python documentation. In short,

#%d will format a number for display.
#%s will insert the presentation string representation of the object (i.e. str(o))
#%r will insert the canonical string representation of the object (i.e. repr(o))

# This is a variable that assingns a sentence with a modulo %d. This will format a number for display.
x = "There are %d types of people." % 10
#Both these variable asign string values 
binary = "binary" 
do_not = "don't"

#This variable asigns a sentence with a modulo %s. This will insert the presentation string representation of the object (i.e. str(o))
y = "Those who know %s and those who %s." % (binary, do_not) 


print (x)
print(y)

#This variable asigns a boolean value
hilarious = False
#This variable asigns a sentence with a modulo %r. This will insert the canonical string representation of the object (i.e. repr(o))
joke_evaluation = "Isnt't it that joke so funny?! %r"

#This command prints the value of the variables above.
print(joke_evaluation % hilarious)


w ="This is the left side of..."
e ="a string with a right side"


print (w + e)

