from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("cars.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

def car_func(selector):
    print("car_func", soup.select_one(selector).string)

car_lambda = lambda q : print("car_lambda", soup.select_one(q).string)

car_func("#gr")
car_func("li#gr")
car_func("#ge")
car_func("ul > li#gr")
car_func("#cars li:nth-of-type(2)")
car_func("li[id='gr']")

car_lambda("#gr")
car_lambda("li#gr")
car_lambda("#ge")
car_lambda("ul > li#gr")
car_lambda("#cars li:nth-of-type(2)")
car_lambda("li[id='gr']")

# print(soup.select("li")[3].string)
# print(soup.find_all("li")[3].string)