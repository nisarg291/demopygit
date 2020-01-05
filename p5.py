def first():
    print("this is my first fun")

first()

def add(a, b):
    c = a + b
    # print(c)
    return c

x = int(input("enter"))
y = int(input("enter"))
z = add(x, y)
print(z)

e = input("enter your email")
p = input("enter your pass")

def login(email1, password1):
    if email1.lower() == "a@b.com" and password1 == "abc123":
        # print("login is successful")
        return 1
    else:
        # print("login is unsuccessful")
        return 0

flag = login(e, p)
if flag == 1:
    print("successful")
else:
    print("unsuccessful")

PWD = "nisarg24680"
for i in range(3):
    password1 = input("enter a password")
    if password1 == PWD:
        print("login is successful")
        break
    else:
        print("password is incorrect and try again", (2 - i), " try remains")
else:
    print("account is blocked")

def login2(email1, password1):
    if email1.lower() == "a@b.com" and password1 == "abc123":
        return 0
    else:
        if email1.lower() == "a@b.com":
            # print("login is successful")
            return 1
        else:
            # print("login is unsuccessful")

            if password1 == "abc123":
                return 2
            else:
                return 3
global email
global password
email = input("enter your email")
password = input("enter your pass")
flag = login2(email, password)

def my(flag):
    global email
    global password
    f = 0
    s = 0
    while f == 0:
        if flag == 0:
            print("email and password is correct ")
            f = 1
            break
        if flag == 1:
            if email == "a@b.com" or s == 0:
                print("password is wrong ")
                print(email)
                password = input("enter your pass again")
                flag = login2(email, password)
            else:
                print("password is wrong ")
                print(email4)
                password4 = input("enter your pass again")
                flag = login2(email4, password4)
        if flag == 2:
            print("email is wrong")
            email4 = input("enter your email again")
            password4 = input("enter your pass again")
            flag = login2(email4, password4)
            s += 1
        if flag == 3:
            print("email and password wrong")
            email4 = input("enter your email again")
            password4 = input("enter your pass again")
            flag = login2(email4, password4)
            s += 1
    else:
        print("stop")

my(flag)

