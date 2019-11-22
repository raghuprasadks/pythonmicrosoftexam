
import calendar
#Create a plain text calendar
c= calendar.TextCalendar(calendar.MONDAY)
str= c.formatmonth(2019,7,0,0)
print(str)

#Create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.MONDAY)
str = hc.formatmonth(2019, 7)
print(str)


#loop over the days of a month
#zeroes indicate that the day of the week is in a next month or overlapping month
for i in c.itermonthdays(2019,7):
  print(i)

#The calendar can give info based on local such a names of days and months (full and abbreviated forms)
for name in calendar.month_name:
    print(name)
for day in calendar.day_name:
    print(day)

