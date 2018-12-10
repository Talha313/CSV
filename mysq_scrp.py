import pymysql
import requests
from bs4 import BeautifulSoup

item_list=[]
def getCntent(url):
  url = ("https://www.sotostore.com/en/6/footwear?orderBy=Published")
  response = requests.get(url)
  html = response.content
  soup = BeautifulSoup(html, "html.parser")
  main_cards = soup.find_all("div", attrs={"class": "card"})
  link = "https://www.sotostore.com"
  for card in main_cards:
    # print(card.prettify())
    product_page1 = card.find("a", {"class": "card-image-link"})['href']
    product_page = link + product_page1
    img1 = link + card.find("img", attrs={"class": "card-img"})['data-src']
    h4_brand = str(card.find("h4", attrs={"class": "card-brand"}).text)
    h4_title = str(card.find("h4", attrs={"class": "card-title"}).text)
    active_price = str(card.find("span", attrs={"class": "active-price"}).text)
    original_price = str(card.find("del", attrs={"class": "original-price"}).text)

    # img = card.find("img", src=re.compile("^(/images/)"))
    # img1=img_link+img.get('src')
    item_dic = {}
    item_dic['product_page'] = product_page
    item_dic['img'] = img1
    item_dic['brand'] = h4_brand.strip()
    item_dic['title'] = h4_title.strip()
    item_dic['active_price'] = active_price.strip()
    item_dic['original_price'] = original_price.strip()
    if item_dic not in item_list:
      item_list.append(item_dic)
    # print(item_dic)

def create_table(conn):

  cur = conn.cursor()

  cur.execute("CREATE TABLE  products (product VARCHAR(255),img VARCHAR(255),brand VARCHAR(255),title VARCHAR(150),active VARCHAR (150),original VARCHAR(150))");
  cur.execute("SHOW TABLES")
  cur.close()
def insert_into_table(conn, values):
  try:
    cur=conn.cursor()
    query = "INSERT INTO products (product, img, brand, title, active,original) VALUES (%s, %s, %s, %s, %s, %s)"
    cur.execute(query, values)
    conn.commit()
    print(cur.rowcount, "record inserted.")
  except:
    print("Not inserted")
  finally:
    cur.close()
  #cur.close()
def select(conn):
  cur=conn.cursor()
  cur.execute("SELECT * FROM products")
  for x in cur:
    print(x)

def update(conn,new_values):
  try:
    cur=conn.cursor()
    query = "UPDATE products SET brand = %s, title=%s  WHERE product = %s"
    cur.execute(query,new_values)
    conn.commit()
    print(cur.rowcount, "record(s) affected")
  except:
    print("not updated")
  finally:
    cur.close()

def main():
  try:
    url = ("https://www.sotostore.com/en/6/footwear?orderBy=Published")
    getCntent(url)
    conn = pymysql.connect(host='127.0.0.1', user='talha', passwd='a', db='pythondb')
    #create_table(conn)
  # for item in item_list:
  #   values = (item['product_page'], item['img'], item['brand'], item['title'], item['active_price'], item['original_price'])
#     insert_into_table(conn, values)
    #select(conn)
    product1='https://www.sotostore.com/en/product/17299/react-element-55'
    update(conn, ('GulAhmad','Jacket',product1))
    select(conn)
  except:
    print("Error in main")
  finally:
    conn.close()

if __name__ =="__main__":
   main()
