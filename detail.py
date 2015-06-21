# -*- coding: utf-8 -*-
import json
from lxml import etree
from StringIO import StringIO
import requests
#from pyspider.fetcher import Fetcher
from tornado_fetcher import Fetcher

class Car(object):
	def __init__(self):
		self.type_id = '' 
		self.name = ''
		self.guide_price =''
		self.lowest_price = ''
		self.manufacturer = ''
		self.level = ''
		self.engine = ''
		self.gearbox = ''
		self.size = ''
		self.struct = ''
		self.top_speed = ''
		self.acc = ''
		self.fuel_consumption = ''
	def __unicode__(self):
		ll = []
		ll.append(str(self.type_id))
		ll.append(self.name)
		ll.append(self.guide_price)
		ll.append(self.lowest_price)
		ll.append(self.manufacturer)
		ll.append(self.level)
		ll.append(self.engine)
		ll.append(self.gearbox)
		ll.append(self.size)
		ll.append(self.struct)
		ll.append(self.top_speed)
		ll.append(self.acc)
		ll.append(self.fuel_consumption)
		return ','.join(ll)

def get_param(id):
	url = "http://car.autohome.com.cn/config/series/%s.html" % (id)
	car_list = []
        print url
 	fetcher = Fetcher(
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36',
		phantomjs_proxy = 'http://localhost:9999',	
    		)	
	
	t = fetcher.phantomjs_fetch(url)	
		
	#print t['content'].encode('utf-8')
        parser = etree.HTMLParser()
        tree   = etree.parse(StringIO(t['content']), parser)
	
	# ---------------name -------------------
        item_list = tree.xpath('//div[@class="carbox"]/div/a/text()')
	print 'name', len(item_list)
	if len(item_list) <= 0:
		return []

	for item in item_list:
		car = Car()
		car.type_id = id
		car.name = item
		car_list.append(car)
	
	# -----------------guide price--------------------
        item_list = tree.xpath('//tr[@id="tr_2000"]/td/div/text()')
        print 'guide_price', len(item_list)
	i = 0
	for i in xrange(len(item_list)):
		car_list[i].guide_price = item_list[i]	
	
	# -----------------lowest price--------------------
        item_list = tree.xpath('//tr[@id="tr_2001"]/td/div/a/text()')
        print 'lowest_price', len(item_list)
	i = 0
	for i in xrange(len(item_list)):
		car_list[i].lowest_price = item_list[i]	
	
	# ----------------manufacturer---------------------
        item_list = tree.xpath('//tr[@id="tr_0"]/td/div/text()')
        print 'manufacturer', len(item_list)
	i = 0
	for i in xrange(len(item_list)):
		car_list[i].manufacturer= item_list[i]	
	
	# ----------------level---------------------
        item_list = tree.xpath('//tr[@id="tr_1"]/td/div/text()')
        print 'level', len(item_list)
	i = 0
	for i in xrange(len(item_list)):
		car_list[i].level = item_list[i]	

	# ----------------engine---------------------
        item_list = tree.xpath('//tr[@id="tr_2"]/td/div/text()')
        print 'engine', len(item_list)
	i = 0
	for i in xrange(len(item_list)):
		car_list[i].engine = item_list[i]	

	# ----------------gearbox---------------------
        item_list = tree.xpath('//tr[@id="tr_3"]/td/div/text()')
        print 'gearbox', len(item_list)
	i = 0
	for i in xrange(len(item_list)):
		car_list[i].gearbox = item_list[i]	

	# ----------------size---------------------
        item_list = tree.xpath('//tr[@id="tr_4"]/td/div/text()')
        print 'size', len(item_list)
	i = 0
	for i in xrange(len(item_list)):
		car_list[i].size = item_list[i]	

	# ----------------struct---------------------
        item_list = tree.xpath('//tr[@id="tr_5"]/td/div/text()')
        print 'struct', len(item_list)
	i = 0
	for i in xrange(len(item_list)):
		car_list[i].struct= item_list[i]	
	
	
	# ----------------top_speed---------------------
        item_list = tree.xpath('//tr[@id="tr_6"]/td/div/text()')
        print 'top_speed', len(item_list)
	i = 0
	for i in xrange(len(item_list)):
		car_list[i].top_speed = item_list[i]	

	
	# ----------------acc---------------------
        item_list = tree.xpath('//tr[@id="tr_7"]/td/div/text()')
        print 'acc', len(item_list)
	i = 0
	for i in xrange(len(item_list)):
		car_list[i].acc = item_list[i]	

	
	# --------------- fuel_consumption ----------------------
        item_list = tree.xpath('//tr[@id="tr_11"]/td/div/text()')
        print 'fuel_consumption', len(item_list)
	i = 0
	for i in xrange(len(item_list)):
		car_list[i].fuel_consumption = item_list[i]	

	return car_list


if __name__ == "__main__":
	id = 812 
	id_list = []	
	with open('./id_list.txt') as fp:
		for line in fp:
			id_list.append(int(line))
	print 'len(id_list)', len(id_list)
	
	# target_csv	
	fp = open("./car.csv", 'w')
	for id in id_list:	
		car_list = get_param(id)
		for car in car_list:
			fp.write(unicode(car).encode('utf-8'))
			fp.write('\n')


	fp.close()


