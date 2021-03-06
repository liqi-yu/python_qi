# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/p/25d5e55d11b6']

    rules = [
        Rule(link_extractor=LinkExtractor(allow=r'.*/p/[0-9a-z]{12}'),callback="parse_detail",follow=True)
    ]

    def parse_detail(self, response):
        print(response.text)
