point = 1
number = 100
numsum = 0
while point <= number:
	numsum = numsum + point
	point = point + 1
power = numsum * numsum

point2 = 1
numsum2 = 0
while point2 <= number:
	numsum2 = numsum2 + (point2*point2)
	point2 = point2 + 1
power2 = numsum2

print power
print power2
print power - power2