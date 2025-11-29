#Create an etch a sketch program
#Have the user enter a pen color, a line length, and an angle
#Use turtle to draw a line based on their specifications
#Let them specify new lines over and over until they enter a line length of 0
#When the user specifies a line length of 0 stop drawing

import turtle
lineLength = "1"
while lineLength != "0":
    print("Type 0 to exit")
    color = input("What's the color that you want? Choose one: green or red or blue or black: ")
    lineLength = input("What's the line length? ")
    if lineLength == "0":
        break
    angle = int(input("What's the angle of the line? "))
    turtle.color(color)
    turtle.forward(int(lineLength))
    turtle.right(angle)
print("Amazing Draw!")