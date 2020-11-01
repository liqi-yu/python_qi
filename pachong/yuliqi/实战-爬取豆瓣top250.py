# -*- coding: utf-8 -*- 
# @Time : 2020/10/15 11:24 
# @Author : 余礼奇 
# @File : 实战-爬取豆瓣top250.py

import requests
from bs4 import BeautifulSoup

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}


#获取详情页面url
def get_detail_urls(url):
    resp=requests.get(url,headers=headers)
    # print(resp.text)
    html=resp.text
    soup=BeautifulSoup(html,'lxml')
    lis=soup.find('ol',class_='grid_view').find_all('li')
    detail_urls=[]
    for li in lis:
        detail_url=li.find('a')['href']
        # print(detail_url)
        detail_urls.append(detail_url)
    return detail_urls

#解析详情页面内容
def parse_detail_url(url,f):
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    #电影名
    name=list(soup.find('div',id='content').find('h1').stripped_strings)
    name=''.join(name)
    # print(name)
    #导演
    director=list(soup.find('div',id='info').find('span').find('span',class_='attrs').stripped_strings)
    director=''.join(director)
    # print(director)
    #编剧
    screenwriter=list(soup.find('div',id='info').find_all('span')[3].find('span',class_='attrs').stripped_strings)
    screenwriter=''.join(screenwriter)
    # print(screenwriter)
    #主演
    actor=list(soup.find('span',class_='actor').find('span',class_='attrs').stripped_strings)
    actor=''.join(actor)
    # print(actor)
    #评分
    score=soup.find('strong',class_='ll rating_num').string
    # print(score)
    f.write('{},{},{},{},{}\n'.format(name,director,screenwriter,actor,score))


def main():
    base_url='https://movie.douban.com/top250?start={}&filter='
    with open('doubantop250.csv','a',encoding='utf-8') as f:
        for x in range(0,251,25):
            url=base_url.format(x)
            detail_urls=get_detail_urls(url)
            for detail_url in detail_urls:
                parse_detail_url(detail_url,f)





if __name__=='__main__':
    main()







