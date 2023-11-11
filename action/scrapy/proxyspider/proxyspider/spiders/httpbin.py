# -*- coding: utf-8 -*-
import scrapy


# export http_proxy='http://127.0.0.1:7890'
# setting 增加 scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
# 通过 Request.meta['proxy'] 读取 http_proxy 环境变量加载代理

class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["httpbin.org"]
    # 通过ip查看请求的ip地址
    start_urls = ["https://httpbin.org"]

    # 通过header 查看user-agent
    # start_urls = ['http://httpbin.org/headers']

    def parse_item(self, response):
        item = {}
        # item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # item["name"] = response.xpath('//div[@id="name"]').get()
        # item["description"] = response.xpath('//div[@id="description"]').get()
        print("parse_items", response.text)
        return item
