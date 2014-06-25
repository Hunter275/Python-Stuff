import urllib2
try:
    urllib2.urlopen('http://facebook.com')
except urllib2.HTTPError, e:
    print(e.code)
except urllib2.URLError, e:
    print(e.args)