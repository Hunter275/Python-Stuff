#list contains 5162 names
namepoint = 0
mastersum = 0
filename = "/Users/hunter/Desktop/names2.txt"
while namepoint <= 5162:
	with open(filename) as f:
	    lines = f.read().splitlines()
	#print lines[0]
	letterdic = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26}
	nameletters = list(lines[namepoint].lower())
	#print nameletters
	maximum = len(nameletters) - 1
	point = 0
	numsum = 0
	while point <= maximum:
		#print nameletters[point]
		#print nameletters[point] + str(letterdic[nameletters[point]])
		numsum = numsum + ((letterdic[nameletters[point]]) * (namepoint + 1))
		point = point + 1
		#print
	print lines[namepoint] + " " + str(namepoint + 1) + " " + str(numsum)
	namepoint = namepoint + 1
	mastersum = mastersum + numsum
print mastersum