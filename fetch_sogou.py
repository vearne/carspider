import requests
import lxml
from lxml import etree
from StringIO import StringIO

s = requests.Session()
res = s.get('http://weixin.sogou.com/')
s.get('http://pb.sogou.com/pv.gif?uigs_productid=weixin&type=article&status=fail')
res = s.get('http://weixin.sogou.com/weixin?query=%E7%8B%97&fr=sgsearch&type=2&ie=utf8&w=01019900&sut=4106&sst0=1442414258174&lkt=0%2C0%2C0')
#print res.content
parser = etree.HTMLParser()
tree   = etree.parse(StringIO(res.text), parser)
item_list = tree.xpath('//div[@class="txt-box"]/h4/a')
t = item_list[0]
url = 'http://weixin.sogou.com' + t.get('href')
print url
#print url
#t = 'http://weixin.sogou.com/websearch/art.jsp?sg=CBf80b2xkgZiCvGZw_mTR87iG5A9zFN35Wp4jMrUxT-ZKGhd40ot9XWjxq3PYgNjBGqWHSZmr05-KubC2CPgmwYTEtRD7sV1nLHfCQrCQoQ.&url=p0OVDH8R4SHyUySb8E88hkJm8GF_McJfBfynRTbN8wgk1nN-Q6sVbddAdC73n1A4IKUX_KcUigeP5f7Ol_3v9VLvkvBrfA0s6cJ4YJLhKmJoeweX8uAukDD9iBvIC3qlqIPPCPkKnIhYy-5x5In7jJFmExjqCxhpkyjFvwP6PuGcQ64lGQ2ZDMuqxplQrsbk'

res = s.get(url)
print res.content



