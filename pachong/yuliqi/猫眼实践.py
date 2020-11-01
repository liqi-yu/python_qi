from urllib import  request

url = 'http://piaofang.maoyan.com/dashboard'
header={
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

rq=request.Request(url,headers=header)
resp = request.urlopen(rq)

print(resp.read().decode())#解码，能识别汉字了

