names = ["nis", "nik", "meh"]
for i in names:
    print(i)
for i in range(1, 10, 3):
    print(i)
for i in reversed(range(1, 100)):
    for j in names:
        print(i, j)
sum = 0
lst = [3, 4, 5, 6, 7, 8, 9]
for i in lst:
    sum += i
print("sum is=", sum)

lst1 = [2, 1.5, 3.0, 3]
for i in lst1:
    if i % 1 == 0:
        print(i, "is int")
    else:
        print(i, "is float")

while i <= 10:
    if i == 5:
        print(i)
        break
    else:
        print(i)
    i += 1
else:
    print("whole loop done")

lst = ["nis@gmail.com", "nik@gmail.com", "meh@gmail.com", "kes@gmail.com"]
email = input("enter a email")
for i in lst:
    if email == i:
        print("email is exist")
        break
else:
    print("email is not found")
