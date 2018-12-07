from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getContent(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        print("page no found")
    except URLError as e:
        print("server not found")
    try:
        bsobj=BeautifulSoup(html,'lxml')
        print(bsobj)
        head=bsobj.h1
        return  head
    except AttributeError as e:
        print("error in bs")
h=getContent("http://pythonscraping.com/pages/page1.html")
if (h==None):
    print("nothing found")
else:
    print(h)






