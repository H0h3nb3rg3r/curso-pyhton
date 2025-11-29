#"for" - "para" in portuguese
#"while" - "enquanto" in portuguese

#While loops:
#Pour a cup of coffee for each guests

#While do something while it is TRUE

#E.g.:
answer = "0"
while answer != "4":
    answer = input("What is 2 + 2? ")
print("Yes! 2 + 2 is 4!")
#while the user keep typing a number that is not 4, the code will still asking, till the user insert 4


#Another e.g.:
import turtle
i = 0
while i < 4:
    turtle.forward(100)
    turtle.right(90)
    i=i+1 #MOST IMPORTANT LINE
#This code will draw a square


#Another e.g.:
j = 0
while j <= 4:
    turtle.forward(100)
    turtle.right(90)
    j=j+1
#This code will draw 5 lines, because it will execute till reach 4, and the counter starts in 0