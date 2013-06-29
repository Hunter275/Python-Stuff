from datetime import datetime

now = datetime.now()

if now.minute <= 9:
    print str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour) + ":" + "0" + str(now.minute) + ":" + str(now.second)
else:
    print str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)