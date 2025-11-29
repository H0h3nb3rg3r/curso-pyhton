#E.g.:
import turtle
turtle.speed(100) #set the speed of the drawing
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
    for mmoresteps in range (4): #this line will be executed 16 times, because each loop has 4 times, and 4*4=16
        turtle.forward(50)
        turtle.right(50)


#Another e.g.:
for steps in range(5):
    turtle.forward(100)
    turtle.right(360/5)
    for mmoresteps in range (5): #this line will be executed 25 times, because each loop has 5 times, and 5*5=25
        turtle.forward(50)
        turtle.right(360/5)


#Another e.g.:
nbrSides = 5
for steps in range(nbrSides):
    turtle.forward(100)
    turtle.right(360/nbrSides) #360/4=90
    for mmoresteps in range (nbrSides):
        turtle.forward(50)
        turtle.right(360/nbrSides)