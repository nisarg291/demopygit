
import mymodule
# classes and objects
"""Python is an object oriented programming language.
Almost everything in Python is an object,
with its properties and methods.
A Class is like an object constructor,
or a "blueprint" for creating objects."""


# Create a Class
# To create a class ,
# use the keyword class:
class MyClass:
    x = 5


"""Create Object
Now we can use the class 
named myClass to create objects:"""
p1 = MyClass()
print(p1.x)


# _init_ fun is in built fun

# All classes have a function called __init__(),
# which is always executed when the class is being initiated.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Note: The self parameter is a reference to the current instance of the class,
    # and is used to access variables that belong to the class.
    def myfunc(self):
        print("hello","name="self.name,"age=",age)


# self paramter are used in fun which are declared in class
# self parameter is required to access the current variable of the class
p1 = Person("john", 36)
print(p1.name)
print(p1.age)
p1.myfunc()


# It does not have to be named self , you can call it whatever you like,
# but it has to be the first parameter of any function in the class:
class my:
    m = 5

    """ def __init__(myobj, name, age):
        myobj.name = name
        myobj.age = age"""

    def myf(abc):
        print("Hello my name i", abc.m)


m1 = my()
print(m1.name)
m1.myf()


mymodule.myfun("Jonathan")