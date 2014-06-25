point = 0
numsum = 0
filename = "/Users/hunter/GitRepos/Python Stuff/Project Euler/Problem13numbers.txt"
with open(filename) as f:
	    lines = f.read().splitlines()
while point <= 99:
	numsum = numsum + int(lines[point])
	point = point + 1
print str(numsum)[0:10]
