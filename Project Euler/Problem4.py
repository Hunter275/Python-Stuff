test1 = 999
test2 = 999
result = test1 * test2
firsthalf = len(str(result)) / 2
strresult = str(result)
first = strresult[0:firsthalf]
secondhalf = strresult[firsthalf:]
second = secondhalf[::-1]

while test2 >= 100:
	result = test1 * test2
	firsthalf = len(str(result)) / 2
	strresult = str(result)
	first = strresult[0:(firsthalf)]
	secondhalf = strresult[firsthalf:]
	second = secondhalf[::-1]


	if first == second:
		print "***HIT Result:",result, test1, test2, "HIT***"
		#break

	elif test2 == 100:
		#print "Result:",result, test1, test2, "Miss"
		test1 = test1 - 1
		test2 = test1

	else:
		#print "Result:",result, first, second, "Miss", test1, "*", test2
		test2 = test2 - 1