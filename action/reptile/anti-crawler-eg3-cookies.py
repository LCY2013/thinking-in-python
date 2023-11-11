import requests

# 在同一个 Session 实例发出的所有请求之间保持 Cookie 信息
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/12345678')
r = s.get('http://httpbin.org/cookies')

# {
#   "cookies": {
#     "sessioncookie": "12345678"
#   }
# }
print(r.text)

# 会话可以使用上下文管理器
with requests.Session() as s:
    print(s.get('http://httpbin.org/cookies/set/sessioncookie/12345678').text)
