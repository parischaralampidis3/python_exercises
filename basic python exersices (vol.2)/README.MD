Comments
--------
Comments in Python are the lines in the code that are ignored by the interpreter
during the execution of the program. Comments enhance the readability of the code and help the programmers to understand the code very carefully. 

-Single line comments
-Multiline comments
-Docstring comments

# Python program to demonstrate comments
 
# sample comment
#name = "geeksforgeeks"
#print(name)

Comments are generally used for the following purposes:

-Code readability
-Explanation of the code or metadata of the project
-Prevent execution of code
-To include resources



Truth terms
-----------
n Python we have the following terms (characters and phrases) for determining if something is 
“True” or “False.” Logic on a computer is all about seeing if some combination of these characters 
and some variables is True at that point in the program.
 
 • and
 • or
 • not
 • != (not equal)
 • == (equal)
 • >= (greater- than- equal)
 • <= (less- than- equal)
 • True
 • False


Python Comparison Operators
---------------------------

These operators compare the values on either sides of them and decide the relation among them
 They are also called Relational operators.

Assume variable a holds 10 and variable b holds 20, then −

Operator	Description	Example

==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.

!=	If values of two operands are not equal, then condition becomes true.	(a != b) is true.

<>	If values of two operands are not equal, then condition becomes true.	(a <> b) is true. This is similar to != operator.

>	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.

<	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.

>=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.

<=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.


!= True?
--------

1 != 0 True
1 != 1 False
0 != 1 True
0 != 0 False

== True?
--------

1 == 0 False
1 == 1 True
0 == 1 False
0 == 0 True


Python Assignment Operators
---------------------------

=	Assigns values from right side operands to left side operand	c = a + b assigns value of a + b into c

+= 	Add AND	It adds right operand to the left operand and assign the result to left operand	c += a is equivalent to c = c + a

-= 	Subtract AND	It subtracts right operand from the left operand and assign the result to left operand	c -= a is equivalent to c = c - a

*= 	Multiply AND	It multiplies right operand with the left operand and assign the result to left operand	c *= a is equivalent to c = c * a

/= 	Divide AND	It divides left operand with the right operand and assign the result to left operand	c /= a is equivalent to c = c / a

%= 	Modulus AND	It takes modulus using two operands and assign the result to left operand	c %= a is equivalent to c = c % a

**= 	Exponent AND	Performs exponential (power) calculation on operators and assign value to the left operand	c **= a is equivalent to c = c ** a

//= 	Floor Division	It performs floor division on operators and assign value to the left operand	c //= a is equivalent to c = c // a 


Python Logical Operators
------------------------

NOT True?
---------

not False True
not True False

OR True?
--------

True or False True
True or True True
False or True True
False or False False

AND True?

True and False False
True and True True
False and True False
False and False False

NOT OR True?

not (True or False) False
not (True or True) False
not (False or True) False
not (False or False) True

NOT AND True?

not (True and False) True
not (True and True) False
not (False and True) True
not (False and False) True


!= True?
1 != 0 True
1 != 1 False
0 != 1 True
0 != 0 False



== True?
1 == 0 False
1 == 1 True
0 == 1 False
0 == 0 True



There are following logical operators supported by Python language. Assume variable a holds 10 and variable b holds 20 then


and Logical AND	If both the operands are true then condition becomes true.	(a and b) is true.

or Logical OR	If any of the two operands are non-zero then condition becomes true.	(a or b) is true.

not Logical NOT	Used to reverse the logical state of its operand.	Not(a and b) is false.



If statements

-------------
Decision making is anticipation of conditions occurring while execution of the program and specifying actions taken according to the conditions.

Decision structures evaluate multiple expressions which produce TRUE or FALSE as outcome. 

You need to determine which action to take and which statements to execute if outcome is TRUE or FALSE otherwise.

Following is the general form of a typical decision making structure found in most of the programming languages −

Python programming language assumes any non-zero and non-null values as TRUE, and if it is either zero or null, then it is assumed as FALSE value.

Python programming language provides following types of decision making statements. Click the following links to check their detail.


What do you think the if does to the code under it? An if- statement creates what is 

called a “branch” in the code. It’s kind of like those choose-your-own-adventure books 

where you are asked to turn to one page if you make one choice and another if you go 

a different direction. The if- statement tells your script, “If this boolean expression is 

True, then run the code under it, otherwise skip it.


Why does the code under the if need to be indented four spaces? A colon at the end 

