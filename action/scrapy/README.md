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
- scrapy crawl httpbin --nolog
- scrapy crawl httpbin -o proxies.json
- scrapy crawl httpbin -o proxies.json -s LOG_ENABLED=True -s LOG_FILE=log.txt

## randproxy http_proxy

- scrapy startproject randproxy
- cd randproxy
- scrapy genspider -t crawl httpbin httpbin.org
- scrapy crawl httpbin
- scrapy crawl httpbin --nolog
- scrapy crawl httpbin -o proxies.json
- scrapy crawl httpbin -o proxies.json -s LOG_ENABLED=True -s LOG_FILE=log.txt





