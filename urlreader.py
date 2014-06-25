import urllib2
from bs4 import BeautifulSoup
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.open('https://news.ycombinator.com/')
soup = BeautifulSoup(response)
table = soup("td", {'class' : 'title' })
#print table[3].a.string.encode('utf-8')

point = 1
while point <= len(table) - 1:
	print table[point].a.string.encode('utf-8')
	point = point + 2