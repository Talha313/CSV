from urllib.request import urlopen
from bs4 import BeautifulSoup
from  urllib.error import URLError
try:
    html=urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
except URLError as e:
    print("server erre")

bs=BeautifulSoup(html,'lxml')
for link in bs.findAll("a"):
    if('href' in link.attrs):
        print(link.attrs['href'])

