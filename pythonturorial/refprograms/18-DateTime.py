#DateTime
#https://www.w3schools.com/python/python_datetime.asp
from datetime import date
from datetime import time
from datetime import datetime
def main():
 	 ##DATETIME OBJECTS
     #Get today's date from datetime class
    today=datetime.now()
    print(today)
  # Get the current time
    t = datetime.time(today)
    print("The current time is", t)
 #weekday returns 0 (monday) through 6 (sunday)
    wd = date.weekday(today)
 #Days start at 0 for monday
    days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print("Today is day number %d" % wd)
    print("which is a " + days[wd])

if __name__== "__main__":
    main()

#Formatting Y - Year - four numbers

from datetime import datetime
def main():
    now = datetime.now()
    print(now.strftime("%Y"))

if __name__== "__main__":
    main()

#Formatting y - Year last two numbers

from datetime import datetime
def main():
    now = datetime.now()
    print("Formatting")
    #year in 4 digits 2018
    print(now.strftime("%Y"))
    #year in 2 digits 18
    print(now.strftime("%y"))
    #Day in full for example Friday
    print(now.strftime("%A"))
    #Day in short for example Fri
    print(now.strftime("%a"))
    #Month in Full for example May
    print(now.strftime("%B"))
    # Month in Full for example May
    print(now.strftime("%b"))
    # Day of the month for example 18
    print(now.strftime("%d"))

if __name__== "__main__":
    main()


#
#Example file for formatting time and date output
#
from datetime import datetime
def main():
   #Times and dates can be formatted using a set of predefined string
   #Control codes
      print("Local date time ")
      now= datetime.now() #get the current date and time
      #%c - local date and time, %x-local's date, %X- local's time
      print(now.strftime("%c"))
      print(now.strftime("%x"))
      print(now.strftime("%X"))
##### Time Formatting ####
      #%I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM
      print(now.strftime("%I:%M:%S %p")) # 12-Hour:Minute:Second:AM
      print(now.strftime("%H:%M")) # 24-Hour:Minute
if __name__== "__main__":
    main()


import datetime
today_date = datetime.date.today()
print(today_date)
new_today_date = today_date.strftime("%d/%m/%Y")
print(new_today_date)

#Future date
import datetime

x = datetime.datetime(2019, 12, 31)

print(x)


import time
epoch =time.time()
print("epoch",epoch)
t = time.localtime(epoch)
print('local time',t)
d = t.tm_mday
m = t.tm_mon
y = t.tm_year
print('Current date is %d-%d-%d' %(d,m,y))
te = time.ctime(epoch)
print('Ctime : epoch ',te)
t = time.ctime()
print('ctime ',t)

from datetime import *
now = datetime.now()
print(now)
print('Date now {}/{}/{}'.format(now.day,now.month,now.year))
print('Time now {}:{}:{}'.format(now.hour,now.minute,now.second))

today = datetime.today()
print("Today's date and time",today)
td = date.today()
print("Today's date",td)
d = date(1980,1,1)
print('date of Birth',d)
t = time(7,5)
print('time of birth',t)
dt= datetime.combine(d,t)
print('Date and time of birth 1st kid',dt)
dt1 = datetime(year=2016,month=6,day=24,hour=19,minute=59)
print('date 1',dt1)
dt2 = dt1.replace(year=2018)
print('Date and time of 2nd kid birth',dt2)

'''
strf format
'''
x = datetime.now()
print('current date and time',x)

print(x.strftime("%a"))


day = input ("Enter date in dd/mm/yyyy format")
d, m, y = day.split('/')
if (int(y)%4 == 0):
    print('its a leap year')
else:
    print('its not a leap year')
    
d,m,y = input("Enter date in dd/mm/yyyy format").split('/')
print (d,m,y)
d,m,y = [int (x) for x in input("Enter date in dd/mm/yyyy format").split('/')]
print ('converted to int' ,d,m,y)
    
lst = [int (x) for x in input("Enter date in dd/mm/yyyy format").split('/')]
print('list ',lst)

a,b,c=[10,20,30]
print(a,b,c)

'''
https://www.w3resource.com/python/python-date-and-time.php
'''
import datetime
today = datetime.date.today()
print('today ',today)
new_year = datetime.date(2020, 1, 1)
print(new_year)

#import datetime
#Time object
noon = datetime.time(12, 0, 0)
print(noon)

# Current datetime
now = datetime.datetime.now()
print(now)

# Datetime object
millenium_turn = datetime.datetime(2020, 1, 1, 0, 0, 0)
print(millenium_turn)


# The size of each step in days
day_delta = datetime.timedelta(days=1)

start_date = datetime.date.today()
end_date = start_date + 7*day_delta

for i in range((end_date - start_date).days):
    print(start_date + i*day_delta)
    
    
from datetime import datetime, timedelta
now = datetime.now()
then = datetime(2018, 1, 1)
delta = now-then
print(delta)

from datetime import datetime, timedelta
now = datetime.now()
then = datetime(2019, 5, 23)
delta = now-then
print(delta.days)
# 60
print(delta.seconds)
# 40826


from datetime import date, timedelta

current_date = date.today().isoformat()   
days_after = (date.today()+timedelta(days=30)).isoformat()  

print("\nCurrent Date: ",current_date)
print("30 days after current date : ",days_after)

from datetime import date, timedelta

current_date = date.today().isoformat()   
days_before = (date.today()-timedelta(days=30)).isoformat()

print("\nCurrent Date: ",current_date)
print("30 days before current date: ",days_before)

import time
from datetime import datetime
seconds_since_epoch=time.time()  #1469182681.709

utc_date=datetime.utcfromtimestamp(seconds_since_epoch)
print(utc_date)

import datetime

today = datetime.date.today()
print('Today:', today)

yesterday = today - datetime.timedelta(days=1)
print('Yesterday:', yesterday)

tomorrow = today + datetime.timedelta(days=1)
print('Tomorrow:', tomorrow)

print('Time between tomorrow and yesterday:', tomorrow - yesterday)



