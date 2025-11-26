#If you're in England say hello, if you are in Germany say guten tag, if you are in France say bonjour,...:
country = input("Where are you from? ")
if country.upper == "CANADA":
    print("Hello")
elif country.upper == "GERMANY":
    print("Guten Tag")
elif country.upper == "FRANCE":
    print("Bonjour")
else:
    print("Aloha/Ciao/G'Day")
#elif is another if - else if - "senão se" in portuguese
#Test your code with all the ways possible

#E.g.:
team = input("Enter your favorite hockey team: ").upper() #EASIER WAY TO UPPER THIS STRING
if team == "FLYERS":
    print("Best team ever!!")
elif team == "SENATORS":
    print("Go Sens Go!")
elif team == "RANGERS":
    print("Go Rangers")
else:
    print("I don't have anything clever to say here")