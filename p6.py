from tkinter import *
lst = [1,2,3,4]
print(lst)
lst1 = [[1, 2], [3, 4], [5, 6]]
lst2 = [[1, 2], [3, 4], [5, 6]]
print(lst1[1][0])
print(lst1 + lst2)
lst3 = [1, 2, "hello", 12.5]
print(lst3)
print(len(lst3))
email = ["abc@gmail.com","nik@gmail.com"," nis@gmail.com"]
password = ["1234", "3456", "6789"]

e = input("email")
p = input("password")
i = 0;
for i in range(len(email)):
    if email[i] == e:
        if password[i] == p:
            print("successfully login")
            break
        else:
            print("password is not match")

else:
    print("login is unsuccessful")
def fun():
    email1 = input("enter email")
    pass1 = input("enter pass")
    i = 0
    for i in range(len(email)):
        if email1 == email[i]:
            if pass1 == password[i]:
                print("please change password");
                label1:
                    oldpass = input("enter old pass")
                    newp+ss = input("enter new pass")
                    repass = input("enter retype new pass")
                    if oldpass == password[i]:
                        if newpass == repass:
                            password[i] = newpass
                        else:
                            print("newpass and retype password is not same")
                    else:
                        print("oldpass is not match")
                        return label1;
            else:
                print("password is not found")
                fun();
        else:
            print("email is not found")
            fun();
    else:
        print("login is unsuccessful")

print(password)

