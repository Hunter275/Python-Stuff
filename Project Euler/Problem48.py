point = 0
numsum = 0
while point <= 1000:
	numsum = numsum + (point ** point)
	point = point + 1
print str(numsum-1)[((len(str(numsum)) - 10)):len(str(numsum))]
print numsum - 1