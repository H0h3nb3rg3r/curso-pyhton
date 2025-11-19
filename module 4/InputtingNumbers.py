#example of asking to the user for an input:

salary = input("please enter your salary: ")
bonus = input("please enter your bonus: ")
paycheckAmount = salary + bonus
print(paycheckAmount)
#ERROR CODE


#other example, but without asking:
salary1 = "5000"
bonus1 = "500"
payCheck = salary1 + bonus1
print(payCheck)
#ERROR CODE


#right code:
salary2 = 5000
bonus2 = 500
payCheck2 = salary2 + bonus2
print(payCheck2)

#other right code:
salary4 = int(input("please enter your salary: "))
bonus4 =  int(input("please enter your bonus: "))
payCheck3 = salary4 + bonus4
print(payCheck3)
#in numbers we need to put int or float before the input, input just works with words - IMPORTANT
#int is for entire numbers, and float is for decimal numbers



#Functions to convert from one datatype to another:
#int(value)   - converts to an integer
#long(value)  - converts to a long integer
#float(value) - converts to a floating number(i.e. a number that can hold decimal places)
#str(value)   - converts to a string


#other way to correct the code:
salary5 = input("please enter your salary: ")
bonus5 = input("please enter your bonus: ")
paycheckAmount2 = float(salary5) + float(bonus5)
print(paycheckAmount2)


#What happen if someone type "BOB" as their salary?:
#python won't accept, because just numbers are accepted