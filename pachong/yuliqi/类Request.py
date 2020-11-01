from urllib import request

header={
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
rq=request.Request('https://www.baidu.com',headers=header)
resp=request.urlopen(rq)
print(resp.read())