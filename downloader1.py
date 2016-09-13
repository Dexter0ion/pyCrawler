# coding:utf8

import urllib2
import cookielib

url = "http://www.baidu.com"

#Method 1
print "The first method"

response_1 = urllib2.urlopen(url)
print response_1.getcode() #200 means complete
print len(response_1.read())

#Method 2 - Request
print "The second method"

request = urllib2.Request(url)
request.add_header("DEXION","Mozilia/5.0") #pretend to be mozilia explorer
response_2 = urllib2.urlopen(request)
print response_2.getcode()
print len(response_2.read())

#Method3 - Cookielib-CookieJar??

print "The third method"

#Get cookie
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

response_3 = urllib2.urlopen(url)
print response_3.getcode()
print "_______________________________"
print cj
print "_______________________________"
print response_3.read()
