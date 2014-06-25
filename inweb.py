term = "Tanner"
search = "Hunter Tanner Connor Sam"
term = list(term)
search = list(search)

point1 = 0
point2 = 0
while point2 < len(search):
	if term[point1] == search[point2]:
		point1 = point1 + 1
		point2 = point2 + 1
		if point1 == len(term):
			print "Yes"
	else:
		point2 = point2 + 1
		if point1 == len(term):
			print "No"
		else:
			print "No"
			break
