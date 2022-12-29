DATA TYPES
----------
number
------
Numnber data types store numeric values.They are immutable data types, which means that changing the value of a number data type results in a newly allocated project

intenger 
--------
In Python, text in between quotes -- either single or double quotes -- is a string data type.
 An integer is a whole number, without a fraction, while a float is a real number that can contain a fractional part. For example, 1, 7, 342
 are all integers, while 5.3, 3.14159 and 6.0 are all floats. When attempting to mix incompatible data types, you may encounter a TypeError.
 You can always check the data type of something using the type() function.
  Integers are the whole number, including negative numbers but not franctions. In Python, there is no limit to how long an integer value can be.
They can be created directly by entering a number with a decimal point, or by using operations such as division on integers. Extra zeros present at the number's end are ignored automatically.

-float
------
This is a real number with floating-point represantation. It is specified by a decimal point. 


-complex

+ plus
- minus
/ slash
* asterisk
% percent
< less- than
> greater- than
<= less- than- equal
>= greater- than- equa

Type conversion between numbers
-------------------------------
We can convert one number into the other
form by two methods:

-Using Arithmetic operations
----------------------------
We can use operations like addition, substract, division and multiply, in order to change the type of the number
implicity, if one of the operands is float.This method is not working for complex numbers. 

a = 1.6
b = 5 

c = a + b 

print(c)

Using built-in functions ------------------------ 

  We can also use built in functions 
  like int(), float() and complex( )
  to convert into different types explicitly.

When we convert float to int, the decimal part is truncated. 

Note: 

We can’t convert a complex data type number into int data type and float data type numbers.
We can’t apply complex built-in functions on strings.

Random numbers in Python
------------------------
Python provides a random module to generate pseudo - random numbers. This 
module can create random numbers, select a random element from a sequence in Python. 

Math module
------------
The math module of Python helps to carry different mathematical operations trigonometry, statistics, probability, logarithms, etc.

VARIABLES
----------------
Python variables is containers which store values. Python is not 'statically typed'. We do not need to declare variables before using them, or declare their type. A variable is created the moment we first assign a value to it. 
A python variable is a name giver to a memory location. It is the basic unit of storage in a program.

Rules for creating variables in Python
---------------------------------------
- A variable name must start with a letter or the underscore character.
- A variable cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores(A-z, 0-9, and _).
- Variable names are case-sensitive(name, Name and NAME are three different variables).
- The reserved words(keywords) cannot be used naming the variable

Declare the Variable
Let’s see how to declare the variable and print the variable.

Number = 100
 
# display
print( Number)

Re-declare the Variable
We can re-declare the python variable once we have declared the variable already.

Python3
# declaring the var
Number = 100
 
# display
print("Before declare: ", Number)
 
# re-declare the var
Number = 120.3
   
print("After re-declare:", Number)


Asign a single value to multiple 
--------------------------------
variables.
----------

Also Python allows asigning a single value to serveral variables simultaneouusly with "=" operators.

a = b = c = 10
 
print(a)
print(b)
print(c)

Asigning different values to multiple
------------------------------------- variables
---------

Python allows adding different values in a single line with "," operators. 

a, b, c = 1, 20.2, "GeeksforGeeks"
 
print(a)
print(b)
print(c)

Global keyword
---------------
Global keyword is a keyword that allows a user to modify a variable outside of the 
current scope.
It is used to create global variables from a non-global scope inside a function. Global 
keyword is used inside a function only when we want to do asignments or when we want to change a variable.

Rules of global keyword:

-If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a local unless explicitly declared as global.

-Variables that are only referenced inside a function are implicitly global.

-We Use global keyword to use a global variable inside a function.

-There is no need to use global keyword outside a function.

# Python program to modify a global
# value inside a function
 
x = 15
def change():
 
    # using a global keyword
    global x
 
    # increment value of a by 5
    x = x + 5
    print("Value of x inside a function :", x)
 
 
change()
print("Value of x outside a function :", x)

