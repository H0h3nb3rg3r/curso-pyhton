#Formatiing the numbers:

print("I have %d cats" % 6)
#Output: I have 6 cats

print("I have %3d cats" % 6)
#Output: I have   6 cats

print("I have %03d cats" % 6)
#Output: I have 006 cats

print("I have %f cats" % 6)
#Output: I have 6.000000 cats

print("I have %.2f cats" % 6)
#Output: I have 6.00 cats

#float has decimal numbers after the comma and decimal don't


#Example with formatted numbers:
area = 0 #optional line
height = 10
width = 20
area = width * height /2
#print("the area of the triangle would be " + area)#ERROR LINE, DONT WORK WITH NUMBERS
print("the area of the triangle would be %d" % area)#in cases of numbers, we need to use this line
print("the area of the triangle would be %f" % area)#other line that works
print("the area of the triangle would be %.2f" % area)#other line that works



#other examples:
print("Myfavorite number is %d !" % 98)
print("Myfavorite number is %6d !" % 98)
print("Myfavorite number is %06d !" % 98)





#Other ways to format numbers. Formatting numeric values:

print("I have {0:d} cats".format(6))
#Output: I have 6 cats

print("I have {0:3d} cats".format(6))
#Output: I have   6 cats

print("I have {0:03d} cats".format(6))
#Output: I have 0006 cats

print("I have {0:f} cats".format(6))
#Output: I have 6.000000 cats

print("I have {0:.2f} cats".format(6))
#Output: I have 6.00 cats

#0 means that the count starts in 0, position 0. 6 is at position 0 in the count


#Same examples, but with the .format syntax to include numbers our outputs:
print("The area of the triangle would be {0:f} ".format(area))
print("The area of the triangle would be {0:.2f} ".format(area))

#Other same examples:
print("My favorite number is {0:d} ".format(98))

#Other example:
print("Here are three numbers! The first is {0:d} The second is {1:4d} And the last number is {2:d}".format(7,8,9))
#This is an example with multiple numbers, nad we need to use this: #0 means that the count starts in 0, position 0. 6 is at position 0 in the count



#We can use a "\" - back slash - to indicate a command that continues on the next line, e.g.:
total = 5 + 6 + 8 \
+ 6 + 2
print(total)

#Other example:
print("Here are three numbers! \
      The first is {0:d} The second is {1:4d} And the last number is {2:d}".format(7,8,9))#WRONG WAY TO DO IT

print("Here are three numbers!" + \
      "The first is {0:d} The second is {1:4d} And the last number is {2:d}".format(7,8,9))#RIGHT WAY TO DO IT

print("Here are three numbers!" + \
"The first is {0:d} The second is {1:4d} And the last number is {2:d}".format(7,8,9))#it's also right, but give a space from the beginning of the line, 
#the space who python gives'