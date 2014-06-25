power = 2 ** 1000
point = 0
numsum = 0
numlist = list(str(power))
while point <= 301:
	numsum = numsum + int(numlist[point])
	point = point + 1
print numsum