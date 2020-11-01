from urllib import request,parse
from http.cookiejar import CookieJar


header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

cookiejar = CookieJar()
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
post_url = 'https://www.pplt.net/login.php?'
post_data = parse.urlencode({
    'username':'射破苍穹',
    'password':'wzzddx000'
})
req = request.Request(post_url,data=post_data.encode('utf-8'))
opener.open(req)

url='https://www.pplt.net/index.php'
rq=request.Request(url,headers=header)
resp=opener.open(rq)
print(resp.read().decode('gbk'))

