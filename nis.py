import random as r
# random function
print(r.randrange(1, 10))
# print(random.randrange(1,10))
""" it is  multiple line comment
hi hello"""
# multiple line string we know that string is immutable
# means the value of string is not change
x = """ \n    Hi    hello 
I am learning   Python    
Welcome  \n """
print("the string is\n", x)
print("length of the string is =", len(x))
# strip is use to remove white space
print(x.strip())
print(x.lower())
print(x.upper())
a = "Hello, World!"
print(a.replace("H", "J"))
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']
p = a.split(",")
print(p)
print(type(p))
# Check String
# To check if a certain phrase or character is present in a string,
# we can use the keywords in or not in.
# Example
# Check if the phrase "ain" is present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print("'ain' is present or not=", x)
# it give error bcz we can't combine 2 different type of variable
# like string and int
age = 36
# txt = "My name is John, I am "+ age
# print(txt)
# print(type(txt))
# But we can combine strings and numbers by using the format() method!
# The format()method takes the passed arguments,formats them, and places them
# in the string where the placeholders {} are:
# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# The format() method takes unlimited number of arguments,
# and are placed into the respective placeholders:
# Example
quantity = 3
itemno = 567
price = 49.95
myorder1 = "I want {} pieces of item {} for {} dollars."
print(myorder1.format(quantity, itemno, price))
# You can use index numbers {0} to be sure the arguments are
# placed in the correct placeholders:

# Example
quantity = 3
itemno = 567
price = 49.95
myorder1 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder1.format(quantity, itemno, price))
# user input
x = input("enter a value for x ")
y = input("enter a value for y ")
z = int(x) + int(y)
print(z)
"""List is a collection which is ordered and changeable. 
Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. 
Allows duplicate members.
Set is a collection which is unordered and unindexed.
 No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. 
No duplicate members."""

# list = mutable or changes kari sakay
lst1 = list([10, 20, 30, 40])
print(lst1)
lst = [10, 20, 20, 30, 40]
lst.insert(2, 50)
lst.insert(2, 40)
lst.extend(lst)
print(lst)
print(lst.count(40))
print(lst)
print(lst.index(40))
# You cannot copy a list simply by typing list2 = list1
# because: list2 will only be a reference to list1,
# and changes made in list1 will automatically
# also be made in list2.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
thislist[0] = "blueberry"
print(thislist)
print(mylist)
mylist = list(thislist)
print(mylist)
# tuple = immutable or values of the tuple is not change
"""The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.
Example
Using the tuple() method to make a tuple:"""

thistuple = tuple(("apple", "banana", "cherry"))
# note the double round-brackets
print(thistuple)
tup = (10, 20, 30, 20)
print(tup)
print(tup.index(20))
print(tup.count(20))
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
# set
# A set is a collection which is unordered and unindexed.
# In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# The update() method inserts the items in set2 into set1:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# Dictionary
"""A dictionary is a collection which is unordered,
 changeable and indexed. In Python dictionaries are written with curly brackets, 
 and they have keys and values.
Example
Create and print a dictionary:"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
print(x)
y = thisdict.get("model")
print(y)
thisdict["year"] = 2018
for x in thisdict:
    # print(x) # it will print all key names
    # print(thisdict[x])# it will print all values
    print(x, ":", thisdict[x])
for x in thisdict.values():
    print(x)  # it will print all values
for x, y in thisdict.items():
    print(x, ":", y)
thisdict["color"] = "red"  # adding items
print(thisdict)
thisdict.pop("model")  # removing items
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict["brand"]
print(thisdict)
del thisdict
# print(thisdict)  # error
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
mydict = dict(thisdict)
"""Nested Dictionaries
A dictionary can also contain many dictionaries, this is called nested dictionaries.

Example
Create a dictionary that contain three dictionaries:"""
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}
"""Or, if you want to nest three dictionaries that already exists as dictionaries:
Example
Create three dictionaries, than create one dictionary
 that will contain the other three dictionaries"""
child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
# if elif and else
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
a = 200
b = 33
c = 500
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")
if a > b and c > a:
    print("Both conditions are True")
if a > b or a > c:
    print("At least one of the conditions is True")
if b < a < c:
    print("Both conditions are True")
"""Nested If
You can have if statements inside if statements, 
this is called nested if statements.
Example"""
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
# The pass Statement
# if statements cannot be empty,
# but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
# Example
a = 33
b = 200
if b > a:
    pass
# while loop
i = 1
while i < 6:
    print(i)
    i += 1
# break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# The else Statement
"""With the else statement we can run a block of code once when the condition no longer is true:
Example
Print a message once the condition is false:"""

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
# for loop
for x in "banana":
    print(x)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
for x in range(6):
    print(x)
for x in range(6):
    print(x)
else:
    print("Finally finished!")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
# function
"""A function is a block of code.
 which only runs when it is called.
You can pass data, known as parameters, 
into a function.
A function can return data as a result."""
# function defination
def my_function():
    print("Hello from a function")


# calling function
my_function()

def my_function1(name):
    print(name)

my_function1("nisarg adalja")
my_function1("dhruvil patel")
# Arbitrary Arguments, *args
"""If you do not know how many arguments that will be passed into your function,
 add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, 
and can access the items accordingly:
Example
If the number of arguments is unknown, add a * before the parameter name:"""
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
def fun(*n):
    for i in range(len(n)):
        print(n[i])
fun(1)
fun(1, 2, 3)
fun(1, 2, 3, 4, 5)
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
def fact(n):
    if n == 1:
        return 1
    else:
        x1 = n * fact(n-1)
        return x1

print(fact(6))
def fibo(n):
    if n <= 2:
        return 1
    else:
        x1 = fibo(n-1) + fibo(n-2)
        return x1

print(fibo(6))
def fact(n):
    if n == 1:
        return 1
    else:
        x1 = n * fact(n-1)
        return x1

print(fact(6))
"""Python Lambda
A lambda function is a small anonymous function.
A lambda function can take any number of arguments,
 but can only have one expression.
Syntax
lambda arguments : expression """
x = lambda a : a + 10
print(x(5))
# Lambda functions can take any number of arguments:

# Example
# A lambda function that multiplies argument a with argument b and print the result:
x = lambda a, b: a * b
print(x(5, 6))
# Why Use Lambda Functions?
"""The power of lambda is better shown when you use them
as an anonymous function inside another function.
Say you have a function definition that takes one argument, 
and that argument will be multiplied with an unknown number:"""
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)

print(mydoubler(11))