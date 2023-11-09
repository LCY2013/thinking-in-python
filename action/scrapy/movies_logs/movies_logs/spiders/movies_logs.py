import scrapy
from scrapy import Selector
from scrapy.spiders import CrawlSpider


class MoviesSpider(CrawlSpider):
    # 定义爬虫名称
    name = "movies_logs"
    allowed_domains = ["movie.douban.com"]
    # 起始URL列表
    start_urls = ["https://movie.douban.com"]

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        # for i in range(0, 10):
        i = 0
        url = f'https://movie.douban.com/top250?start={i * 25}'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
        # url 请求访问的网址
        # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
        # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        # 打印网页的url
        print(response.url)
        # 打印网页的内容
        # print(response.text)

        # soup = BeautifulSoup(response.text, 'html.parser')
        # title_list = soup.find_all('div', attrs={'class': 'hd'})
        movies = Selector(response=response).xpath('//div[@class="hd"]')
        for movie in movies:
            #     title = i.find('a').find('span',).text
            #     link = i.find('a').get('href')
            # 路径使用 / .  .. 不同的含义　
            title = movie.xpath('./a/span/text()')
            link = movie.xpath('./a/@href')
            print('-----------')
            print(title)
            print(link)
            print('-----------')
            print(title.extract())
            print(link.extract())
            print(title.extract_first())
            print(link.extract_first())
            print(title.extract_first().strip())
            print(link.extract_first().strip())
