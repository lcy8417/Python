import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}

weather_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%8B%9C&tqi=h4dBtwp0J1Zss4yS59lssssst3V-323491"
news_url = "https://news.naver.com/"
it_url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
eng_url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"

res = requests.get(weather_url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

weather_info = soup.find("div", attrs={"class":"weather_box"})
cur_tem = weather_info.find("span", attrs={"class":"todaytemp"}).get_text()
cur_info = weather_info.find("ul", attrs={"class":"info_list"}).find("p", attrs={"class":"cast_txt"}).get_text()
min_tem = weather_info.find("ul", attrs={"class":"info_list"}).find("span", attrs={"class":"min"}).get_text()
max_tem = weather_info.find("ul", attrs={"class":"info_list"}).find("span", attrs={"class":"max"}).get_text()
rain_rate_morning = weather_info.find("span", attrs={"class":"point_time morning"}).find("span", attrs={"class":"rain_rate"}).find("span", attrs={"class":"num"}).get_text()
rain_rate_afternoon = weather_info.find("span", attrs={"class":"point_time afternoon"}).find("span", attrs={"class":"rain_rate"}).find("span", attrs={"class":"num"}).get_text()
small_dust = weather_info.find("div", attrs={"class":"sub_info"}).find("dd", attrs={"class":"lv2"}).get_text()
more_small_dust = weather_info.find("div", attrs={"class":"sub_info"}).find("dd", attrs={"class":"lv1"}).get_text()

print("[오늘의 날씨]")
print(cur_info)
print("현재 "+cur_tem+"℃", "(최저 "+ min_tem + " / " + "최고 " + max_tem + ")")
print("오전 강수확률 " + rain_rate_morning + "% / " + "오후 강수확률 " + rain_rate_afternoon + "%")
print()
print("미세먼지 {}".format(small_dust))
print("초미세먼지 {}".format(more_small_dust))
print()

res = requests.get(news_url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

headline_newses = soup.find("ul", attrs={"class","hdline_article_list"}).find_all("li", limit=3)
print("[헤드라인 뉴스]")
for idx, headline_news in enumerate(headline_newses):
    news_text = headline_news.find("div", attrs={"class","hdline_article_tit"}).get_text().strip()
    news_link = headline_news.find("div", attrs={"class","hdline_article_tit"}).find("a")["href"]
    print(news_text, f"https://news.naver.com/{news_link}")
print()

res = requests.get(it_url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

it_newses = soup.find("td", attrs={"class":"content"}).find("ul", {"class":"type06_headline"}).find_all("li")

print("[IT 뉴스]")
for i in range(0, 3):
    news_text = it_newses[i].find_all("dt")
    if(len(news_text) == 1):
        print(news_text[0].get_text().strip())
        print(news_text[0].find("a")['href'])
    else:
        print(news_text[1].get_text().strip())
        print(news_text[0].find("a")['href'])
    print()
print()


res = requests.get(eng_url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

print("[오늘의 영어 회화]")
print("(영어 지문)")

fingerprint = soup.find("div", attrs = {"class":"conv_container"}).find_all("div", attrs={"class":"conv_txtBox"})
korean_fingerprint = fingerprint[0]
english_fingerprint = fingerprint[1]

print(english_fingerprint.find("b", attrs={"class":"conv_txtTitle"}).get_text())
english_fingerprint_list = english_fingerprint.find_all("span", attrs = {"class":"conv_sub"})
korean_fingerprint_list = korean_fingerprint.find_all("span", attrs = {"class":"conv_sub"})
for e in english_fingerprint_list:
    print(e.get_text())

print()
print(korean_fingerprint.find("b", attrs={"class":"conv_txtTitle"}).get_text().strip())
for k in korean_fingerprint_list:
    print(k.get_text())



