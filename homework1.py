import io
import sys
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imageUrl = "https://ssl.pstatic.net/tveta/libs/1327/1327573/2a7c083a99c4e2d2a239_20210422154744590.jpg"
videoUrl = "https://tvetamovie.pstatic.net/libs/1327/1327809/a93685d17e3f7b9f137f_20210422112141233.mp4-pMAIN-v0-f130279-20210422112416217.mp4"

reqData1 = req.urlopen(imageUrl).read()
reqData2 = req.urlopen(videoUrl).read()

savePath1 = "c:/img.jpg"
savaPath2 = "c:/img2.jpg"
with open(savePath1, "wb") as saveFile1:
    saveFile1.write(reqData1)

# with open(savePath2, "wb") as saveFile2:
#     saveFile2.write(reqData2)

print("dd")