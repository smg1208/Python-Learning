import urllib
import collections
from collections import Counter
from collections import OrderedDict
from collections import deque
from collections import namedtuple

import time
import requests
import json
import selenium
import io
import re
import urllib.request
import urllib.parse
import bs4


x = urllib.request.urlopen('https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645.html')
read = bs4.BeautifulSoup(x, 'lxml')
read1 = read.select('.chitietketqua_title')
for i in read1:
    print((i.find('h5').findAll('b')))

# print(read1.find('h5'))
# # Making a GET request
# r = requests.get('https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645.html')
# print(r.text)

