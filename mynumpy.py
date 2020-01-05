from numpy import *

arr = array([1, 2, 3, 4, 5])
print(arr)
arr = linspace(0, 15, 16)
print(arr)
arr = linspace(0, 5, 10)
print(arr)  # 0-5 is divided in 10 is part
arr = arange(1, 15, 2)  # here 2 is step or gap between 2 element
print(arr)
arr = logspace(1, 10, 5)  # it is start form 10^1 to 10^10 and divided into 5 parts
print(arr)
arr = logspace(1, 10, 5)  # it is start form 10^1 to 10^10 and divided into 5 parts
arr = zeros(5)  # 5 is size
print(arr)
arr = ones(6)
print(arr)
arr = ones(6, int)
print(arr)
arr =array([1,2,3,4,5])
arr=arr+5
print(arr)
arr1 =array([1,2,3,4,5])
arr2 =array([4,8,12,16,20])
arr3=arr1+arr2
print(arr3)
print(sin(arr1))
print(sinh(arr1))
print(cos(arr1))
print(tan(arr1))
print(cosh(arr1))
print(tanh(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sort(arr1))
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([4, 8, 12, 16, 20])
arr3 =arr1
print(id(arr1))  # for print address of arr1
print(id(arr3))
arr1 = array([1, 2, 3, 4, 5])
arr3 = arr1.view()
arr1[1] = 5
print(arr1)
print(arr3)
print(id(arr1))  # for print address of arr1
print(id(arr3))
arr1 = array([1, 2, 3, 4, 5])
arr3 = arr1.copy()
arr1[1] = 5
print(arr1)
print(arr3)
print(id(arr1))  # for print address of arr1
print(id(arr3))
print()
# print(concatenate(arr1, arr2))
# print(add(arr1, arr2))
s = "Www.Python.com"
print(s.swapcase())
a = "kloo"
print(len(a))

arr = array([
                [1, 2, 3, 4],
                [2, 3, 4, 4],
                [4, 5, 6, 4]
            ])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
arr1 = arr.flatten()
print(arr1)
arr2 = arr1.reshape(2, 6)
print(arr2)
arr2 = arr1.reshape(3, 4)
print(arr2)
arr2 = arr1.reshape(2, 2, 3)  # 3 dimentional
print(arr2)
arr = array([
                [1, 2, 3, 4],
                [2, 3, 4, 4],
                [4, 5, 6, 4]
            ])
m = matrix(arr)
print(m)
arr1 = array([
                [1, 2, 3],
                [2, 3, 4],
                [4, 5, 6],
                [6, 7, 8]
            ])
m1 = matrix(arr1)
print(m1)
m2 = m1 + m1
print(m2)
m2 = m1 * m
print(m2)