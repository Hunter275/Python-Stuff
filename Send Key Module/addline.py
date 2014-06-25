##########################################
# AfterLine 							 #
# Created by Hunter Thornsberry			 #
# hunter@hunterthornsberry.com			 #
# Free to edit, distrubute, use. 		 #
##########################################


def afterline(filename, line, text): #file is a reserved word
	with open(filename) as f:
	    lines = f.read().splitlines()
	lines.insert(line, text)

	point = 0
	while point < len(lines):
		lines[point] = lines[point] + "\n"
		point = point + 1

	with open('index.html', 'w') as file:
	    file.writelines( lines )