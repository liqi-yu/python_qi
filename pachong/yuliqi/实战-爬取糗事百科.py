# -*- coding: utf-8 -*- 
# @Time : 2020/10/15 19:17 
# @Author : 余礼奇 
# @File : 实战-爬取糗事百科.py

import re
import requests

def parse_page(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    resp=requests.get(url,headers)
    text=resp.text
    contents=re.findall(r'<div\sclass=.+?>.*?<span>(.*?)</span>',text,re.DOTALL)
    duanzi=[]
    for content in contents:
        x=re.sub(r'<.*?>','',content)
        duanzi.append(x.strip())
        print(x.strip())
        print('-'*50)






def main():
    base_url='https://www.qiushibaike.com/text/page/{}/'
    for x in range(1,11):
        url=base_url.format(x)
        parse_page(url)
        break  #为了节省时间，只怕去一页的信息




if __name__=='__main__':
    main()


