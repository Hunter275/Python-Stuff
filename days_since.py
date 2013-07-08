from datetime import datetime

now = datetime.now()

months = {1 : 0, 2 : 31, 3 : 59, 4 : 90, 5 : 120, 6 : 151, 7 : 181, 8 : 212, 9 : 243, 10 : 273, 11 : 304, 12 : 334}

date = raw_input("What is your birthday? (mm/dd/yyyy) ")

month = int(date[:2])
day = date[3:5]
year = date[6:]

days = ((now.year - int(year)) * 365) + int(months[month]) - int(day)

print now.year
print date
print days

