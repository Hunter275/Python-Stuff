from bs4 import BeautifulSoup
import urllib2

req = urllib2.Request("http://adventuresintechland.com/a-web-scraper-that-doesnt-completly-suck/")
response = urllib2.urlopen(req)
the_page = response.read()
soup = BeautifulSoup(the_page)
text = soup.findAll("html")

print text[0].text