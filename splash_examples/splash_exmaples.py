#coding=utf-8

# 需要先用docker 部署 splash 服务, command: docker run -d -p 8050:8050 scrapinghub/splash(本地部署, 也可以远程服务器部署)

import requests


# 获取浏览器渲染之后的源代码
splash_env = 'http://localhost:8050/render.html?url='
url = 'https:/www.baidu.com'
URL = splash_env + url

resp = requests.get(URL)
print(resp.text)


# 等待时长, 可以用于加载的等待时间设置
url = 'https://www.taobao.com'
wait = '&wait=5'
URL = splash_env + url + wait

resp = requests.get(URL)
print(resp.text)


# 以 Json 格式返回请求的信息
splash_env = 'http://localhost:8050/render.json?url='
url = 'https://www.taobao.com'
wait = '&wait=5'
URL = splash_env + url + wait

resp = requests.get(URL)
print(resp.text)


# 实现交互操作的神技能!!!!

from urllib.parse import quote

# 定义一个脚本
lua = '''
function main(splash)
	return 'hello'
end
'''
splash_env = 'http://localhost:8050/execute?lua_source='

URL = splash_env + quote(lua)

resp = requests.get(URL)
print(resp.text)

