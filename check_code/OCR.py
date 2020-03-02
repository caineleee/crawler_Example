#coding=utf-8


# import 之前需要先 pip 安装. install command: pip install tesserocr pillow

import tesserocr
from PIL import Image


image = Image.open('./code2.jpeg')

# what ? 识别错误! 废物!
result = tesserocr.image_to_text(image)
print(result)


# 将图像转换为灰度图像, 传入 "L"
image = image.convert('L')
image.show()


# 将图像进行二值化处理, 范围是 0 -255. 这样可以把图像的文字显示黑白化, 提高识别率
image = image.convert('1')
image.show()

# 哼哼  经过调试 发现这个破图片要二值化设置为 122 才可以识别 em.... 不过总算能正确识别了
image = image.convert('L')
threshold = 122
table = []
for i in range(256):
	if i < threshold:
		table.append(0)
	else:
		table.append(1)

image = image.point(table, '1')
result = tesserocr.image_to_text(image)
print(result)
image.show()






