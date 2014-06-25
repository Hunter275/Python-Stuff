a, b = 0, 1
numsum = 0
while b < 4000000:
	if b % 2 == 0:
		numsum = b + numsum
	a, b = b, a+b
print numsum
