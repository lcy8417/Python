import requests

s = requests.Session()
r = s.get('https://www.naver.com')
# print('1',r.text)
#PUT(FETCH), DELETE, GET, POST

# r = s.get('http://httpbin.org/cookies', cookies={'from':'myName'})
# print(r.text)

url = 'http://httpbin.org/get'
headers = {'user-agent':'myPythonApp_1.0.0'}

# r = s.get(url, headers=headers)
# print(r.text)

s.close()

with requests.Session() as s:
    r = s.get('https://www.naver.com')
    print(r.text)