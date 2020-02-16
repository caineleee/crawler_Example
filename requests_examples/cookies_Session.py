#coding=utf-8

import requests

URL = 'http://httpbin.org/get'
data = {'name':'germey', 'age': 22}

resp = requests.get(URL, params=data)
print(resp.text)
print(type(resp.text))
print(resp.json())
print(type(resp.json()))
print(resp.content)
print(type(resp.content))
print(resp.content.decode('utf-8'))
print(type(resp.content.decode('utf-8')))


'''
	cookie 操作
'''

# 获取 cookie
URL = 'http://www.zhihu.com'
resp = requests.get(URL)
print(resp.cookies)
for key, value in resp.cookies.items():
	print(key, '=', value)


# 使用 cookie

headers = {
	'Cookie': 'd_c0="AAACbf4wzQuPTipi6L_pSvaqjzB90CutWCg=|1495528721"; q_c1=1eadbe2227344dbabb7fbbf08a819094|1529750334000|1501667483000; _zap=651f5afd-115c-48b2-bc86-6ea368562d4f; _xsrf=KKThxXPZOmxFweqInFGVAyiNFzUUTqQm; capsion_ticket="2|1:0|10:1581604685|14:capsion_ticket|44:MWJhZjI5ZDZjYTQ2NDE1ZWFjOTBjZjBiMzQ4NzIwODc=|b93418e7f81f52178e9ab1d7698a01107d7456a3347196b33f46f05eddafe082"; l_n_c=1; r_cap_id="NjZjNGViZjljZGEzNGE5MzgxMzllZTUyY2Q3YjI2NzI=|1581604689|35ece0d94b4614047eaa882915ba1e93f9848aac"; cap_id="ZWZiMmZkMTBiYTBiNGY0NWI1Njg4ZmI5ODY0Y2E4OWU=|1581604689|87566061164f2ee4095415a8678054708470c122"; l_cap_id="ZTIyMDY5NzhhNDBkNDZiYzkxMDI4NWMyY2Y3NDIzZTU=|1581604689|6ef30f0f80d9c5925b273110665739f4a9f65c26"; n_c=1; z_c0=Mi4xdW10M0JRQUFBQUFBQUFKdF9qRE5DeGNBQUFCaEFsVk5xNjB5WHdCS1ZEYjVYc19BaXF1NFJjT1lVUlJOcXMyNWh3|1581604779|73cc528f631617def037320106187a7e219ab16d; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1580634928,1581569170,1581604685,1581734922; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1581734922; KLBRSID=57358d62405ef24305120316801fd92a|1581734923|1581734920',
	'Host': 'www.zhihu.com',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}

resp = requests.get(URL, headers=headers)
print(resp.text)

# 通过 cookie 参数来设置 cookie

headers = {
	'Host': 'www.zhihu.com',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}

Cookie = 'd_c0="AAACbf4wzQuPTipi6L_pSvaqjzB90CutWCg=|1495528721"; q_c1=1eadbe2227344dbabb7fbbf08a819094|1529750334000|1501667483000; _zap=651f5afd-115c-48b2-bc86-6ea368562d4f; _xsrf=KKThxXPZOmxFweqInFGVAyiNFzUUTqQm; capsion_ticket="2|1:0|10:1581604685|14:capsion_ticket|44:MWJhZjI5ZDZjYTQ2NDE1ZWFjOTBjZjBiMzQ4NzIwODc=|b93418e7f81f52178e9ab1d7698a01107d7456a3347196b33f46f05eddafe082"; l_n_c=1; r_cap_id="NjZjNGViZjljZGEzNGE5MzgxMzllZTUyY2Q3YjI2NzI=|1581604689|35ece0d94b4614047eaa882915ba1e93f9848aac"; cap_id="ZWZiMmZkMTBiYTBiNGY0NWI1Njg4ZmI5ODY0Y2E4OWU=|1581604689|87566061164f2ee4095415a8678054708470c122"; l_cap_id="ZTIyMDY5NzhhNDBkNDZiYzkxMDI4NWMyY2Y3NDIzZTU=|1581604689|6ef30f0f80d9c5925b273110665739f4a9f65c26"; n_c=1; z_c0=Mi4xdW10M0JRQUFBQUFBQUFKdF9qRE5DeGNBQUFCaEFsVk5xNjB5WHdCS1ZEYjVYc19BaXF1NFJjT1lVUlJOcXMyNWh3|1581604779|73cc528f631617def037320106187a7e219ab16d; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1580634928,1581569170,1581604685,1581734922; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1581734922; KLBRSID=57358d62405ef24305120316801fd92a|1581734923|1581734920'

jar = requests.cookies.RequestsCookieJar()
for cookie in Cookie.split(';'):
	key, value = cookie.split('=', 1)
	jar.set(key, value)
resp = requests.get(URL)
print(resp.text)


'''
	requests 请求相当于用不同浏览器发送的请求, 如果模拟同一个浏览器发送的请求,
	使用cookie 可以做到.  但是较为繁琐, 也可以使用 Session 实现, 且比 Cookie 操作容易
'''

# 第一次请求设置一个 cookie ,第二次请求没有设置 cookie 第一次请求的 cookie
# 这样请求将无法使用第一次请你求的 cookie , 也就证明这两次请求并非模拟同一个浏览器发送的请求.

URL = 'http://httpbin.org/cookies'
URL_with_cookie = 'http://httpbin.org/cookies/set/123456789'
requests.get(URL_with_cookie)
resp = requests.get(URL)
print(resp.text)

# 使用 Session 可以快速的解决同一个浏览器模拟的问题. 不需要通过设置 cookie 即可快速达到模拟用一用户的访问

Sess = requests.Session()
Sess.get(URL_with_cookie)
resp = Sess.get(URL)
print(resp.text)

# 身份认证

# 身份认证可以使用自带的 HTTPBasicAuth
from requests.auth import HTTPBasicAuth

URl = 'http://localhost:5000'
resp = requests.get(URL, auth=HTTPBasicAuth('username', 'password'))

# # 直接使用 username 和 password 进行身份验证, 这里会默认使用 HTTPBasicAuth

resp = requests.get(URL, auth=('username', 'password'))

# 如果需要 oauth 认证, 则需要 pip install request_oauthlib

from requests_oauthlib import OAuth1

URL = 'xxxx'
auth = Auth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(URL, auth)


