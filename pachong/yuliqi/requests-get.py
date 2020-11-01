import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
kw={'wd':'中国'}

response = requests.get('https://www.baidu.com/s',headers=headers,params=kw)
print(response)

#查询响应内容
# print(response.text)#返回Unicode格式数据
# print(response.content.decode('utf-8'))#返回字节流数据
# print(response.url)

