import requests
import urllib.request as req
from bs4 import BeautifulSoup

# Fake Header 정보

# 헤더 선언
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
}
url = "https://finance.daum.net/"
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')
soup = BeautifulSoup(res,"html.parser")

top = soup.select("ul")

print(soup)