name = input("What is your name? ")
country = input("What country do you live in? ")
country = country.upper() #use the "." to insert things with a list to help
print(country)


#some functions:
message = "Hello world"
print(message.find("world"))            #where is world? is on the six letter of the message, it gives the position - sometimes the count starts in 0
print(message.count("o"))               #count the "o" letter in the message
print(message.capitalize())             #captilize the first letter
print(message.replace("Hello", "Hi"))   #replace Hello to Hi


#Programmers do not memorize all these functions, so how they find them when they need it?
#IntelliSense
#Documentation
#Internet searches



#Example with a postal code:
postalCode = " "  #sometimes the code don't recognize it as a string, so, when this happens, create a line like that, a empty string, and then you put thins on that
postalCode = input("Please enter your postal code: ")
print(postalCode.upper())



#Code with mistakes on each line:
#message = Hello World
#23message = "Hello World"
#New Message = "Hi There"
#print(message.upper)
#print(mesage.lower())
#print(message.count())

#Code writed correctly:
message = "Hello World"
message23 = "Hello World"
NewMessage = "Hi There"
print(message.upper())   #DON'T FORGOT THE PARENTHESES
print(message.lower())   #DON'T FORGOT THE PARENTHESES
print(message.count("e"))