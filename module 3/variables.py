#Rules:
#firstName and firstname are two different variables - because the N is on case up
#a variable can't start with a number, but you can use a number in the middle or in the end of it

#Tips:
#don't craeate a variable with a long name, make your life easier and write a small one
#put comments in lines that have librarys and stuff like that to remember in the future what did you do

#Names for variables:
#Variabel1 - good, but don't use the name variable, use another name
#FirstName - good
#Date - not so good
#Name3 - good
#DOB - interesting, a little confusing, but good, don't use in a corporation, use in personal codes
#DateOfBirth - good
#YourFavoriteSignInTheHoroscope - soooooooooooo long


#Manipulating variables:
firstName = input("What is your first name? ")
lastName= input("What is your last name? ")
print("Hello " + firstName + " " + lastName) #use the sign of plus to combine two variables


#Create a friendly output:
print("Hello, " + firstName)


#Story program:
animal = input("What is you favorite animal? ")
building = input("Name a famous building: ")
color = input("What is your favorite color? ")
print("Hickory Dickory Dock!")
print("The "+color+" "+animal+" ran up the "+building)



#Manipulating variable 2:
message = 'Hello World'
print(message.lower())
print(message.upper())
print(message.swapcase())
#they made different things

#another example:
name = input("What is your name? ")
country = input("What country do you live in? ")
country = country.upper()
print("\nHello, "+name+". You live in "+country)