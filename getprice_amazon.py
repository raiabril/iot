from bs4 import BeautifulSoup
from urllib2 import Request, urlopen
import decimal
userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
url = "https://www.amazon.es/dp/B00K4V9QW8"
req = Request(url, None, {'User-Agent':userAgent})
html = urlopen(req).read()
soup = BeautifulSoup(html, "lxml")
price = soup.find(id='priceblock_ourprice')
print(price.text.split(' ')[1])
title = soup.find(id='productTitle')
title.text.strip()


from bs4 import BeautifulSoup
from urllib2 import Request, urlopen
import decimal
userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
url =“https://www.amazon.es/s/ref=nb_sb_ss_c_2_12?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords=discos+duros+externos&sprefix=discos+duros%2Ccomputers%2C200&crid=1WZ6WHY6BMZ65”
req = Request(url, None, {'User-Agent':userAgent})
html = urlopen(req).read()
soup = BeautifulSoup(html, "lxml")