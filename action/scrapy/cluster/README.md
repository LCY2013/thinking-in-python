# 步骤

## scrapy cluster

- pip install scrapy-redis
- scrapy startproject scrapycluster
- cd scrapycluster
- scrapy genspider -t crawl cluster httpbin.org
- scrapy crawl cluster
- scrapy crawl cluster --nolog
- scrapy crawl cluster -o proxies.json
- scrapy crawl cluster -o proxies.json -s LOG_ENABLED=True -s LOG_FILE=log.txt





