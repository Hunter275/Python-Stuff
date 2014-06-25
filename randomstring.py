import random
import string
letterdic = string.ascii_lowercase
point = 0
#print random.randint(1,26)
x = letterdic[random.randint(0,25)] + letterdic[random.randint(0,25)] + letterdic[random.randint(0,25)] + letterdic[random.randint(0,25)]
point1 = 0
point2 = 0
point3 = 0
point4 = 0
while point4 <= 25:
	print letterdic[point4]
	point4 = point4 + 1