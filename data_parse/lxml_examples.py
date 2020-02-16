#coding=utf-8
import os
from lxml import etree


# etree 读取文本的形式
# with open(os.path.abspath('../DataFile/maoyan_borad.html'), 'r') as f:
# 	content = f.read()
# html = etree.HTML(content)

# etree 读取文件的形式
html = etree.parse('../DataFile/maoyan_borad.html', etree.HTMLParser(),)

# etree.tostring 方法必须使用 encoding='utf-8' 参数, 否则输出时中文无法正常显示
result = etree.tostring(html,encoding="utf-8")
print(result)

# 输出所有元素
for i in html.xpath('//*/text()'):

	# if i.text != None:
	# 	print(i.text)
	if i != None:
		print(i)

	# 目前很二的是, 中文输出乱码.  貌似没有找到简单的解决方案 ?  .....
	# 算了抛弃这个破玩意, 先弄 Beautiful Soup 也许就没有这个问题了.   切