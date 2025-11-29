#COUNTING:
for steps in range(4):
    print(steps)
#i starts in 0, in this loop, will be printed:0, 1, 2, 3

for steps2 in range(1,4):
    print(steps2)
#this will never reach the high value, in this case for, it will print: 1, 2, 3

for steps3 in range(1,10,2):
    print(steps3)
#1 to 9 jumping 2 numbers, it will print: 1, 3, 5, 7, 9


for steps4 in [1,2,3,4,5]:
    print(steps4)
#it will print: 1, 2, 3, 4, 5. In this case will execute the last value because we specified it

import turtle
for color in ["red", "blue", "green", "black"]:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)