import datetime as dt
import calendar

def findDay(date):
    born = dt.datetime.strptime(date, "%d %m %Y").weekday()
    return (calendar.day_name[born])

date = input("Enter date-month-year: ")
print(findDay(date=date))