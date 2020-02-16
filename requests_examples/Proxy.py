#coding=utf-8


import requests


# 代理无效, 需要更换实际可用的代理
proxies = {
	'http': 'http://10.10.1.10:3128',
	'https': 'http://10.10.1.10:1010'
}

URL = 'https://www.taobao.com'

requests.get(URL, proxies=proxies)


# 如果使用呢 HTTP Basic Auth, 可以使用那个 user:password@Host:Port 语法来设置代理

proxies = {
	'http': 'http://UserName:Password@10.10.1.10:3128',
	'https': 'http://UserName:Password@10.10.1.10:1010'
}
requests.get(URL, proxies=proxies)


