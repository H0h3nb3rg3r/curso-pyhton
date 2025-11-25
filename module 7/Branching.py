#Branching: "ramificação" in portuguese

#Right code of last class:
#What will appear on the screen if deposit is 150?
#What will appear on the screen if deposit is 50?
#What will appear on the screen if deposit is exactly 100?:
deposit = float(input("How much do you want to deposit: "))
if deposit > 100: #101 or more - NOT 100
    print("Enjoy your toaster!")
else: #if you print 100 or less, if the condition is NOT true
    print("Enjoy your mug!")
print("Have a nice day!")



#You can use boolean:
freeToaster = False #Needs to initialize it
#if I don't put that is False and then type "50", the code will crash
deposit1 = float(input("How much do you want to deposit: "))
if deposit1 > 100:
    freeToaster = True #Set boolean variable freeToaster to True - True: "T" needs to be upper case
#If the variable freeToaster is true, the print statement will execute:
if freeToaster:
    print("Enjoy your toaster!")
print("Have a nice day!")
#IT'S BETER TO DO IN THAT WAY IF YOU ARE WORKING WITH CODES, OR IF YOU'RE WRITTING BIG CODES

#A Boolean variable is one that holds the value true or false