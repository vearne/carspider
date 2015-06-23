# -*- coding: utf-8 -*-
import json
from lxml import etree
from StringIO import StringIO
import requests
from tornado_fetcher import Fetcher

url_list = []
with open('url.txt') as fp:
	for line in fp:
		url_list.append(line)	

#url_list = ['http://www.autohome.com.cn/2805/#levelsource=000000000_0&pvareaid=101594', 'http://www.autohome.com.cn/19/#levelsource=000000000_0&pvareaid=101594']
#res_list = []
fp = open('./config_url.txt', 'w')
for url in url_list:
	print url
	t = requests.get(url) 
	parser = etree.HTMLParser()
        tree   = etree.parse(StringIO(t.text), parser)
        x = tree.xpath('//li[@class="nav-item current"]')
	if x:
		target = x[0]
		target = target.getnext()	
		#res_list.append(target.getchildren()[0].get("href"))
		url = target.getchildren()[0].get("href")
		if url is None:
			continue
		print type(url)
		fp.write(url)
		fp.write('\n')

        x = tree.xpath('//div[@class="models_nav"]/a[2]')
	#print type(x)
	for item in x:
		url = 'http://www.autohome.com.cn/' + item.get("href")	
		print type(url)
		fp.write(url)
		fp.write('\n')
	fp.flush()

fp.close()