of a line is how you tell Python you are going to create a new “block” of code, and then 

indenting four spaces tells Python what lines of code are in that block. This is exactly the 

same thing you did when you made functions in the fi rst half of the book.


1	if statements

An if statement consists of a boolean expression followed by one or more statements.

2	if...else statements

An if statement can be followed by an optional else statement, which executes when the boolean expression is FALSE.

3	nested if statements
You can use one if or else if statement inside another if or else if statement(s).

Let us go through each decision making briefly −


Single Statement Suites
If the suite of an if clause consists only of a single line, it may go on the same line as the header statement.

Here is an example of a one-line if clause −



var = 100
if ( var == 100 ) : print "Value of expression is 100"
print "Good bye!"
When the above code is executed, it produces the following result −

Value of expression is 100
Good bye!

Loops
-----
Python programming language provides the following types of loops to handle looping requirements.

Python provides three ways for executing the loops. 

While all the ways provide similar basic functionality, they differ in the syntax and condition

checking time.


While loop
----------

In python, a while loop is used to execute a block of statements repeatedly until a given condition 

is satisfied. And when the condition becomes false, the line immediately after the loop in the 

program is executed.

All the statements intended by the same number of character spaces after a programing construct are considered, 

to be a part of a single block of code. Python uses indentation as its method of groupinh statements.

else on while loop
------------------

As discussed above, while loop executes the block until a condition is satisfied.When the condition becomes false, 

the statement immediately after the loop is executed.

The else clause is only executed when your while condition becomes false.If your break out of

the loop, or if an exception is raised, it won't be executed.



if condition:
    # execute these statements
else:
    # execute these statements
and while loop like this are similar

while condition:
     # execute these statements
else:
     # execute these statements


Typing statement while block
----------------------------

If the while block consists of a single statement then we can declare the entire loop in a single as shown below:

count = 0
 
while(count == 0):print( "Hello Geek" )

WARNING!
-------
It is suggested not to use this type of loopes as it is a never ending infinite loop

where the condition is always true and you have to forcelly terminate the compiler.


for loop
--------

For loops are used for sequential traversal.

In Python, there is no C style for loop, i.e., for (i=0; i<n; i++). 

There is “for in” loop which is similar to for each loop in other languages.
 
Let us learn how to use for in loop for sequential traversals.



syntax
------

for iterator_var in sequense:
	statements(s)


Lists
-----


Python lists are just like dynamically sized arrays, declared in other languages.

In simple language, a list is a collection of things, enclosed in [] and separated by commas.


animals = ['bear','tiger','penguin','zebra']
bear = animals[0]

What does exit(0) do?
---------------------

On many operating systems, a program can abort with exit(0), and the number passed in will indicate
an error or not. If you do exit(1), then it will be an error, but exit(0) will be a good exit.

dictionaries
------------

Dictionary in Python is a collection of key values, used to store data values like a map, which unlike 
other data types which hold only a single value as an element.

Dictionary holds key:value pair. Key-Value is provided in the dictionary to make it optimized.

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)

In Python, a dictionary can be created by placing a sequence of elements within the curly {} braces, separated 
by comma.
Dictionary holds pairs of values, one being the key and the other corresponding pair element being its Key:Value/
Values in a dictionary can be any data type and can be duplicated, whereas keys can't be repeated
and must be immutable. 

Note - Dictionary keys are case sensitive, the same name but different cases of key wil be treated dinstinctly.

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys:")
print(Dict)

#Creating a Dictionary
#with Mixed keys

Dict = {'Name': 'Geeks', 1:[1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Kes:")
print (Dict)

Dictionary can also be created by the built-in function dict(). An empty dictionary can be 
created by just placing to culry braces {}.

#Creating an empty Dictionary

Dict = {}
print("Empty Dictionary: ")
print(Dict)

#Creating a Dictionary.
#with dict() method

Dict = dict( {1: 'Geeks', 2 : 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

#Creating a Dictionary
#with each items as a Pair

Dict = dict([(1,'Geeks'),(2,'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)





Dictionary methods
------------------
clear() – Remove all the elements from the dictionary
copy() – Returns a copy of the dictionary
get() – Returns the value of specified key
items() – Returns a list containing a tuple for each key value pair
keys() – Returns a list containing dictionary’s keys
pop() – Remove the element with specified key
popitem() – Removes the last inserted key-value pair
update() – Updates dictionary with specified key-value pairs
values() – Returns a list of all the values of dictionary
