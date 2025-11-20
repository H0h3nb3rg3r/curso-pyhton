#We also use datetime to store times:
import datetime
currentTime = datetime.datetime.now()
print(currentTime)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)

#We can use strftime:
import datetime
currentTime2 = datetime.datetime.now()
print(datetime.datetime.strftime(currentTime2, "%H:%M"))
# %H - hours(24hr clock)
# %l - hours(12hr clock)
# %p - AM or PM
# %m - minutes
# %s - seconds



#Other code:
import datetime
currentTime3 = datetime.datetime.now()
print(currentTime3.minute)