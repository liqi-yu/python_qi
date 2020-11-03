# -*- coding: utf-8 -*- 
# @Time : 2020/11/3 19:31 
# @Author : 余礼奇 
# @File : qiushibaike_spider.py

import scrapy

class QiushiSpider(scrapy.Spider):
    name='qiushibaike'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

    def start_requests(self):
        base_url='https://www.qiushibaike.com/text/page/{}/'
        urls=[]
        for i in range(1,14):
            urls.append(base_url.format(i))
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse,headers=self.headers)

    def parse(self, response, **kwargs):
        # page=response.url.split('/')[-2]
        # filename='qiushi-%s.html'%page
        # with open(filename,'wb') as f:
        #     f.write(response.body)
        # self.log('saved file %s'%filename)


        content_left_div=response.xpath('//*[@id="content"]')
        content_list_div=content_left_div.xpath('./div')

        for content_div in content_list_div:
            yield {
                'author':content_div.xpath('.//div/a[2]/h2/text()').get(),
                'content':content_div.xpath('.//a/div/span/text()').getall()
            }



