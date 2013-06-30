from datetime import datetime

now = datetime.now()

months = {1 : 0, 2 : 31, 3 : 59, 4 : 90, 5 : 120, 6 : 151, 7 : 181, 8 : 212, 9 : 243, 10 : 273, 11 : 304, 12 : 334}

date1 = months[now.month] + now.day
date1 = date1 - 1

# Jan 26, first full moon
date2 = date1-26

#print date2
#print (date2 / 29.4) * 10
date3 = (date2 / 29.4) * 10

if 58 >= date3 >= 60:
	print "D to O"
else:
	print "O to C"