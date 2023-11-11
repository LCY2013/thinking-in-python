# pip install fake-useragent
from fake_useragent import UserAgent

# ua = UserAgent(verify_ssl=False)
ua = UserAgent()

# 模拟不同的浏览器
print(f'Chrome浏览器：{ua.chrome}')
print(f'Firefox浏览器：{ua.firefox}')
print(f'Opera浏览器：{ua.opera}')
print(f'Safari浏览器：{ua.safari}')

# 随机返回头部信息，推荐使用
print(f'随机返回头部信息：{ua.random}')
