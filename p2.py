name = input("enter a name ")
gender = input("enter a gender ")
age = int(input("enter a age "))

if gender == "m" and age >= 21:
    print("Hello", name, ",you are eligible for marriage.")
elif gender == "m" and age <= 21:
    print("Hello", name, ",you are not eligible for marriage as legal age for (",gender,")is (21)")
elif gender == "f" and age >= 18:
    print("Hello", name, ",you are eligible for marriage.")
else:
    print("Hello", name, ",you are not eligible for marriage as legal age for (",gender,")is (18)")
