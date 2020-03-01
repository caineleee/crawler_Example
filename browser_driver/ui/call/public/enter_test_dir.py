#!/usr/bin/python
#coding=utf-8

def enter_test_dir(self):
    '''
    进入到指定的二级目录
    :param self:
    :return:
    '''

    #进入到指定的一级目录
    level1 = self.obj.getElementObject(self.driver,'filePage','level1')
    level1.click()

    #进入到指定的二级目录
    level2 = self.obj.getElementObject(self.driver,'filePage','level2')
    level2.click()

    print('进入到第二级测试目录中....')
