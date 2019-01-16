import requests
from bs4 import  BeautifulSoup
import  re
import  random
session_requests = requests.session()

desktop_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

def random_headers():
    return {'User-Agent': random.choice(desktop_agents)}


def getCntent():
    url="https://www.sneakersnstuff.com/en/product/34525/adidas-stan-smith"
    append_url = "https://www.sneakersnstuff.com"
    try:
        result = session_requests.get(url, headers=random_headers())
        print(result.ok, result.status_code)
        if (result.ok and result.status_code == 200):
            soup = BeautifulSoup(result.text, 'lxml')
            # print(soup.prettify())
            right_column = soup.find("div", attrs={"id" : "right-column" })
            product_name = right_column.find("h1" , attrs= {"id":"product-name"}).text
            price = right_column.find("span", attrs={"class" : "price"}).text
            sizes = right_column.find_all("div", attrs = {"class" : "size-button"})
            size_list =[]
            for s in sizes:
                size = str(s.find("span", attrs={"class": "size-type"}).text).strip()
                if size not  in size_list:
                    size_list.append(size)

            image = append_url + soup.find("img", attrs={"id": "primary-image"})["src"]
            print(product_name)
            print(price)
            print(size_list)
            print(image)



    except Exception as e:
        print(e)

if __name__ == '__main__':
    getCntent()