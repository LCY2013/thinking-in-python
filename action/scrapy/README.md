# 步骤

## movies 爬虫

- scrapy startproject spiders
- cd spiders && cd spiders
- scrapy genspider -t crawl movies movie.douban.com
- scrapy crawl movies

## 爬虫示例

- scrapy startproject movies_logs
- cd movies_logs
- scrapy genspider -t crawl movies movie.douban.com
- scrapy crawl movies_logs

## proxyspider http_proxy

- scrapy startproject proxyspider
- cd proxyspider
- scrapy genspider -t crawl httpbin httpbin.org
- scrapy crawl httpbin





