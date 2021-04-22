from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daun.net">daum</a></li>
        <li><a href="http://www.daun.com">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")
# print('links', type(links))
a = soup.find_all("a", string='daum')
# print('a', a)
b = soup.find_all("a", limit=3)
# print('b', b)
c = soup.find_all(string=["naver", "google"])
print(c)
for link in links:
    # print('link', type(link), link)
    href = link.attrs['href']
    txt = link.string
    # print('txt >> ', txt, 'href >> ', href)