from urllib.request import urlopen
from bs4 import BeautifulSoup
import  re

html=urlopen("http://pythonscraping.com/pages/page3.html")
bs=BeautifulSoup(html, 'lxml')
image=bs.findAll("img",re.compile({"src":"\.\.\/img\/gifts\/img.*\jpg"}) )
for i in image:
    print(i["src"])