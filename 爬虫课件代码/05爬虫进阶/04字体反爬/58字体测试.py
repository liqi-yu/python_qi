import requests
import re
import base64
from fontTools.ttLib import TTFont

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
resp = requests.get("https://cs.58.com/chuzu/",headers=headers)
text = resp.text
font_face = re.search(r"@font-face.+base64,(.+?)'\)",text).group(1)

font_data = base64.b64decode(font_face)
with open('58字体测试.ttf','wb') as fp:
    fp.write(font_data)

baseFont = TTFont("58字体测试.ttf")

baseFont.saveXML("58字体测试.xml")