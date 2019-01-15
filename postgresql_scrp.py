import psycopg2
#from config import config
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
    """ create tables in the PostgreSQL database"""
    try:

        commands = (
            """
                CREATE TABLE  IF NOT EXISTS products (
                product VARCHAR (255),
                img  VARCHAR (255),
                brand  VARCHAR (150),
                title  VARCHAR (150),
                active VARCHAR (150),
                original VARCHAR (150)
                )
            """)
        cur=conn.cursor()
        cur.execute(commands)

    except:
        print("No table created")
    finally:
        cur.close()

    cur=conn.cursor()
    cur.execute(commands)

def insert(conn, values):

        """ insert a new vendor into the vendors table """
        query = """INSERT INTO products(product, img, brand, title, active, original)
             VALUES(%s, %s, %s, %s, %s, %s);"""
        cur=conn.cursor()
        cur.execute(query, values)
        conn.commit()
def select(conn):
    cur=conn.cursor()
    query="SELECT * FROM products "
    cur.execute(query)
    print("The number of parts: ", cur.rowcount)
    for i in cur:
        print(i)
    cur.close()
def update(conn, values):
    """ update vendor name based on the vendor id """
    try:
        query = """ UPDATE products
                    SET brand = %s,
                    title = %s
                    WHERE product = %s"""
        cur = conn.cursor()
        cur.execute(query, values)
        conn.commit()
        updated_rows = cur.rowcount
        print(updated_rows)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cur.close()



def main():
    url = ("https://www.sotostore.com/en/6/footwear?orderBy=Published")
    getCntent(url)
    conn = psycopg2.connect(host="localhost",database="pythondb", user="talha", password="a")
    #create_table(conn)
    # for item in item_list:
    #    values = (item['product_page'], item['img'], item['brand'], item['title'], item['active_price'], item['original_price'])
    #    insert(conn, values)
    product1 = 'https://www.sotostore.com/en/product/17346/mx608wt'
    update(conn,('TALHA', 'JACKET', product1))
    select(conn)
    print(conn)
    conn.close()
    print(conn)
if __name__ == "__main__":
    main()

