from datetime import datetime

now = datetime.now()

if now.month == 2:
	date1 = 31 + now.day

if now.month == 3:
	date1 = 59 + now.day
	
if now.month == 4:
	date1 = 90 + now.day
	
if now.month == 5:
	date1 = 120 + now.day
	
if now.month == 6:
	date1 = 151 + now.day

if now.month == 7:
	date1 = 181 + now.day
	
if now.month == 8:
	date1 = 212 + now.day
	
if now.month == 9:
	date1 = 243 + now.day
	
if now.month == 10:
	date1 = 273 + now.day
	
if now.month == 11:
	date1 = 304 + now.day
	
if now.month == 12:
	date1 = 334 + now.day
	

date1 = date1 - 1

# Jan 26, first full moon
date2 = date1-26

print date2
print (date2 / 29.4) * 10
date3 = (date2 / 29.4) * 10

if 58 >= date3 >= 60:
	print "D to O"
else:
	print "O to C"