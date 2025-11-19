#What does 2/5/2014 represent?
#It's YEAR - MONTH - DAY
#But what if you want to display the date with a different format?:
import datetime
currentDate = datetime.date.today()
print(currentDate.strftime("%d %B %Y, %A"))
#strftime allows you to specify the date format
#%d = day
#%b = month in letters - the abbreviation
#%B = month in leeters - the full month name
#%y = year, but just the last two digits of the year
#%Y = year, the 4 digit year
#%a = day of the week abbreviated
#%A = day of the week in full name
#%m = minutes
#Check the site if you forgot the % of the dates



#Code example:
#Could you print out a wedding invitation?
#"Please attend our event Sunday, July 20 in the year 1997"
import datetime
currentDate2 = datetime.date(1997, 7, 20)#this line specify the date
print(currentDate2.strftime("Please attend our event %A, %B %d in the year %Y"))



#How many days do I have to my birthday?:
import datetime
currentDate4 = datetime.date.today()
userInput = input("When is your next birthday? (mm/dd/yyyy) ")
birthday = datetime.datetime.strptime(userInput, "%m/%d/%Y").date()
#Why did we lis datetime twice?:
#Because we are calling the strptime function, which is part of the datetime class, which is in datetime module
print(birthday)
days = birthday - currentDate4
print("Your next brithday will be in", days.days, "days")



#How many days do I have to my birthday?: - NOT MADE UP IN THE CLASS
import datetime
userInput2 = input("Whats is your birthday? (mm/dd/yyyy) ")
birthday2 = datetime.datetime.strptime(userInput2, "%m/%d/%Y")
currentDate3 = datetime.date.today()
BirthdayThisYear = datetime.date(currentDate3.year, birthday2.month, birthday2.day)
if BirthdayThisYear < currentDate3:
    BirthdayNext = datetime.date(currentDate3.year + 1, birthday2.month, birthday2.day)
else:
    BirthdayNext = BirthdayThisYear
DaysRemaining = (BirthdayNext - currentDate3).days
print(f"You have {DaysRemaining} days until your birthday!")
#"f" in the print means your are going to put a variable in the print