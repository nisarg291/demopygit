n = int(input("enter a num"))
if n % 2 == 0:
    if n % 7 == 0:
        print("number is divisible by 7")
    else:
        print("number is not divide by 7")
else:
    if n % 5 == 0:
        print("divide by 5")
    else:
        print("not divide by 5")


