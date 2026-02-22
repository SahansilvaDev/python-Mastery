import datetime

b_day = datetime.datetime(2000, 5, 15)
print("Birthday:", b_day)  # output: Birthday: 2000-05-15 00:00:00
print("Year:", b_day.year)  # output: Year: 2000
print("Month:", b_day.month)  # output: Month: 5
print("Day:", b_day.day)  # output: Day: 15
print("Formatted Birthday:", b_day.strftime("%d-%m-%Y"))  # output: Formatted Birthday: 15-05-2000
print("Formatted Birthday:", b_day.strftime("%A, %d-%m-%Y"))  # output: Formatted Birthday: Monday, 15-05-2000

now = datetime.datetime.now()
print("Current Date and Time:", now)  # output: Current Date and Time: current date and time
print("Current Year:", now.year)  # output: Current Year: current year

today = datetime.date.today()
print("Today's Date:", today)  # output: Today's Date: current date

age = now.year - b_day.year
if (now.month, now.day) < (b_day.month, b_day.day):
    age -= 1
print("Age:", age)  # output: Age: calculated age


weekday = today.weekday()
print("Weekday (0=Monday):", weekday)  # output: Weekday (0=Monday): current weekday number

weekday = today.isoweekday()
print("ISO Weekday (1=Monday):", weekday)  # output: ISO Weekday (1=Monday): current ISO weekday number


t = datetime.time(14, 30, 0)
print("Time:", t)  # output: Time: 14:30:00

print("Hour:", t.hour)  # output: Hour: 14
print("Minute:", t.minute)  # output: Minute: 30
print("Second:", t.second)  # output: Second: 0


t = datetime.datetime.today()
print("Current Time:", t)  # output: Current Time: current time
print("Date", t.date())  # output: Date: current date
print("Time", t.time())  # output: Time: current time


t_delta = datetime.timedelta(days=10)
print("10 days from now:", t + t_delta)  # output: 10 days from now: date after 10 days                 
print("10 days ago:", t - t_delta)  # output: 10 days ago: date before 10 days                 

t_delta = datetime.timedelta(hours=10)
print("10 hours from now:", t + t_delta)  # output: 10 hours from now: date after 10 hours                 
print("10 hours ago:", t - t_delta)  # output: 10 hours ago: date before 10 hours                 


is_leap = (b_day.year % 4 == 0 and (b_day.year % 100 != 0 or b_day.year % 400 == 0))
print("Is Birth Year a Leap Year?:", is_leap)  # output: Is Birth Year a Leap Year?: True or False


