# fibonacci series 0 1 1 2 3 5 8 13

def fibo(n):
    a = 0
    b = 1
    print(a);
    print(b);
    for i in range(2, n):
        c = a+b
        a = b
        b = c
        print(c)

fibo(10)

# factorial

def fact(n):
    mul = 1
    for i in range(1, n+1):
        mul = mul * i
    return mul

n1 = int(input("enter num which you want to find factorial of num = "))
res = fact(n1)
print(f"factorial of {n1}! is {res}.")

import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())

def fibo1(n2):
    if n2 < 2:
        return n2
    else:
        return fibo1(n2-1)+fibo1(n2-2)

for i in range(0, 10):
    print(fibo1(i))

def fact_res(n):
    if n == 0:
        return 1
    else:
        return n * fact_res(n-1)

rs = fact_res(5)
print("fact of 5! is", rs)

# filter
nums = [1,3,5,4,6,8,9,11,6,13]
even = list(filter(lambda n: n % 2 == 0, nums))
print("even nums list is", even)

odd = list(filter(lambda n: n % 2 != 0, nums))
print("odd nums list is", odd)

# map()
doublee = list(map(lambda n: n*2, even))
print(doublee)
# reduce()
from functools import reduce

sum = reduce(lambda a, b: a+b, nums)
print("sums of value of nums of list", sum)

def div(a, b):
    print(a/b)

div(2, 4)

# decorators

def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)  # here we call func which is div(a,b) called
    return inner
div1 = smart_div(div)
div1(2, 4)

class Computer:
    company = "dell"  # class variable
    def __init__(self, cpu, ram):
        self.cpu = cpu  # it is instance variable
        self.ram = ram
    def config(self):
        print("hi my laptop has configure as follow", self.cpu, self.ram)
    # class method
    def get_method(cls):  # cls means class
        return cls.company
    # static method
    def info():
        print("hi it is static method")
com1 = Computer("i5", 8)
Computer.config(com1)
com2 = Computer("i5", 4)
Computer.config(com2)
print(Computer.get_method(Computer))  # get_method(Computer)
Computer.info()

# inner class
class Student:
    def __init__(self,name, rno):
        self.name = name
        self.rno = rno
# self.lap = self.Computer("i5", 8)
    def show(self):
        print("name=", self.name, "rno=", self.rno)


    class Computer:
        company = "dell"  # class variable

        def __init__(self, cpu, ram):
            self.cpu = cpu  # it is instance variable
            self.ram = ram

        def show(self):
            print("cpu=", self.cpu, "ram=", self.ram)
        # class method
        def get_method(cls):  # cls means class
            return cls.company

s1 = Student("nis", 2)
s2 = Student("ada", 3)

# print(s1.lap.company)
"""lap1 = s1.lap
lap2 = s2.lap
lap1.config()
lap2.config()"""
lap1 = Student.Computer("i5", 8)
lap2 = Student.Computer("i7", 16)
s1.show()
lap1.show()
s2.show()
lap2.show()

# inheritance

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feature(self):
        print("it is feature of parent class")

    def show(self):
        print("it is parent class show method")
        print("parents name=", self.name)

class child(Parent):
    def __init__(self, name, age, name1, age1):
        super().__init__(name, age)
        self.name1 = name1
        self.age1 = age1

    def feature1(self):
        print("it is feature of child class")

    def show1(self):
        print("it is child class show method")
        print("child name=", self.name1)

    # here we do not have method overloading
    def show1(self, n2):  # so it will overide show1() method of above
        self.n2 = n2
        print("it is child class show method")
        print("child name=", self.name1, self.n2)

c1 = child("hiteshbhai", 57, "nisarg", 22)
c1.feature()
c1.show()
c1.feature1()
# c1.show1()  # so it will give error if we do overloading
c1.show1(10)

class Student:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def __add__(self, other):
        m1 = self.n1 + other.n1
        m2 = self.n2 + other.n2
        s3 = Student(m1, m2)
        return s3
    def __gt__(self, other):
        v1 = self.n1 + self.n2
        v2 = other.n1 + other.n2
        if v1 > v2:
            return True
        else:
            return False
    def __str__(self):
        return "n1={} n2={}".format(self.n1, self.n2)

s1 = Student(50, 30)
s2 = Student(30, 40)

s3 = s1 + s2  # Student._add__(s1,s2)
print(s3.n1, s3.n2)

if s1 > s2:  # Student.__gt__(s1,s2)
    print("s1 is win")
else:
    print("s2 is win")

print(s3)  #  Student.__str__(s3)

a=5
b=0
try:
    print(a/b)
except Exception as e:
    print("you cannot divide a number by 0", e)
finally:
    print("it is finally block")
print("bye")

from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)

t1 = Hello()
t2 = Hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("bye")

# file

f = open('my', 'r')
print(f.read())

f1 = open('abc', 'w')
f1.write("hi\n")
f1.write("my name is nisarg\n")


f = open('my', 'r')
f1 = open('abc', 'a')

f1.write(f.read())

f = open("img.jpg", 'rb')
f1 = open("mypic.jpg", 'wb')
for i in f:
    print(i)
    f1.write(i)
