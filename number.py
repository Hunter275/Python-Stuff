x = 1000
filename = "test2"
target = open(filename, 'w')

while x < 9999:
	print x
	target.write(str(x) + '\n')
	x += 1 

target.close()