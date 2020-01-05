from array import *


arr = array('i', [])
n = int(input("enter size of array"))
for i in range(n):
    x = int(input("enter"))
    arr.append(x)

print(arr)

newArr = array(arr.typecode, (a for a in arr))
print(newArr)
newArr = array(arr.typecode, (a * a for a in arr))
print(newArr)

val = int(input("enter val for search"))
print(arr.index(val))
k = 0
for e in arr:
    if e == val:
        print("index is", k)
    k += 1
