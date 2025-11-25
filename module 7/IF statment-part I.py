#Should I drive or take a bus?:
#Am I late? What's the price of gas?
#Should I cook at home or go out?:
#Do I have any food at home? Do I have enough money to go out?

#Codes that solve problems in real situations

#E.g. code:
answer = input("Would you like express shipping? ")#"=" just one equal symbol is to put something inside the variable
if answer == "yes": #if is a condition, and we need to put ":". "==" is to indicate exactly what was typed
    print("That will be an extra $10")#you need to let the space in the start to be inside the print
print("Have a nice day")#it's not on the print statement, so, it will be printed no matter the answer of the user

#Different symbols in pyhton:
#== - is equal to                      - if answer == "yes":
#!= - is not equal to                  - if answer != "no":
#<  - is less than                     - if total < 100:
#>  - is greater/more than             - if total > 100:
#<= - is less than or equal to         - if total <= 100:
#>= - is greater/more than or equal to - if total >= 100:

#other e.g. code:
favoriteTeam = input("What is your favorite hockey team? ")
if favoriteTeam == "Senators":
    print("Yeah! Go Sens Go")
    print("But I miss Alfredsson")
print("It's okay if you prefer football/soccer")