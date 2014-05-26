import urllib2
import time
addr='http://store.apple.com/hk/browse/home/shop_iphone/family/iphone'
while (1==1):
	time.sleep(10)
	response = urllib2.urlopen(addr)
	html = response.read()
	x=html.find("Unavailable")
	if (x<0):
		print 'Selling IPhone4'
	else:
		print 'No Iphone Sells Orz'
