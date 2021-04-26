import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

houses = soup.find("div", attrs={"class":"wrap_tbl tbl_trade"}).find("tbody").find_all("tr")

for idx, house in enumerate(houses):
    print(f"============매물 {idx+1} ==========")
    house_type = house.find("td", attrs={"class":"col1"}).find("div", attrs={"class":"txt_ac"}).get_text().strip()
    area = house.find("td", attrs={"class":"col2"}).find("div", attrs={"class":"txt_ac"}).get_text().strip()
    price = house.find("td", attrs={"class":"col3"}).find("div", attrs={"class":"txt_ac"}).get_text().strip()
    posx = house.find("td", attrs={"class":"col4"}).find("div", attrs={"class":"txt_ac"}).get_text().strip()
    posy = house.find("td", attrs={"class":"col5"}).find("div", attrs={"class":"txt_ac"}).get_text().strip()
    print(f"거래 : {house_type}")
    print(f"면적 : {area}")
    print(f"가격 : {price}")
    print(f"동 : {posx}")
    print(f"층 : {posy}")
        
