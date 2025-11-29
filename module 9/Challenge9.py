#Get turtle to draaw an octagon
#Hint: to calculate the angle, you take 360 degrees and divide it by the number of sides the shape you are drawing
#Extra challenge: let the user specify how mnany sides the object will have and draw whatever they ask
#Double bonus challenge: add a nested loop to draw a smaller version of the object inside!


#FIRST CHALLENGE
import turtle
octagon = 8
for i in range(octagon):
    turtle.forward(100)
    turtle.right(360/octagon)


#SECOND CHALLENGE:
userObject = int(input("How many sides the object will have? "))
smallObject = userObject
for j in range(userObject):
    turtle.forward(100)
    turtle.right(360/userObject)
    for i1 in range(smallObject):
        turtle.forward(40)
        turtle.left(360/smallObject)