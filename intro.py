from datetime import datetime

now = datetime.now()

number = now.hour * now.minute / now.second + now.day
 
print number
#print number
# print "Here is a random number: " + number
# name = raw_input("What is your name? ")
# print "Greetings, " + name + " how are you feeling today?"