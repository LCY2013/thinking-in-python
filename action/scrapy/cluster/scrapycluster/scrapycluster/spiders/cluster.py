import json

import scrapy

from scrapycluster.items import ScrapyclusterItem


class ClusterSpider(scrapy.Spider):
    name = "cluster"
    allowed_domains = ["httpbin.org"]
    start_urls = ["http://httpbin.org/ip"]

    def parse(self, response):
        item = ScrapyclusterItem()
        item['ip'] = json.loads(response.text)['origin']
        yield item