Variables and Scope
-------------------

Why is the % character a “modulus” and not a “percent”?
--------------------------------------
Mostly that’s just how the designers chose to use that symbol. In normal writing, you are correct 
to read it as a “percent.” In programming, this calculation is typically done with simple division 
and the / operator. The % modulus is a different operation that just happens to use the % symbol.

How does % work?
-----------------
Another way to say it is “X divided by Y with J remaining.” For example, “100 divided by 16 with 
4 remaining.” The result of % is the J part, or the remaining part.
What is the order of operations?
In the United States we use an acronym called PEMDAS, which stands for Parentheses Exponents 
Multiplication Division Addition Subtraction. That’s the order Python follows as well.



Why does / (divide) round down?
--------------------------------
It’s not really rounding down; it’s just dropping the fractional part after the decimal. Try doing 
7.0 / 4.0 and compare it to 7 / 4 and you’ll see the difference

Python %d and %s For Formatting Integer and String
------------------------------------------

Python is developed with the C programming language and some of the language syntaxes 
are borrowed from the C. The % is an operator used to format a given string in different 
ways. The %d is the format specifier used to print integers or numbers. 
There is also the %s string specifier which is used to print and format string values
and string variables.

%d Format Specifier
--------------------
One of the popular use cases for the %d format specifier is using the print() method. 
In the following example, we will the age which is an integer inside a string by using 
the %d format specifier. The %d format specifier can be also used multiple times.
 We will provide the integers as a tuple in the following example.

age = 40

print("My age is %d" % (age) )
My age is 40
With multiple integers, you can provide multiple item tuples like below.
%
age = 40

print("My age is %d. I have born in %d." % ( age , 1980 ) )

%s Format Specifier
-------------------
The %s can be used with different methods like print(), format(), etc. In general %s is used to put and print string values or string variables. In the following example, we want to print the name variable in a parameterized way.

name = "Ahmet"

print("My name is %s" % name)
My name is Ahmet
Alternatively, we can use the %s multiple times for a single string or print().


name = "Ahmet"

surname = "Baydan"

print("My name is %s %s" % (name,surname))
My name is Ahmet Baydan
%d and %s Format Specifiers At The Same Time
The %d and %s format specifiers can be also used at the same time. Just provides the integer and string values or variables as a tuple. In the following example, we provide the name and age as a string and integer values.

name = "Ahmet"

age = 8

print("My name is %s and I am %d years old." % (name,age))
My name is Ahmet and I am 8 years old.


What if I wanted to start the months on 
---------------------------------------
a new line?
------------

You simply start the string with \n like this:
 "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

Why do the \n newlines not work when I 
--------------------------------------
use %r?
-------

That’s how %r formatting works; it prints it the way you wrote it (or close to it). It’s the “raw” 
format for debugging.

