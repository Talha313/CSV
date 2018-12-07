from urllib.request import urlopen
from bs4 import BeautifulSoup
import  re
pages=set()
def  getlinks(pageUrl):
     global pages
     html=urlopen("http://en.wikipedia.org"+pageUrl)
     bs=BeautifulSoup(html,'lxml')
     for link in bs.findAll("a", href=re.compile("^(/wiki/)")):
         if (link.attrs['href'] not in pages):
             newPage=link.attrs['href']
             print(newPage)
             pages.add(newPage)
             getlinks(newPage)
getlinks("")
