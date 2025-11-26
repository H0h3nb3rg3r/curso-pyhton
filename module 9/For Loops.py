#Loops:
#Pour a cup of cofee for each guest
#Wash the dishes until they are all clean

#E.g.:
#turtle is a library to draw a line in the screen
import turtle
turtle.color("green")
turtle.forward(100)
turtle.color("blue")
turtle.right(90)
turtle.forward(100)
turtle.backward(80)
turtle.left(100)
turtle.right(500)

#draw a square:
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
#the lines repeat


#using for - is a loop to specify how much do you want that code to repeat, in this case, it will repeat 4 times:
#you can just change "steps" who is the variable, and the number in the parentheses, that is how much it will repeat:
#we use "i" as the name of variable, becaus i is the "official name" for the accountant
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.color("red")#this part will not repeat, because it's not on the loop
turtle.forward(200)#this part will not repeat, because it's not on the loop


#IMPORTANT ---LOOPS STARTS IN 0 --- IMPORTANT