Why do I get an error when I put spaces 
---------------------------------------
between the three double- quotes?
---------------------------------
You have to type them like """ and not " " ", meaning with no spaces between each one.

from os.path import exists
----------------------------
OS module in Python provides functions for interacting with the operating system. 
OS comes under Python’s standard utility modules. This module provides a portable way 
of using operating system dependent functionality. os.path module is sub module of OS 
module in python used for common path name manipulation.


python methods
--------------
seek()
------

In Python, seek() function is used to change the position of the File Handle to a given 
specific position. File handle is like a cursor, which defines from where the data has 
to be read or written in the file. 

The reference point is selected by the from_what argument. It accepts three values: 
 

0: sets the reference point at the beginning of the file 
 
1: sets the reference point at the current file position 
 
2: sets the reference point at the end of the file 


Why does seek(0) not set the current_line to 0?

First, the seek() function is dealing in bytes, not lines. So that’s going to the 0 byte (fi rst byte) in 
the fi le. Second, current_line is just a variable and has no real connection to the fi le at all. We 
are manually incrementing it

open()
--------
Before you can read or write a file, you have to open it using Python's built-in open() function. 
This function creates a file object, which would be utilized to call other support methods associated with it.

close()
--------
Python file method close() closes the opened file.
 A closed file cannot be read or written any more. Any operation, 
which requires that the file be opened will raise a ValueError after the file has been
 closed. Calling close() more than once is allowed.

Python automatically closes a file when the reference object of a file is reassigned 
to another file. It is a good practice to use the close() method to close a file.

fileObject.close()

#!/usr/bin/python

# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name

# Close opend file
fo.close()

read()
---------
The read() method reads a string from an open file. 
It is important to note that Python strings can have binary data. apart from text data.

fileObject.read([count])

#!/usr/bin/python

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print "Read String is : ", str
# Close opend file
fo.close()

readline()
----------
Python readline() is a file method that helps to read one complete line from the given file. It has a trailing newline (“\n”) at the end of the string returned.

You can also make use of the size parameter to get a specific length of the line. The size parameter is optional, and by default, the entire line will be returned.

The flow of readline() is well understood in the screenshot shown below:

You have a file demo.txt, and when readline() is used, it returns the very first line from demo.txt.

How does readline() know where each line is?

Inside readline() is code that scans each byte of the fi le until it fi nds a \n character, then stops 
reading the fi le to return what it found so far. The fi le f is responsible for maintaining the current 
position in the fi le after each readline() call, so that it will keep reading each line


write()
--------
The write() method writes any string to an open file. 

It is important to note that Python strings can have binary data and not just text.

The write() method does not add a newline character ('\n') to the end of the string 

fileObject.write(string)


#!/usr/bin/python

# Open a file
fo = open("foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n")

# Close opend file
fo.close()


truncate()
----------
Python file method truncate() truncates the file's size. 

If the optional size argument is present, the file is truncated to (at most) that size.

The size defaults to the current position. The current file position is not changed. 

Note that if a specified size exceeds the file's current size, 

the result is platform-dependent.



Note − This method would not work in case file is opened in read-only mode.

operations


fileObject.truncate( [ size ])



#!/usr/bin/python

# Open a file
fo = open("foo.txt", "rw+")
print "Name of the file: ", fo.name

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.readline()
print "Read Line: %s" % (line)

# Now truncate remaining file.
fo.truncate()

# Try to read file now
line = fo.readline()
print "Read Line: %s" % (line)

# Close opend file
fo.close()






Mathematical operations
-------------------------                                                                                                                                                           a + b = Adds a and b

a - b = Subtracts b from a

a * b = Multiplies a and b

a / b = Divides a by b

a ** b = Elevates a to the power of b. For non integer values of b, this becomes a root (i.e. a**(1/2) is the square root of a)

a // b = The integer part of the integer division of a by b

a % b = The remainder part of the integer division of a by b    





Logical conditions
-------------------

Python supports the usual logical conditions from mathematics:

Equals: a == b

Not Equals: a != b

Less than: a < b

Less than or equal to: a <= b

Greater than: a > b

Greater than or equal to: a >= b


a = 33
b = 200
if b > a:
  print("b is greater than a")


else

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")



if (n%2==0) and (n in range(2,6) or n > 20): #Conditions B and D
    print('Not Weird')
elif (n%2 == 1) or (n%2 == 0 and n in range(6, 21)): #Conditions A and C
    print('Weird')




Loops
-------
Loops are control structures that iterate over a range to perform a certain task. They can work with any iterable type, such as lists and dictionaries. To control the loop in this problem, use the range function (see below for a description).

There are two kinds of loops in Python.

A for loop:

for i in range(0, 5):
    print i
And a while loop:

i = 0
while i < 5:
    print i
    i += 1

When using a for loop, the next value from the iterator is automatically taken at the start of each loop. When using a while loop, the iterator must be initialized prior to the loop,
 and the value updated within the loop.

Note Be careful about indentation in Python. Read more

The range() function

The range function is a built in function that returns a series of numbers. At a minimum, it needs one integer parameter.

Given one parameter, , it returns integer values from  to . 

For example, range(5) returns the numbers  through  in sequence.
To start at a value other than , call range with two arguments. For example, range(1,5) returns the numbers  through .
Finally, you can add an increment value as the third argument. For example, range(5, -1, -1) produces the descending sequence from  through  and range(0, 5, 2) produces , , .
If you are going to provide a step value, you must also include a start value.


Textwrap
The textwrap module provides two convenient functions: wrap() and fill().

textwrap.wrap()
The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most.
It returns a list of output lines.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 
textwrap.fill()
The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.



Escape Sequences
-----------------
This is the list of all the escape sequences Python supports. You may not use many of these, but 
memorize their format and what they do anyway. Also try them out in some strings to see if you 
can make them work.
Escape What it does.

\\ Backslash (\)

\' Single- quote (')

\" Double- quote (")

\a ASCII bell (BEL)

\b ASCII backspace (BS)

\f ASCII formfeed (FF)

\n ASCII linefeed (LF)

\N{name} Character named name in the Unicode database (Unicode only)

\r ASCII carriage return (CR)

\t ASCII horizontal tab (TAB)

\uxxxx Character with 16- bit hex value xxxx (Unicode only)

\Uxxxxxxxx Character with 32- bit hex value xxxxxxxx (Unicode only)

\v ASCII vertical tab (VT)

\ooo Character with octal value oo

\xhh Character with hex value hh
-------------------------------------------------


Functions
----------

Functions do three things:
 1. They name pieces of code the way variables name strings and numbers.
 2. They take arguments the way your scripts take argv.
 3. Using #1 and #2, they let you make your own “mini- scripts” or “tiny commands.”

Functions can be classified into the following three types:

- Built in functions : These are functions that already predefined in python like print(), min() etc.

-User-defined functions: These are functions that programmers create and use at the places where they need them.

-Anonymous functions: These are the functions that do not have a name and are defined by the user.These are also called lambda functions.

Empty functions
----------------
Empty functions are not allowed in Python. We cannot defined a fuctions without writing at leaset one line of code.We get error by running an empty function. A solution for this is to use the 'pass' statement.This can be considered as a function that does nothing.


def empty_func():
    pass

Python function arguments
-------------------------
Arguments are the values passed to a function when we call it. 
Arguments are the input supplied to the function while using it.Whereas parameters are the names used inside the function while defining it.

But we cannot pass those values as arguments on which the function cannot do the required operations. For example, we cannot add a string and a number. Because of this, we get an error on passing the wrong values as shown below.

Traceback (most recent call last):
File “<pyshell#59>”, line 1, in <module>
add(‘tres’,54)
File “<pyshell#52>”, line 2, in add
sum=num1+num2
TypeError: can only concatenate str (not “int”) to str

Types of python arguments

-required arguments
-------------------


Functions may have been a mind- blowing amount of information, but do not worry. Just keep 
doing these exercises and going through your checklist from the last exercise and you will 
eventually get it.
There is one tiny point though that you might not have realized, which we’ll reinforce right now. 
The variables in your function are not connected to the variables in your script. Here’s an exercise 
to get you thinking about this:

def cheese_and_crackers(cheese_count, boxes_of_crackers):
 print "You have %d cheeses!" % cheese_count
print "You have %d boxes of crackers!" % boxes_of_crackers
 print "Man that's enough for a party!"
 print "Get a blanket.\

print "OR, we can use variables from our script:"
 amount_of_cheese = 10
 amount_of_crackers = 50

 cheese_and_crackers(amount_of_cheese, amount_of_crackers)



input() function
-----------------

Python input() function is used to take the values from the user. 
This function is called to tell the program to stop and wait for the user to input the values. 
It is a built-in function. The input() function is used in both the version of Python 2.x and Python 3.x. 
In Python 3.x, the input function explicitly converts the input you give to type string. But Python 2.x input function takes the value and type of the input you enter as it 
is without modifying the type. 

                                                         