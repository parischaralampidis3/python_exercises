MODULE, CLASSES, AND OBJECTS.
-----------------------------

Python is something called an object oriented programming language. What this means is there's a construct in Python called a class that let's you stucture your software in particular way.
Using classes you can add consistency to your programs so that they can be used in a cleaner way.
A class is a user-defined blueprint or prototype from which objects are created.
Classes provide a means of bundling data and functionality together.
Creating a new class creates a new type of object, allowing new instances of that type to be made.
Class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and userd by creating an instance of that class.

Some points on Python class:

- Classes are created by keyword class

- Attributes are the variables that belong to a class

- Attibutes are always public and can be accessed using the dot(.) operator.

Class Objects
--------------

An Object is an instance of  a class. A class is like a blueprint, while an instance is a copy of the class with actual values. 

An object consists of 

State: It is represented by the attributes of an object. It also reflects the properties of an object.

Behaviour: It is represented by the methods of an object.It also reflects the response of an object to other objects.

Identity: It gives  a unique name to an object and enables one object to interact with other object.

Declaring objects
-----------------

When an object of a class is created, the class is said to be instantiated. All the instances share the attributes an the behavioue of the class. But the 
values of those attributes the state are unique fore each object. A single class may have any number of instances.

The self 
--------

-Class methods must have an extra first parameter in the method definition.We do not give a value for this parameter when we call the method, Python provides it.

-if we have a method that takes no arguments, we still have one  argument.

self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.



__init__method
--------------

The __init__method is similar to the constructors in C++ and Java. 
Constructors are used to initialize the object's state. 
Like methods, a constructor also contains a collection of statements that are executed at the time of object creation.
It runs as soon as an object of a class is instantiated. The method is useful to do any instatiation you want to do with your project. 

 Constructors are used to initializing the object’s state. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.

Class and intstance variables
------------------------------

Instance variables are for data, unique to each instance and class variables are for attributes and methods shared by all instances of the class.Instance variables are variables whose value is assigned a constuctor or method with self whereas class variables are variables whose value is assigned in the class.

Inheritance in Python
---------------------
One of the core concepts in the object-oriented programming (OOP) languages  is inheritance.
It is a mechanism that allows you to create hierarcy of classes that share a set of properties and methods by deriving a class from another class.
Inheritance is the capability of one class to devire or inherit the properties from another class.

Benefits of inheritance are:
---------------------------

- It represents real-world relationships well

- It provides the reusability of a code. We don't have to write the same code again and again. Also it allows us to add more features to a class without modifying it.

- It is transitive in a nature, which means tha if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.

-Inheritance offers a simple, understandable model structure

-Less development and maintenance expenses result from an inheritance.

Subclassing (Calling constructor of 
-----------------------------------
parent class)
---------------------

A child class needs to indetify which class is its parent class.
This can be done by mentioning the parent class name in the definition of the child class.

Different types of Inheritance:

Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.


Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances. 

Hierarchical inheritance More than one derived class are created from a single base.


Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.


Comnposition
-------------



Polyphormism
------------