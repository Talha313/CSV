import requests
from bs4 import  BeautifulSoup
import  re
item_list=[]
import sqlite3
from sqlite3 import Error

def getCntent(url):
    url=("https://www.sotostore.com/en/6/footwear?orderBy=Published")
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    main_cards=soup.find_all("div", attrs={"class":"card"})
    link="https://www.sotostore.com"
    for card in main_cards:
        #print(card.prettify())
        product_page1=card.find("a", {"class":"card-image-link"})['href']
        product_page=link+product_page1
        img1 = link+ card.find("img", attrs={"class":"card-img"})['data-src']
        h4_brand=str(card.find("h4",attrs={"class": "card-brand"}).text)
        h4_title = str(card.find("h4", attrs={"class": "card-title"}).text)
        active_price=str(card.find("span", attrs={"class":"active-price"}).text)
        original_price=str(card.find("del", attrs={"class":"original-price"}).text)

# img = card.find("img", src=re.compile("^(/images/)"))
# img1=img_link+img.get('src')
        item_dic={}
        item_dic['product_page'] = product_page
        item_dic['img']=img1
        item_dic['brand']=h4_brand.strip()
        item_dic['title']=h4_title.strip()
        item_dic['active_price']=active_price.strip()
        item_dic['original_price']=original_price.strip()
        if item_dic not in item_list:
             item_list.append(item_dic)
        #print(item_dic)
def write(list):
     with open('store.csv', mode='w') as f:
        csv_liner = "ProductPage,Image,Brand,Title,ActivePrice,OriginalPrice\n"
        f.write(csv_liner)
        for i in list:
            csv_var = i['product_page']+","+i['img'] + "," + i['brand'] + "," + i['title'] +","+ i['active_price'] + "," + i['original_price'] +"\n"
            f.write(csv_var)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
     """ create a table from the create_table_sql statement
     :param conn: Connection object
     :param create_table_sql: a CREATE TABLE statement
     :return:
     """
     try:
         c = conn.cursor()
         c.execute(create_table_sql)
     except Error as e:
         print(e)

def insert_product(conn, project):
    """

    """
    sql = ''' INSERT INTO products(product,image,brand,title,active_price,orginal_price)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    #return cur.lastrowid

def update_products(conn, new_values):
    sql = ''' UPDATE products
                  SET brand = ? ,
                      title = ?  
                  WHERE product = ?'''
    cur = conn.cursor()
    cur.execute(sql, new_values)


def select_data_from_db(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM products ")

    rows = cur.fetchall()
    cur.close()
    for row in rows:
        print(row)

if __name__ == "__main__":
    url = ("https://www.sotostore.com/en/6/footwear?orderBy=Published")
    getCntent(url)
   # print(item_list)
    #write(item_list)

    sql_create_products_table = """ CREATE TABLE IF NOT EXISTS products (
                                           product text,
                                           image text,
                                           brand text,
                                           title text,
                                           active_price text,
                                           orginal_price text
                                       ); """
    database='my_store.db'
    try:
    # Create connection function called
        conn = create_connection(database)
#Table creation function called

        if conn is not None:
            create_table(conn, sql_create_products_table)
        else:
            print("Error! Can not create Connection")

    # insertion function called
    #     for item in item_list:
    #          with conn:
    #             product = (item['product_page'], item['img'], item['brand'],item['title'],item['active_price'],item['original_price'])
    #             insert_product(conn, product)
    #print(item_list)
        new_url = 'https://www.sotostore.com/en/product/17347/wx608wt'
        try:

            with conn:
                update_products(conn,('GulAhmad','Jackets',new_url))

        except:
            print("Error in Updation")

        select_data_from_db(conn)

    except:
        print("Invalid opertions detected")
    finally:
        conn.close()