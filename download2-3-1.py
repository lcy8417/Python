import io
import sys
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com"

mem = req.urlopen(url)

# print(type(mem))

# print("geturl", mem.geturl())
# print("status", mem.status) #200정상, 404없음, 403접속거절, 500서버자체에서에러
# print("headers", mem.getheaders())
# print("info", mem.info())
# print("coode", mem.getcode())
# print("read", mem.read())
# print(urlparse("http://www.encar.com"))