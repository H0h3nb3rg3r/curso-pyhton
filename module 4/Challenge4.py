#Create a loan calculator:
#Have the user enter the cost of the loan, the interest rate, and the number of years for the loan
#Calculate monthly payments with the following formula:
#M = L[i(1+i)n] / [(1+i)n-1]
#M - monthly payment
#L - loan amount
#i - interest rate(for an interest rate of 5%, i = 0.05)
#n = number of payments
M = 0
L = float(input("please insert the value of the loan: "))
i = float(input("insert your interest rate in %: ")) / 100
#divide per 100 because the tax rate needs to be 0.05, if the user type 5 for example
nInYears = float(input("insert the number of years for the loan: "))
nInMonths = nInYears * 12
M = L * (i * (1 + i)**nInMonths) / ((1 + i)**nInMonths - 1)
print("Your monthly payment will be: $", M)
#use comma to put a number
print("Your monthly payment will be: $%.2f" % M)
#or use a pecentage signal to do it, but it will just work if you put a percentage in the print