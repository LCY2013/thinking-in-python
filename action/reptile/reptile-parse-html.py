# 使用BeauifulSoup解析HTML

import requests
from bs4 import BeautifulSoup as bs

# bs4是第三方库需要使用pip命令安装

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'

header = {'user-agent': user_agent}

baseUrl = 'https://movie.douban.com/top250'

response = requests.get(baseUrl, headers=header)

bs_info = bs(response.text, 'html.parser')

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for tag in tags.find_all('a', ):
        # 获取所有链接
        print(tag.get('href'))
        # 获取电影名字
        print(tag.find('span', ).text)
