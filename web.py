from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://pythonscraping.com/pages/page1.html")
bsobj=BeautifulSoup(html.read(),'lxml')
print(bsobj.prettify)
print(bsobj.nonExistingTag.someTag)





# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html=urlopen("http://facebook.com")
# bsobj=BeautifulSoup(html.read(),'lxml')
# print(bsobj.h1)