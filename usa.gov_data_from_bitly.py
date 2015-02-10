
	
#%%

import json
import urllib2

linkx = urllib2.urlopen('http://developer.usa.gov/1usagov')


fp = open('bitly.txt', 'r')
bitlyx = fp.readlines()

jslink = []
for line in bitlyx:
	jslink.append(json.loads(line))
	
	