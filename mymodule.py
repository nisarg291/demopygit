def myfun(name):
    print("hello" + name)
n = 5
for i in range(n):
    print(i+1, end="")

n = 5
arr = [2, 3, 5, 6, 6]
n1 = max(arr)
while max(arr) == n1:
    arr.remove(n1)
print(max(arr))

l1 = ["nisarg","nis", "meh", "nik", "deep", "dhruv"]
l2 = [10, 10, 30.5, 40.5, 30.5, 40]
i = 0
n2 = min(l2)

while i < len(l2):
    if l2[i] == n2:
        l2.remove(n2)
        n = l1[i]
        l1.remove(n)
    i += 1
j = len(l2) - 1
n1 = min(l2)
while j >= 0:
    if l2[j] == n1:
        print(l1[j])
    j -= 1
# l1 = ["nisarg","nis", "meh", "nik", "deep", "dhruv"]
# l2 = [10, 10, 30.5, 40.5, 30.5, 40]
l1 = ["Harsh", "Beria", "Varun", "Kakunami", "Vikas"]
l2 = [20, 20, 19, 19, 21]
l3 = []
i = 0
n2 = min(l2)

while i < len(l2):
    if l2[i] == n2:
        l2.remove(n2)
        n = l1[i]
        l1.remove(n)
    else:
        i += 1

# print(l1)
# print(l2)
j = 0
n1 = min(l2)
s1 = len(l2)
while j < s1:
    if l2[j] == n1:
        l3.append(l1[j])
    j += 1

l3.sort()
for i in l3:
    print(i)
x = 2.22
print(type(x))

avg = 26
# if variable type is int ya float for example 26.3 then round(avg,2) is not posible so only use format or % method
print(round(avg, 2))
print("{0:.2f}".format(avg))
print('%.2f' % avg)

avg = 26.4567
print(round(avg, 2))
print("{0:.2f}".format(avg))
print('%.2f' % avg)
str = "insert 0 5"
t = str.split()
print(t)
t =()
lst = [2, 3, 5, 4]
tup = tuple(lst)

# lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a: a + 10
print(x(5))
x = lambda a, b: a * b
print(x(5, 6))
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
"""Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument,
 and that argument will be multiplied with an unknown number:"""
def myfun(n):
    return lambda a: a * n

mydoubler = myfun(2)  # myfun have return statement so we have mydoubler variable to store the return value
print(mydoubler(11))
mytripler = myfun(3)
print(mytripler(11))
# iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self # it is same as __init__ fun but __iter__ is return self object

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()  # here myclass is object of MyNumber class
myiter = iter(myclass)  # so here it return self object and it store in myiter
for x in myiter:
    print(x)

import platform

x = dir(platform)
print(x)
