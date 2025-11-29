#Another e.g.:
import turtle
i = 0
while i <= 4:
    turtle.forward(100)
    turtle.right(90)
    i=i+1
#This code will draw 5 lines, because it will execute till reach 4, and the counter starts in 0

#The same code, but executing 4 times:
import turtle
j = 1
while j <= 4:
    turtle.forward(100)
    turtle.right(90)
    j=+1 #This is the same as j=j+1

#IMPORTANT --- BUT ALWAYS PREFER TO START WITH 0 --- IMPORTANT


#Another e.g.:
i1 = 0
while i1 < 3:
    turtle.forward(100)
    turtle.right(90)
#This code will stay executing forever, because we don't have the counter to control



#IMPORTANT --- PREFER TO USE FOR LOOPS --- IMPORTANT