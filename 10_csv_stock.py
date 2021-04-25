import csv
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # 엑셀에서 한글 깨지면 인코딩 이렇게
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
writer.writerow(title)

for i in range(1, 5):
    url = f"https://finance.naver.com/sise/sise_market_sum.nhn?&page={i}"
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: #의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)