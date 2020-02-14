#coding=utf-8
import urllib.parse
import urllib.request


URL = 'https://www.python.org'

resp = urllib.request.urlopen(URL)

# print(resp.read().decode('utf-8'))
print(type(resp))

print(resp.status)
print(resp.getheaders())
print(resp.getheader('Server'))


URL = 'http://httpbin.org/post'
data = {'word':'hello'}
# 将字典转换为 url 参数的字符串
dataToStr = urllib.parse.urlencode(data)
# 参数需要转换为字节码
dataToBytes = bytes(dataToStr, encoding='utf-8')
resp = urllib.request.urlopen(URL,data=dataToBytes)
# decode 是将 bytes 数据转换为 string
print(resp.read().decode('utf-8'))

