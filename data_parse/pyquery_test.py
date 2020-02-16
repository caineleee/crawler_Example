#coding=utf-8
import os
from pyquery import PyQuery as pq

# with open(os.path.abspath('../DataFile/maoyan_borad.html'), 'r') as f:
# 	content = f.read()

# 传入HTML 格式的字符串
# doc = pq(content)
# print(doc('li'))


# 传入指定的 URL 也可以直接获取网页
# doc = pq(url='https://cuiqingcai.com')
# print(doc('title'))
# print(doc('meta'))

# 之间传入文件路径方式打开
doc = pq(filename=os.path.abspath('../DataFile/maoyan_borad.html'))
# print(doc('li'))


#






