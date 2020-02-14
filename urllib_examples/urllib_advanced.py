#coding=utf-8
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

'''
	关于 build_opener 的使用

	如果页面弹出提示框需要输入用户密码, 使用以下方式可以访问
'''

username = 'ursername'
password = 'passowrd'
url = 'http://xxxxx'


userInfo = HTTPPasswordMgrWithDefaultRealm()
userInfo.add_password(None, url, username, password)

# 传入一个 HTTPPasswordMgrwithDefaultRealm 对象作为参数, 实例化一个 HTTPBasicAuthHandler 对象, 建议一个处理验证的 Handle
auth_handler = HTTPBasicAuthHandler(userInfo)
opener = build_opener(auth_handler)

try:
	result = opener.open(url)
	html = result.read().decode('utf-8')
	print(html)
except URLError as e:
	print(e.reason)


'''
	基于代理发送请求, 在本机搭建代理 运行在指定的端口上
	key 代表 SCHEMA 类型, Value 是代理链接. 链接可以添加多个
'''

from urllib.request import ProxyHandler

proxy_handler = ProxyHandler({
	'http':'http://127.0.0.1:9743',
	'https': 'https://127.0.0.1:9743'
})

opener = build_opener(ProxyHandler)
try:
	resp = opener.open('https://www.baidu.com')
	print(resp.read().decode('utf-8'))
except URLError as e:
	print(e.reason)


'''
	Cookies 处理
	
'''

import http.cookiejar
from urllib.request import HTTPCookieProcessor


# 获取 Cookies
cookie = http.cookiejar.CookieJar()
handle = HTTPCookieProcessor(cookie)
opener = build_opener(handle)
resp = opener.open('https://www.baidu.com')
for item in cookie:
	print(item.name + "=" + item.value)


# 如果要将 Cookies 保存到文件中需要使用 MozillaCookieJar 或 LWPCookieJar

file_path = 'xxxxx'
# cookie = http.cookiejar.MozillaCookieJar(file_path)
cookie = http.cookiejar.LWPCookieJar(file_path)
handle = HTTPCookieProcessor(cookie)
opener = build_opener(handle)
resp = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)


# 读取保存在文件里的 cookie 信息, 发送请求

cookie = http.cookiejar.LWPCookieJar()
cookie.load(file_path, ignore_expires=True, ignore_discard=True)
handle = HTTPCookieProcessor(cookie)
opener = build_opener(handle)
resp = opener.open('https://www.baidu.com')
print(resp.read().decode('utf-8'))


'''
	用于实现 Robots(爬虫协议) 分析, 判断网站中那些是可以爬取的, 哪些不可以
'''

from urllib.robotparser import RobotFileParser

robotp = RobotFileParser('http:www.jianshu.com/rebots.txt')
robotp.read()
print(robotp.can_fetch('*', 'http:www.jianshu.com/p/b67554025d7d'))  # 如果可以爬取返回 True
print(robotp.can_fetch('*', 'http:www.jianshu.com/search?q=python&page=1&type=collections'))  # 不可以爬取则返回 False


