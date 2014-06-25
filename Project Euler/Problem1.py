numsum = 0
number = 1
problemnum = 1
while problemnum < 1000:
	if number % 3 == 0 or number % 5 == 0:
		print number + numsum
		numsum = numsum + number
		problemnum = problemnum + 1
		number = number + 1
	else:
		problemnum = problemnum + 1
		number = number + 1