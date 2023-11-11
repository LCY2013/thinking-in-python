# http 协议的 GET 方法
import requests

r = requests.get('https://github.com')
print(r.status_code)
print(r.headers['content-type'])
# r.text
print(r.encoding)
# r.json()

# http 协议的 POST 方法
import requests

r = requests.post('http://httpbin.org/post', data={'key1': 'value1', 'key2': 'value2'})
print(r.json())
