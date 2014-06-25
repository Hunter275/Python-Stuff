a, b = 0, 1
numsum = 0
while len(list(str(b))) < 1001:
	if len(list(str(b))) == 1000:
		print len(list(str(b))), (numsum + 1)
		break
	a, b = b, a+b
	numsum = numsum + 1
