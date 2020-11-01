from urllib import request

url='https://www.biedoul.com/index/'
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
for i in range(3):
    i=5962+i
    urll=url+str(i)
    rq=request.Request(urll,headers=header)
    resp=request.urlopen(rq)
    print(resp.read().decode())

