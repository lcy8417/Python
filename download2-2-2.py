import io
import sys
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAxMTZfMTc1%2FMDAxNjEwNzc2ODU2MTAy.op2Ed60TaKfEkQKVizP9MXDxGU7-UmDGy2lsnRhIWjcg.U-rEPN7_K2wNKLph9JyZd0OMyAySNUk6ZJlPs57M1Yog.JPEG.hkim116%2F%25B0%25F5.jpg&type=sc960_832"
htmlURL = "http://www.google.com"

savePath1 = "c:/test1.jpg"
savePath2 = "c:/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

saveFile1 = open(savePath1,'wb')
saveFile1.write(f)
saveFile1.close()