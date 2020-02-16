#coding=utf-8
import os
from bs4 import BeautifulSoup

with open(os.path.abspath('../DataFile/maoyan_borad.html'), 'r') as f:
	content = f.read()
soup = BeautifulSoup(content, 'lxml')

# 输出全部内容
print(soup.prettify())

# 获取整个元素
print(soup.head)

# 获取元素标签名称
print(soup.title.name)

# 获取元素文本
print(soup.title.string)

# 获取某个元素的属性
print(soup.p.attrs)

# 获取某个元素的属性值
print(soup.p.attrs['class'])

# 获取元素属性值简化写法
print(soup.p['class'])

# 获取指定元素的所有你内容(包含子元素内容)
print(soup.div.contents)

# 获取元素的直接子节点
print(soup.ul.children)
for i in soup.ul.children: print(i)

# 获取元素的所有子节点(直接子节点 & 非直接子节点)
print(soup.ul.descendants)
for i in soup.ul.descendants: print(i)

# 获取元素的上一级父节点的所有内容
print(soup.span.parent)

# 获取元素的上两层父节点内容
print([i for i in enumerate(soup.span.parents)])

# 获取同级节点   同级节点获取有问题, 无法获取元素, 需要后续补充.  其实没啥用这个破玩意, 我有了 find_all() 根本用不到这个!
# print('next_sibling(下一个同级节点) :', soup.p.next_sibling)
# print('next_sibling(下一个同级节点) :', soup.link.next_sibling.string)
# print('next_sibling(下一个同级节点) :', soup.link.next_elements)
# print('next_sibling(下一个同级节点) :', soup.link.next_elements.strings)

# 使用 find_all 函数来获取所有符合的元素

# attrs 为字典形式, 可以把元素的属性以字典形式传入, 并返回结果
print(soup.find_all(attrs={'class':'name'}))

# 根据指定的 id 获取元素
print(soup.find_all(id='app'))

# 根据指定的标签名获取元素
print(soup.find_all(name='title'))

# 根据 class 属性获取元素
print(soup.find_all(class_='user-menu'))


# 用 text 参数来匹配文件的内容, 可以传入字符串和正则表达式
import re
print(soup.find_all(text=re.compile('主演')))

# 使用 CSS 选择器, 需要调用 select() 方法
# 根据 id 获取元素
print(soup.select('#app'))

# 根据 class 获取元素
print(soup.select('.releasetime'))

# 根据标签名获取元素
print(soup.select('meta'))

# 根据标签层级获取元素
print(soup.select('div span'))

# 使用嵌套层级获取元素
for ul in soup.select('ul'):
	print(ul.select('li'))

# 获取属性
for ul in soup.select('ul'):
	print(ul.attrs['class'])

# 获取文本  这里要说一下, 有人说 string 属性和 get_text 方法效果完全一致. 但是并不是的!!!
# sting 应该是只能获取不换行的元素文本. 如果涉及到换行的话只能使用 get_text() 方法才能获取到
for ul in soup.select('ul'):
	for a in ul.select('li'):
		print('使用 "sting" 属性 :',a.string)
		print('使用 "get_text()" 方法 :',a.get_text())