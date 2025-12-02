guests = ["Christopher", "Susan", "Bill", "Satya"]
#Command to locate something, if have two, the code will locate the first:
print(guests.index("Bill"))

#What if we search a value that doesn't exists in the list:
#print(guests.index("Steve"))
#The code will not run, it will have an error


#Option 1 to loop through a list:


#Find out how many entrie are in the list:
nbrValueInList = len(guests)
print("Your code have", nbrValueInList, "values")

#FOR to print 4 values of the list in order, each name on a new line. This count in for will starts in 1:
for steps in range(nbrValueInList):
    print(guests[steps])


#Option 2 to loop through a list:


#Specify the name of your list and a variable name to hold each entry as you go through the loop:
for currentGuests in guests:
#The variable guests will ocntain the values as we go through the loop:
    print(currentGuests)





#Code to put the values in alphabetical order:
guests.sort()
for guests in guests:
    print(guests)