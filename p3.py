i = 1
j = 1
while i < 10:
    j = 1
    while j < 10:
        print(i, j)
        j += 1
    i += 1

limit = int(input("enter a limit"))
n = int(input("enter a num"))
i = 1
while i <= limit:
    if i == n:
        print(n, " is found")
        break
    print(i)
    i += 1

limit = int(input("enter a limit"))
n = int(input("enter a num"))
i = 1
while i <= limit:

    if i == n:
        print(n, " is found")
    else:
        print(i)
    i += 1
    continue
