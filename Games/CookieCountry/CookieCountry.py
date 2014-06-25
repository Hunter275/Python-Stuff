#time for wait
import time

print """
================
Cookie Country!
================
"""
time.sleep(2)
print "You are King Cookie!"
time.sleep(2)
print ""
print "Your nemisis, King Rasin, is building an army!"
time.sleep(4)
print ""
print "Your duty as king is to defend your land!"
time.sleep(4)
print ""
print "Build your cookie army, and defend your lands!"
print ""
time.sleep(4)
stoves = 1
cookies = 1
stovesph = 1 
x = 1
while x > 0:
	print """













====================================
=                                  =
=                                  =
=  S                               =
====================================
	"""
	if stoves < 10:
		print "* Stoves: ",stoves, "                      *"
	else:
		print "* Stoves: ",stoves, "                     *"

	if cookies < 10:
		print "* Cookies: ",cookies, "                      *"
	else:
		print "* Cookies: ",cookies, "                     *"
	print "* Cookies Per Hour:",stovesph,"              *"          
	print """
*                                  *
************************************
	"""
	time.sleep(1)
	cookies += 1
	x+=1