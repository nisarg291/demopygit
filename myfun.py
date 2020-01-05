
def add_sub(a, b):
    c = a+b
    d = a-b
    return c, d

res1,res2 = add_sub(5, 3)
print("add. is:", res1, "sub is", res2)

def add_sub_mul_div(a, b):
    c = a+b
    d = a-b
    e = a*b
    f = a/b
    return c, d, e, f

res1,res2,res3,res4 = add_sub_mul_div(5, 2)
print("add. is:", res1, "sub is", res2,"mul. is:", res3, "div is", res4)

def swap_value(x = 5, y= 6):
    x = x + y
    y = x - y
    x = x - y
    s = "inner x={}, y={}"
    print(s.format(x, y))
    # return x, y


def swap(ls1 =[10, ], ls2 =[20, ]):  # here it does not have any pass by reference so we convert into list and pass list as par.
    for i in range(len(ls1)):
        tem = ls1[i]
        ls1[i] = ls2[i]
        ls2[i] = tem
    s = "inner ls1={}, ls2={}"
    print(s.format(ls1, ls2))


x = 10
y = 20

s = "before swap by value x={}, y={}"
print(s.format(x, y))

swap_value(x, y) # swap by value fun is called

s = "after swap by value x={}, y={}"
print(s.format(x, y))
x = 10
y = 20
ls1 = [x, ]
ls2 = [y, ]

s = "before swap by list ls1={}, ls2={}"
print(s.format(ls1, ls2))

swap(ls1, ls2)  # swap by list fun is called

s = "after swap by list ls1={}, ls2={}"
print(s.format(ls1, ls2))

ls1 = [10, 20, 30]
ls2 = [20, 30, 40]
s = "before  by list ls1={}, ls2={}"
print(s.format(ls1, ls2))
print()
swap(ls1, ls2)  # swap by list fun is called
print()
s = "after  by list ls1={}, ls2={}"
print(s.format(ls1, ls2))

swap()

swap_value()

def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)

person("navin", age=28, city="Mumbai", mon="78020")
