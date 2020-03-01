#!/usr/bin/python
#coding=utf-8


from selenium.webdriver.support.ui import WebDriverWait
import configparser
import os
import importlib,sys
importlib.reload(sys)

class ObejctMap(object):
    def __init__(self):
        #获取存放页面元素定位表达式及定位表达式的配置文件所在绝对路径
        #os.path.abspath(__file__)表示获取当前文件所在的路径目录
        self.uiObjMapPath = os.path.dirname(os.path.abspath(__file__))+'//UiObjectMap.ini'
        print(self.uiObjMapPath)

    def getElementObject(self,driver,webSiteName,elementName):
        try:
            #创建一个读取配置文件的实例
            cf = configparser.ConfigParser()

            #将配置文件内容加载到内存
            #cf.read(self.uiObjMapPath)
            cf.read(self.uiObjMapPath,'utf-8')

            #根据 section 和 option 获取配置文件中也没元素的定位方式及定位方法表达式组成的字符串,并使用">"分割
            locators= cf.get(webSiteName,elementName).split(">>")

            #得到定位方式
            locatorMethod = locators[0]

            #得到定位表达式
            locatorExpression = locators[1]

            print(locatorMethod,locatorExpression)

            #通过显示等待方式获取页面元素
            element = WebDriverWait(driver,10).until(lambda x:x.find_element(locatorMethod,locatorExpression))

        except Exception as e:
            raise e
        else:
            #当页面元素被找到后,将该页面元素反对方返回给调用者
            return element