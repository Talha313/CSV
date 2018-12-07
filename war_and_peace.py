from  urllib.request import urlopen
from  urllib.error import HTTPError
from bs4 import BeautifulSoup
from  urllib.error import URLError

try:
    html=urlopen("http://pythonscraping.com/pages/warandpeace.html")
except HTTPError as  e:
    print("page not found")
except URLError as e:
    print("server not found")
try:
    bs=BeautifulSoup(html,'lxml')
    nameList=bs.findAll("span", {"class":"green"})
    for name in nameList:
        print(name.get_text())

    # namelist=bs.findAll({"h1","h2", "h3"})
    # for name in namelist:
    #     print(name.get_text())

    # nameList=bs.findAll(text="by")
    #
    # print (len(nameList))
except AttributeError as e:
    print("door ja")

