number = 100
point = 1
numsum = 1
while point < number:
	numsum = numsum * number
	number = number - 1
listnum = list(str(numsum))

xpoint = 0
xsum = 0
while xpoint < len(listnum):
	xsum = xsum + int(listnum[xpoint])
	xpoint = xpoint + 1
print xsum