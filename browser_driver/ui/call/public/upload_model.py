#!/usr/bin/python
#coding=utf-8

import os,random,time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class upload_file:
    def upload(self):

        # 文件路径
        path = '/Users/xxxxx/Documents/xxxx'

        # 获取目录下文件的列表
        file_list = os.listdir(path)

        files = []

        # 获取目录下的文件列表
        for i in file_list:
            # os.path.splitext():分离文件名与扩展名
            if os.path.splitext(i)[1] == '.rvt':
                files.append(i)
                print(i)

        # 随机选取一个目录下的文件
        choose = random.randint(0, len(files) - 1)
        self.file = files[choose]
        print('文件名是:  ', self.file)

        # 上传上面选取的文件
        uploadButton = self.obj.getElementObject(self.driver, 'filePage', 'uploadButton')
        uploadButton.send_keys(path + '/' + self.file)  # 上传随机的一个文件

        #等待上传中的模型进度组件出现
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self.obj.getElementObject(self.driver, 'filePage', 'uploadingFile')))

        #定位正在上传统计组件
        uploadingCount = self.obj.getElementObject(self.driver, 'filePage', 'uploadingCount')

        #根据正在上传组件显示的内容判断模型上传的状态
        while uploadingCount.text != '正在上传：0':
            print('模型正在上传')
            time.sleep(5)
        else:
            print('模型上传成功!')

        # 等待两秒
        time.sleep(2)

        #定位文件列表中第一个文件的文件名
        self.models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        model_name = self.models_list.find_element_by_xpath('div[1]/span[2]')

        #判断文件名是否与上传的文件名相同
        self.assertTrue(model_name, self.file)