from urllib.request import urlopen
from bs4 import BeautifulSoup
import  re

html=urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon",'lxml')
bs=BeautifulSoup("a")
for link in bs.findAll("div",{"id":"bodyContent "}).findAll("a",href=re.compile()):
