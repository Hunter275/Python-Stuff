import urllib2
from bs4 import BeautifulSoup
import os

f = open("hackerheadlines.txt", "wb")

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.open('https://news.ycombinator.com/')
soup = BeautifulSoup(response)
table = soup("td", {'class' : 'title' })

point = 1
position = 1
while point <= len(table) - 1:
	if "Ask" in table[point].a.string.encode('utf-8'):
		os.system("aplay -q beep-07.wav")
	print table[point].a.string.encode('utf-8'), position
	f.write(table[point].a.string.encode('utf-8') + " " +  str(position) + "\n")
	point = point + 2
	position = position + 1

f.close