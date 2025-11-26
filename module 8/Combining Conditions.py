#Win the lottery, you need to decide what to do with the money, do this OR that, or do this AND that

#AND:
#both sides must be true:
wonLottery = True
bigWin = True
#Print statment only executes if both conditions are true
if wonLottery and bigWin:
    print("You can retire")

#Here are all the possible combinations:
#if firstCondition and secondCondition:
#First Condition | Second Condition | Statment is
#True            | True             | True
#True            | False            | False
#False           | True             | False
#False           | False            | False


#E.g.:
team = input("Enter your favorite hockey team: ").upper()
sport = input("Enter your favorite sport: ").upper()
if sport == "HOCKEY" and team == "RANGERS":
    print("I miss Messier")
else:
    print("I don't know that team")




#OR:
#This OR that
saturday = True
sunday = True

if saturday or sunday:
    print("You can sleep in")


#E.g.:
team1 = input("Enter your favorite hockey team: ").upper()
sport1 = input("Enter your favorite sport: ").upper()
if sport1 == "HOCKEY" and team1 == "RANGERS":
    print("I miss Messier")
elif team1 == "LEAFS" or team1 == "SENATORS":
    print("Good luck getting cup this year")
else:
    print("I don't know that team")



#You can combine multiple "and"/"or" in a single if statment:
month = input("Enter your favorite month with the first three letters: ").upper()
if month == "SEP" or month == "APR" or month == "JUN" or month == "NOV":
    print("There are 30 days in this month")
else:
    print("There are 31/28 days in this month")


favMovie = input("What is your favorite movie? ").upper()
favBook = input("What is your favorite movie? ").upper()
favEvent = input("What is your favorite movie? ").upper()
if favMovie == "STAR WARS" and favBook == "LORD OF THE RINGS" \
    and favEvent == "COMICON":
    print("You and I should hang out")
else:
    print("You and I should not hang out")




#Combining "and" and "or" in a single if:
country = input("What country are you from? ").upper()
pet = input("What animal is your pet? ").upper()
if country == "CANADA" and pet == "MOUSE" or pet == "BEAVER":
    print("Do you play hockey too?")
else:
    print("Do you play hockey at least?")


# --- IMPORTANT --- AND first, and then the code will check the OR --- IMPORTANT ---



#E.g. -  If the sport is hockey and the team iis the senators or leafs, display the cup message:
team2 = input("Enter your favorite hockey team: ").upper()
sport2 = input("Enter your favorite sport: ").upper()
#First way to do it:
sportIsHockey = False
if sport2 == "HOCKEY":
    sportIsHockey = True
teamIsCorrect = False
if team2 == "SENATORS" or team2 == "LEAFS":
    teamIsCorrect = True
if sportIsHockey and teamIsCorrect:
    print("Good luck getting the cup this year")
#Second way to do it:
if sport2 == "HOCKEY" and (sport2 == "SENATORS" or team2 == "LEAFS"):
    print("Good luck getting the cup this year")
#Put things in parentheses, because he need to check both, and in complexe codes you will need parentheses, so put parentheses always