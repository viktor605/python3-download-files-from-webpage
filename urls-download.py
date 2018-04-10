#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen, urlretrieve

#url = "https://cs.brown.edu/~rt/gdhandbook/"
url = input()
resp = urllib.request.urlopen(url)
soup = BeautifulSoup(resp, "lxml", from_encoding=resp.info().get_param('charset'))
links = []
for link in soup.find_all('a', href=True):
    links.append(link.get('href'))
    
for elem in links:
    elem = '%s%s' % (url, elem)
    print(elem)
    destination = elem.rsplit('/',1)[1]
    urlretrieve(elem, destination)
