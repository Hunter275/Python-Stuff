import urllib2

number = raw_input("One(1) or Two(2)? ")

if number == "1":
	for line in urllib2.urlopen("https://gist.github.com/Hunter275/5900281/raw/5017767febb968ede36fa6cc2c17e436de3f83db/gistfile1.txt"):
  	  	print line
  	  
elif number == "2":
	for line in urllib2.urlopen("https://gist.github.com/Hunter275/5900324/raw/5073010b52bee56b811ebbed259c555fde07c428/gistfile1.txt"):
		print line
		
else:
	print "Please use numrical number 1 or 2"