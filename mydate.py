import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()

print(x.year) # it will print year
print(x.strftime("%A"))  # it will print name weekday
# Creating Date Objects
"""To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.

Example
Create a date object:"""
x = datetime.datetime(2020, 5, 17)
print(x)

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))  # it will print  name month
x = datetime.datetime(2018, 6, 15)
print(x.strftime("%c"))  # Local version of date and time
print(x.strftime("%d"))  # it will print day of the month like 15
x= datetime.datetime.now()
print(x.strftime("%p"))  # for am/pm
print(x.strftime("%H"))  # for hours in 0-24 format
print(x.strftime("%I"))  # for Hour in 0-12 format
print(x.strftime("%M"))  # for minites 0-60
print(x.strftime("%S"))  # for second
print(x.strftime("%f"))  # for micro second

