#Correcting the code of part I and other part:
bestTeam = "SENATORS"
favoriteTeam = input("What is your favorite hockey team? ")
#if favoriteTeam.upper() == "Senators":  - it will not work
#if favoriteTeam.upper() == bestTeam: - it will work
if favoriteTeam.upper() == "SENATORS":
    print("Yeah! Go Sens Go")
    print("But I miss Alfredsson")
print("It's okay if you prefer football/soccer")
#USE .lower() or .upper() IN THIS KIND OF CODES - IFS


#Two ways to write codes:
#if answer == "yes":
#if not answer == "no":
#OR
#if total < 100:
#if not total >= 100:
#Choose one and put in your code!
#But prefer the first one, it's better to think when you're writting a code
#E.g:
#if courseCompleted == "yes":
#if total < 50:
#if notVaccinated == "yes":


#E.g. code with numbers:
deposit = 150
if deposit > 100:
    print("You get a free toaster!")
print("Have a nice day")
#What will appear on the screen if deposit is 150?
#What will appear on the screen if deposit is 50?
#What will appear on the screen if deposit is exactly 100?:
#E.g. code with numbers, but asking the user to put the number:
deposti1 = float(input("How much do you want to deposit: "))
#if float(deposit) > 100: - it also will work, but you can't put float in the input - but prefer the other style
if deposti1 > 100: #101 or more - NOT 100
    print("Enjoy your toaster!")
print("Have a nice day")