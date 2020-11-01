from urllib import request
import os

url='https://www.x520xs.com/15/15537/18363836.html'
resp=request.urlopen(url)
print(resp.read().decode())

# f=open('long.txt','w')
# f.write(resp.read())
# f.close()
#不能写入，是write的问题，或者换种方法可以？