import random
email = "abc@gmail.com"
passw = "abcd"
email1 = input("enter email id")
pass1 = input("enter pass")
if email == email1.lower() or email == email1.upper():
    if passw == pass1:
        print("login is successful")
    else:
        print("password is wrong")
else:
    print("email is wrong")
password = random.random() * 100000
while password < 100000:
    password *= 10

print(round(password))