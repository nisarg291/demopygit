import turtle
a = 5
b = 5
"""
my_turtle = turtle.Turtle()
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
"""
my_turtle = turtle.Turtle()

def square():

    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)

square()
square()
square()
square()
my_turtle.forward(200)
square()
square()
square()
square()

elephant_weight = 3000
ant_weight = 0.1
if elephant_weight > ant_weight:
    my_turtle.forward(200)
    square()
else:
    my_turtle.left(90)
    my_turtle.forward(100)
    square()

quazi: "happy"
while quazi == "happy":
    square()
