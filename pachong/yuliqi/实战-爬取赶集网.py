# -*- coding: utf-8 -*- 
# @Time : 2020/10/15 18:52 
# @Author : 余礼奇 
# @File : 实战-爬取赶集网.py
import requests
import re


headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}

def parse_page(page_url):
    resp=requests.get(page_url,headers=headers)
    text=resp.text
    houses=re.findall(r'''
        <div.+?ershoufang-list".+?<a.+?js-title.+?>(.+?)</a>        #获取房源的标题
        .+?<dd.+?dd-item.+?<span>(.+?)</span>           #获取房源的户型
        .+?<span.+?<span>(.+?)</span>           #获取房源面积
        .+?<div.+?price.+?<span.+?>(.+?)</span>   #获取房源的价格   
    ''',text,re.VERBOSE|re.DOTALL)
    for house in houses:
        print(house)



def main():
    base_url='http://gz.ganji.com/zufang/pn{}/'
    for x in range(1,11):
        page_url=base_url.format(x)
        parse_page(page_url)
        break




if __name__=='__main__':
    main()