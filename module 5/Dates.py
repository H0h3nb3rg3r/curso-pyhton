#How many days do I have to my birthday?
#The datetime class allows us to get the current date and time
#The important statement gives us access to the funcionality of the datetime class
import datetime
#today is a function that returns today's date
print(datetime.date.today())
#RIGHT CODE

#other way to do it:
import datetime
currentDate = datetime.date.today() #storage the date without showing on the screen
print(currentDate)


#today = datetime.date
#ERROR CODE



#Different parts of the date:
import datetime
currentDate2 = datetime.date.today()
print(currentDate2)
print(currentDate2.year)
print(currentDate2.month)
print(currentDate2.day)


#When is my project due?
#I want a book appointment in two weeks, what will the date be?