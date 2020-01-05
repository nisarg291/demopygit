# inheritance
# _init fun is use to intialized variable of class

# Use the Person class to create an object, and then execute the printname method:

class parent:
    x1 = 5
    def __init__(self,  fname, lname):
        self.firstName = fname
        self.lastName = lname

    def data(self):
        print("parent", self.firstName, self.lastName)


x = parent("nis", "ada")
x.data()

class child(parent):
    def __init__(self,  fname, lname, address):
        parent.__init__(self, fname, lname)
        # super().__init__(self, fname, lname)
        self.address = address
    def pri(self):
        print("child", " ", self.firstName, " ", self.lastName, " ", self.address)


c = child("nisarg", "adalja", "dikshanti")
print(c.x1)
c.data()
print(c.firstName)
print(c.lastName)
print(c.address)
c.pri()
# Iterator vs Iterable
"""Lists, tuples, dictionaries, and sets are all iterable objects. 
They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:
Example
Return an iterator from a tuple, and print each value:
"""
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"

myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

"""Create an Iterator
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
As you have learned in the Python Classes/Objects chapter,
 all classes have a function called __init__(),
 which allows you do some initializing when the object is being created.
The __iter__() method acts similar, you can do operations (initializing etc.), 
but must always return the iterator object itself.
The __next__() method also allows you to do operations,
 and must return the next item in the sequence.
Example
Create an iterator that returns numbers, starting with 1,
 and each sequence will increase by one (returning 1,2,3,4,5 etc.):"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)  # here __iter__ method is call during creating object

print(next(myiter))  # x=1 a=2
print(next(myiter))  # x=2 a=3
print(next(myiter))  #
print(next(myiter))
print(next(myiter))
"""StopIteration
The example above would continue forever if you had enough next() statements, or if it was used in a for loop.

To prevent the iteration to go on forever, we can use the StopIteration statement.

In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:

Example
Stop after 20 iterations:"""

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

