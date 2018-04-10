#!/usr/bin/env python3

# http://qaru.site/questions/67250/retrieve-links-from-web-page-using-python-and-beautifulsoup
# urllib.request.urlopen user agent: https://stackoverflow.com/questions/24226781/changing-user-agent-in-python-3-for-urrlib-request-urlopen

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
    if 'http' not in elem:
        elem = '%s%s' % (url, elem)
    print(elem)
    destination = elem.rsplit('/',1)[1]
    urlretrieve(elem, destination)
