#coding=utf-8

import requests
import re
import json


# def get_board_element(html):
# 	pattern = {}
# 	items = {}
#
# 	result = []
# 	pattern['order'] = re.compile('<dd>.*?board-index.*?>(.*?)</i>',re.S)
# 	pattern['image'] = re.compile('.*?data-src="(.*?)"', re.S)
# 	pattern['name'] = re.compile('.*?name.*?a.*?>(.*?)</a>', re.S)
# 	pattern['start'] = re.compile('.*?star.*?>(.*?)</p>', re.S)
# 	pattern['releaseTime'] = re.compile('.*?releasetiome.*?>(.*?)</p>',re.S)
# 	pattern['integger'] = re.compile('.*?intergeer.*?>(.*?)</i>',re.S)
# 	pattern['fraction'] = re.compile('.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
# 	for key, value in pattern.items():
# 		items[key] = re.findall(value, html) if key != 'name' else re.findall(value, html)[3:]
# 	for num in range(10):
# 		info = {}
# 		for key in items.keys():
# 			if len(items[key]) < num or len(items[key]) == 0:
# 				continue
# 			info.update({key: items[key][num]})
# 		result.append(info)
# 	return result


def get_board_element(html):
	pattern = {}
	items = {}

	pattern['order'] = re.compile('<dd>.*?board-index.*?>(.*?)</i>',re.S)
	pattern['image'] = re.compile('.*?data-src="(.*?)"', re.S)
	pattern['name'] = re.compile('.*?name.*?a.*?>(.*?)</a>', re.S)
	pattern['start'] = re.compile('.*?star.*?>(.*?)</p>', re.S)
	pattern['releaseTime'] = re.compile('.*?releasetiome.*?>(.*?)</p>',re.S)
	pattern['integger'] = re.compile('.*?intergeer.*?>(.*?)</i>',re.S)
	pattern['fraction'] = re.compile('.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
	for key, value in pattern.items():
		items[key] = re.findall(value, html) if key != 'name' else re.findall(value, html)[3:]
	for num in range(10):
		info = {}
		for key in items.keys():
			if len(items[key]) < num or len(items[key]) == 0:
				continue
			if key == 'start':
				items[key][num] = items[key][num].strip()
			info.update({key: items[key][num]})
		yield json.dumps(info, ensure_ascii=False)



def get_page(url, offset=0):
	headers = {
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
	}
	data = {'offset': offset}
	resp = requests.get(url, params=data, headers=headers)
	print('The URL:',resp.url)
	if resp.status_code == 200:
		return get_board_element(resp.text)
	else:
		return None



if __name__ == '__main__':
	url = 'https://maoyan.com/board/4'
	for i in range(10):
		number = i * 10
		result = get_page(url,offset=number)
		for i in result:
			print(i)