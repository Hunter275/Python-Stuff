#list contains 5162 names
namepoint = 0	
mastersum = 0
while namepoint <= 5162:
	readfile = open("/Users/hunter/Desktop/names.txt", "r")
	names = readfile.read()
	rawname = names.split(",")
	rawnames = names.strip('"')
	lenrawname = len(rawname[namepoint]) - 1
	name = rawname[namepoint][1:lenrawname]
	name = name.lower()
	letterdic = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10, "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26}
	maximum = len(list(name)) - 1
	point = 0
	nameletters = list(name)
	numsum = 0
	while point <= maximum:
		#print nameletters[point]
		#print letterdic[nameletters[point]]
		numsum = numsum + (letterdic[nameletters[point]] * namepoint)
		point = point + 1
	print rawname[namepoint][1:lenrawname] + " " + str(numsum) + " " + str(namepoint)
	namepoint = namepoint + 1
	mastersum = mastersum + numsum
print mastersum + 57
