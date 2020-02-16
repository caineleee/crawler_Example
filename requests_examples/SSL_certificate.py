#coding=utf-8

import requests

# 设置不进行 SSL 证书验证
URL = 'https://www.12306.cn'
resp = requests.get(URL, verify=False)

# 忽略证书验证警告
from requests.packages import urllib3

urllib3.disable_warnings()
resp = requests.get(URL, verify=False)


# 通过捕获警告到日志的方式忽略警告
import logging

logging.captureWarnings(True)
resp = requests.get(URL, verify=False)


# 指定一个本地证书作为哭护短证书, 这可以是单个文件(包含秘钥和证书)
# 或一个包含两个文件卤江南的元组

resp = requests.get(URL, cert=('/path/server.crt', '/path/key'))

