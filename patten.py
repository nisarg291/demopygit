"""
    H
   HHH
  HHHHH
 HHHHHHH
HHHHHHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
                    HHHHHHHHH
                     HHHHHHH
                      HHHHH
                       HHH
                        H
"""
"""
n = 5
z = 1
for i in range(n):

    for j in reversed(range(i,n-1)):
        print(" ", end="")
    for k in range(z):
        print("H", end="")
    z += 2
    print()

for i in range(1, 15):
    for j in range(1, 29):
        if j < 3 or j > 27:
            print(" ", end="")
        elif 7 <= i <= 9 and 1 < j < 28:
            print("H", end="")
        elif i < 7 or i > 9:
            if 3 <= j <= 7 or 23 <= j <= 27:
                print("H", end="")
            else:
                print(" ", end="")
    print()
z = 9

for i in range(n):

    for j in range(0,28):
        if j < 20:
            print(" ", end="")
    for j in reversed(range(i)):
        print(" ", end="")
    for k in range(z):
        print("H", end="")
    z -= 2
    print()
"""
thickness = int(input("enter thickness"))  #This must be an odd number
c = 'H'
#top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):  # here 1to 10 and center is 3,4,5,6,7 & center of 11 to 40 is 23,24,25,26,27
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

print('h'*1)
