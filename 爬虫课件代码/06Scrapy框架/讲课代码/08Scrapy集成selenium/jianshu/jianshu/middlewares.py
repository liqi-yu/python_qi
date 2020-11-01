# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http.response.html import HtmlResponse

class JianshuDownloaderMiddleware:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\ProgramApp\chromedriver\chromedriver.exe")

    def process_request(self, request, spider):
        # 然后用selenium去请求
        self.driver.get(request.url)

        next_btn_xpath = "//div[@role='main']/div[position()=1]/section[last()]/div[position()=1]/div"
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, next_btn_xpath))
        )

        while True:
            try:
                next_btn = self.driver.find_element_by_xpath(next_btn_xpath)
                self.driver.execute_script("arguments[0].click();", next_btn)
            except Exception as e:
                break

        # 把selenium获得的网页数据，创建一个Response对象返回给spider
        response = HtmlResponse(request.url,body=self.driver.page_source,request=request,encoding='utf-8')
        return response
