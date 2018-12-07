from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError
from urllib.error import HTTPError
import re

page=set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bs = BeautifulSoup(html, 'lxml')
    for link in bs.findAll("a", href=re.compile("^(/wiki/)")):
        if (link.attrs['href'] not in pages):
            newPage = link.attrs['href']
            print(newPage)
            pages.add(newPage)
            getLinks(newPage)


getLinks("")

