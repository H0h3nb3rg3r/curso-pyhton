#Ask a user to enter the deadline for their project
#Tell them how many days they have to complete the project
#For extra credit, give them the answer as a compination of weeks & days
#Hint: you will need some of the math functions form the module on numeric values

import datetime
currentDate = datetime.date.today()
userInput = input("Insert the deadline of your project (dd/mm/yyyy): ")
deadline = datetime.datetime.strptime(userInput, "%d/%m/%Y").date()
days = deadline - currentDate
totalDays = days.days
weeks = totalDays // 7
remainingDays = totalDays % 7
print("Your deadline is in ", weeks, "week(s) and ", remainingDays, " day(s)")