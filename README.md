# day-finder
Python Program that returns the day when given dd/mm/yy

It uses datetime and caldendar modules.
The funciton takes a paramater of dd/mm/yy and does `dt.datetime.strptime(date, "%d %m %Y)".weekday()` then returns `calendar.day_name` of the variable
