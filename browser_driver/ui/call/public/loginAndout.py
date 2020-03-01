#!/usr/bin/python
#coding=utf-8

from browser_driver.ui.call.public.ObjectMap import ObejctMap
from selenium import webdriver
'''
用于操作 login / logout / project select 等必须步骤的方法实现
'''

def login(self):
    self.obj = ObejctMap()
    self.driver = webdriver.Chrome()
    self.driver.set_window_size(1920,1080)
    self.driver.get('http://000.000.000.000:80/#/login')
    username = self.obj.getElementObject(self.driver,'login','username')
    username.send_keys('User_Name')
    password = self.obj.getElementObject(self.driver,'login','password')
    password.send_keys('Password')
    loginButton = self.obj.getElementObject(self.driver,'login','loginButton')
    loginButton.click()

def project_choose(self):
    project = self.obj.getElementObject(self.driver,'project_choose','project')
    project.click()

    project_option = self.obj.getElementObject(self.driver,'project_choose','projectOption')
    project_option.click()

    comfirm = self.obj.getElementObject(self.driver,'project_choose','confirmButton')
    comfirm.click()

    self.currect_project = self.obj.getElementObject(self.driver,'project_choose','currectProject')

    self.currect_project.is_displayed
    assert self.currect_project.text == u'项目名称'

def logout(self):
    self.driver.quit()