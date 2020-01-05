import random
import math
rval = random.random() * 100
billval = round(rval, 2)
print("your bill is", billval)
b = int(input("how many rs you want to pay"))

if b < billval:
    print("you want to pay extra charge",round(billval - b, 2))

else:
    print("we will pay next time", round(b - billval, 2))

val = float(input("enter a value in float"))

if val - math.ceil(val) > 0.5:
    print(math.floor(val))
else:
    print(math.ceil(val))



