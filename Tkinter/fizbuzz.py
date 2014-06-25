x = 1
while x <= 100:
	if x % 3 == 0 and x % 5 == 0:
		print x, "FizzBuzz"
		x += 1
	elif x % 3 == 0:
		print x, "Fizz"
		x += 1
	elif x % 5 == 0:
		print x, "Buzz"
		x += 1
	else:
		print x
		x += 1