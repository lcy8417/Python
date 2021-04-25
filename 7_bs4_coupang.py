import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[1].find("div", attrs={"class":"name"}).get_text())
for item in items:

    # 추가 할인 쿠폰은 제외
    ad_badge = item.find("span", attrs={"class":"badge badge-benefit"})
    if ad_badge:
        print(" <추가 할인 쿠폰은 제외>")
        continue
    
    name = item.find("div", attrs={"class":"name"}).get_text()

    # 애플 제품 제외
    if "Apple" in name:
        print("     <Apple 상품 제외합니다>")
        continue

    price =  item.find("strong", attrs={"class":"price-value"}).get_text()
    # 리뷰 100개 이상, 평점은 4.5 이상 되는 것만 조회
    rating =  item.find("em", attrs={"class":"rating"}) # 평점
    if rating:
        rating = rating.get_text()
    else:
        rating = "평점 없음"
        print(" < 평점 없는 상품 제외>")
        continue
    
    total_rating =  item.find("span", attrs={"class":"rating-total-count"})
    if total_rating:
        total_rating = total_rating.get_text()
        total_rating = total_rating[1:-1]
    else:
        total_rating = "평점 수 없음"
        print(" < 평점수 없는 상품 제외>")
        continue

    if float(rating) >= 4.5 and int(total_rating) >= 100:
        print(name, price, rating, total_rating)
    