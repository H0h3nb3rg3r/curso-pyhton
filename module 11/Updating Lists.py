guests = ["Christopher", "Susan", "Bill", "Satya"]
print("first value is: " + guests[0])

#Changing a value in a list:
guests[0] = "Steve"
print("first value is now: " + guests[0])

#Adding a value in the end of the list:
guests.append("Steve")
print(guests[-1]) #It will print the last value of the list

#Removing a value from the list:
guests.remove("Bill")
print(guests[2])

#Command to to delete some value in the list:
del guests[0]
print(guests[0])



#E.g.:
guests2 = ["Christopher", "Susan", "Bill", "Bill"]

guests2.append("Colin")

#Updating a value in the list:
guests2[3] = "Sonal"
print(guests2[-1])
print(guests2[3])

guests2.remove("Bill")
#If it have two Bill, the code will remove just one Bill
del guests2[0]
print(guests2[0])
print(guests2)