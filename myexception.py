try:
    print(x)
except:
    print("An exception occurred")

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

#Raise an exception
"""As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.

Example
Raise an error and stop the program if x is lower than 0:"""

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")  # raise Exception is same as throw a exception
# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.
