first = 0
second = 1
third = 2
fourth = 3
fith = 4

sixth = 1
seventh = 2
eighth = 3
nineth = 4
tenth = 5

maximum1 = 0
maximum2 = 0
point = 0
filename = "/Users/hunter/GitRepos/Python Stuff/Project Euler/numbers.txt"
with open(filename) as f:
	    lines = f.read()
	    numbers = list(lines)
#maximum = int(numbers[first]) * int(numbers[second]) * int(numbers[third]) * int(numbers[fourth]) * int(numbers[fith])



#print
while point < 1000:
	maximum1 = int(numbers[first]) * int(numbers[second]) * int(numbers[third]) * int(numbers[fourth]) * int(numbers[fith])
	maximum2 = int(numbers[sixth]) * int(numbers[seventh]) * int(numbers[eighth]) * int(numbers[nineth]) * int(numbers[tenth])
	if maximum1 > maximum2:
		sixth = sixth + 1
		seventh = seventh + 1
		eighth = eighth + 1
		nineth = nineth + 1
		tenth = tenth + 1
		point = point + 1
		print maximum1, maximum2
		print numbers[first], numbers[second], numbers[third], numbers[fourth], numbers[fith]
		print numbers[sixth], numbers[seventh], numbers[eighth], numbers[nineth], numbers[tenth]
		print
	else:
		maximum1 = maximum2
		first = sixth
		second = seventh
		third = eighth
		fourth = nineth
		fith = tenth
		
		sixth = sixth + 1
		seventh = seventh + 1
		eighth = eighth + 1
		nineth = nineth + 1
		tenth = tenth + 1
		point = point + 1
#print maximum1
