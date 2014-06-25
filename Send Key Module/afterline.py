##########################################
# AfterLine 							 #
# Created by Hunter Thornsberry			 #
# hunter@hunterthornsberry.com			 #
# Free to edit, distrubute, use. 		 #
##########################################
import sys

def afterline(filename, line, text): #file is a reserved word
	try:
		with open(filename) as f:
		    lines = f.read().splitlines()
		lines.insert(line, text)
	except (TypeError):
			print "AfterLine Usage: afterline.afterline('filename', line, 'text')"

	if line > len(lines):
		sys.exit("Failed: Line # too large, last line is " + str(len(lines)) )

	point = 0
	while point < len(lines):
			lines[point] = lines[point] + "\n"
			point = point + 1

	with open(filename, 'w') as file:
	    file.writelines( lines )