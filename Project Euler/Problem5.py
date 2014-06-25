number = 2
maximum = 20
test = 3
def isOdd(number):
	if number % 2 != 0:
		return True
	else:
		return False


while number <= maximum:
	if isOdd(test) == True:
		test = test + 1
		#print test
	elif test % number == 0:
		#print "Win " + str(test) + " / " + str(number)
		number = number + 1
		if number == 20:
			print test
	elif test < 900000000:
		#print "Lose " + str(test) + " / " + str(number)
		number = 2
		test = test + 1
	else:
		print "Broken"
		break