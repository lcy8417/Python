import requests
url = "https://www.google.co.kr/"
res = requests.get("http://google.com")
res.raise_for_status()
print(res.text)

with open("youtube/simple.html", "w", encoding="utf8") as f:
    f.write(res.text)