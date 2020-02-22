#coding=utf-8
import os
from pyquery import PyQuery as pq

with open(os.path.abspath('../DataFile/maoyan_borad.html'), 'r') as f:
	content = f.read()

# 传入HTML 格式的字符串
doc = pq(content)
print(doc('li'))


# 传入指定的 URL 也可以直接获取网页
doc = pq(url='https://cuiqingcai.com')
print(doc('title'))
print(doc('meta'))

# 直接传入文件路径方式打开  这种方式好像存在中文编码问题, encoding 参数无效. 如果直接读取字符串则没有是这样的问题
doc = pq(filename=os.path.abspath('../DataFile/maoyan_borad.html'), encoding='utf-8')

# 按照标签名获取元素
print(doc('li'))


# 按照 id 获取元素
print(doc('#app'))


# 组合查询
print(doc('#app p').text())
print(doc('#app .releasetime'))
for i in doc('#app p'):
	print(i.text)


# 获取子元素  find 的寻找范围是选中节点的全部子节点
div = doc('#app')
print(div.find('.name'))


# 获取子元素 children 寻找范围为直接子节点
items = doc('.download-icon')
print(items.children('.down-content'))
print(div.children('p'))

# 获取直接父节点
items = doc('.download-icon')
print(items.parent())


# 获取所有父节点
items = doc('.download-icon')
print(items.parents())

# 获取兄弟节点
items = doc('title')
print(items.siblings('link'))


# 获取元素的属性
print(doc('.search-form').attr('target'))
print(doc('.search-form').attr.target)

# 获取多个元素的属性:
for element in doc('.image-link').items():
	print(element.attr.href)


# 操作节点

# 添加上传 class
title = doc('title')
print(title)
title.add_class('haha')
print(title)
title.remove_class('haha')
print(title)

# # 添加其他属性
title = doc('title')
print(title)
title.attr('name', 'added_name')
print(title)
#
# 修改元素文本内容
title.text('Changed title content')
print(title)
#
# 元素内部插入 HTML 节点
title.html('<span> Edited the title content to insert a span node</span>')
print(title)





