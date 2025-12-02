#Ask the user to enter the names of everyone attending a party
#Then return a list of the party guests in alphabetical order
#This will require pulling togheter everything we have learned so far, so let's walk through the thought process of idea to code

#Break the problem into steps:
#1- Ask the user to enter the name of everyone attending the party
#2- Put those value in a list
#3- Sort the list
#4- Print the sorted list

guests = []
name = " "
while name != "DONE":
    name = input("Enter guest name (enter DONE if no more names): ")
    guests.append(name)

guests.remove("DONE")
guests.sort()
print("Here is your list with the names in alphabetical order:")
for currentGuests in guests:
    print(currentGuests)