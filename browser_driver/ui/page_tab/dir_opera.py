#!/usr/bin/python
#coding=utf-8

import unittest,time,traceback

from bson import ObjectId
from pymongo import MongoClient
from browser_driver.ui.call.public.loginAndout import login,logout,project_choose
from browser_driver.ui.call.public.custom_error import customError
from selenium.webdriver import ActionChains


class MyTestCase(unittest.TestCase):
    def setUp(self):
        login(self)
        project_choose(self)

    def tearDown(self):
        logout(self)

    def test_1_add_level1_dir_cancel(self):
        '''
        check add directory cancel funtion is available
        :return:
        '''
        #click add directory button
        add_dir_button = self.obj.getElementObject(self.driver,'filePage','addDirButton')
        add_dir_button.click()

        #Type 'selenium' in the textbox and click cancel button
        add_dir_textbox = self.obj.getElementObject(self.driver,'filePage','addDirTextBox')
        add_dir_textbox.send_keys('selenium')
        cancel_add_button = self.obj.getElementObject(self.driver,'filePage','cancelAddButton')
        cancel_add_button.click()

        #positioning the name of first record
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record_name = models_list.find_element_by_xpath('div[1]/span[2]')

        #check if the cancelled add directory is saved.
        try:
            self.assertEqual(first_record_name.text,'selenium')
        except AssertionError:
            pass
        except Exception as e:
            print(traceback.print_exc())
        else:
            raise customError('放弃添加的文件夹竟然被保存了?')

    def test_2_add_level1_dir_confirm(self):
        '''
        check if the dirctory add funtion is available
        :return:
        '''
        # click add directory button
        add_dir_button = self.obj.getElementObject(self.driver, 'filePage', 'addDirButton')
        add_dir_button.click()

        # Type 'selenium' in the textbox and click confirm button
        add_dir_textbox = self.obj.getElementObject(self.driver, 'filePage', 'addDirTextBox')
        add_dir_textbox.send_keys('selenium')
        confirm_add_button = self.obj.getElementObject(self.driver, 'filePage', 'confirmAddButton')
        confirm_add_button.click()

        #Positioning the name of first record
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record_name = models_list.find_element_by_xpath('div[1]/span[2]')

        # Check if the directory has been created .
        try:
            self.assertEqual(first_record_name.text,'selenium')
        except AssertionError as e:
            print(traceback.print_exc())
        else:
            raise customError('添加的文件夹竟然没有被保存?')

    def test_3_rename_level1_dir_cancel(self):
        '''
        Check if rename of directory funtion is available
        :return:
        '''

        #Positioning the first record
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record_name = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record_name).perform() # move the mouse pointer on the record

        # Click Rename button
        rename_dir_button = self.obj.getElementObject(self.driver,'filePage','renameButton')
        rename_dir_button.click()

        #Type string 'selenium' in textbox
        rename_dir_textbox = self.obj.getElementObject(self.driver,'filePage','reNameTextBox')
        rename_dir_textbox.send_keys('rename')

        #Click cancel button to cancel the rename opera
        rename_dir_cancel = self.obj.getElementObject(self.driver,'filePage','cancelReNameButton')
        rename_dir_cancel.click()

        # check if the cancelled rename directory is saved.
        try:
            self.assertEqual(first_record_name.text, 'rename')
        except AssertionError:
            pass
        except Exception:
            print(traceback.print_exc())
        else:
            raise customError('放弃重命名的文件夹竟然被保存了?')

    def test_4_rename_level1_dir_confirm(self):
        '''
        Check if the rename directory funtion is available
        :return:
        '''

        # Positioning the first record
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record).perform()  # move the mouse pointer on the record

        # Click Rename button
        rename_dir_button = self.obj.getElementObject(self.driver, 'filePage', 'renameButton')
        rename_dir_button.click()

        # Type string 'selenium' in textbox
        rename_dir_textbox = self.obj.getElementObject(self.driver, 'filePage', 'reNameTextBox')
        rename_dir_textbox.send_keys('rename')

        # Click cancel button to cancel the rename opera
        rename_dir_confirm = self.obj.getElementObject(self.driver, 'filePage', 'confirmReNameButton')
        rename_dir_confirm.click()

        time.sleep(2)
        # Check if the directory has been renamed .
        first_record_name = first_record.find_element_by_xpath('//div[@class="ivu-checkbox-group"]/div[1]/span[2]')
        try:
            self.assertEqual(str(first_record_name.text), 'rename')
        except AssertionError as e:
            print(traceback.print_exc())

    def test_5_delete_level1_dir_cancel(self):
        '''
        Check if the delete cancel funtion is available
        :return:
        '''

        # 连接 MongoDB 数据库
        client = MongoClient('000.000.000.000', 27017)
        db = client['xxxx']
        db.authenticate("{DB_User_Name}", "DB_Password")  # 输入数据库的用户密码
        collection = db.folder  # 表名

        # 查询列表数据
        data = collection.find({'shopId':'4','type':1})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records = {}
        for i in data:
            sub = dict(i)
            new = {cou: sub}
            records.update(new)
            cou += 1

        # Positioning the first record
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record).perform()  # move the mouse pointer on the record

        # Click Rename button
        delete_button = self.obj.getElementObject(self.driver, 'filePage', 'deleteButton')
        delete_button.click()

        # Check if the content delete alert pop-up box is correct
        delete_alert = self.obj.getElementObject(self.driver, 'filePage', 'deleteAlert')
        delete_alert.is_displayed()  # 检查弹框是否显示

        delete_alert_title_range = self.obj.getElementObject(self.driver, 'filePage', 'deleteAlertTitle')
        delete_alert_title = delete_alert_title_range.find_element_by_xpath('s')
        self.assertEqual(delete_alert_title.text, '删除文件夹')  # 检查弹框标题是否正确

        # 检查弹出框的路径是否显示正确
        delete_alert_dir = self.obj.getElementObject(self.driver, 'filePage', 'deleteAlertDirectory')
        delete_alert_dir.is_displayed()  # 验证是否存在
        self.assertEqual(delete_alert_dir.find_element_by_xpath('span[1]').text, '全部>')  # 根目录验证
        # self.assertEqual(delete_alert_dir.find_element_by_xpath('span[2]').text, 'Auto Test>')  # 一级目录验证
        # self.assertEqual(delete_alert_dir.find_element_by_xpath('span[3]').text, 'ReNam1>')  # 二级目录验证
        # self.assertEqual(delete_alert_dir.find_element_by_xpath('span[4]').text, 'ReNamed.rvt')  # 文件名验证

        delete_alert_text = self.obj.getElementObject(self.driver, 'filePage', 'deleteAlertText')
        self.assertEqual(delete_alert_text.text, '删除此(些)文件夹后，将无法恢复，文件夹内的所有内容会被一起删除，您是否确定删除？')  # 弹框文本校验

        # 第一种取消方式 : 点击关闭按钮
        close_button = delete_alert_title_range.find_element_by_xpath('span')
        close_button.click()
        # time.sleep(2)

        # 验证弹框是否消失,数据是否删除
        from selenium.common.exceptions import StaleElementReferenceException
        try:
            delete_alert.is_displayed()
        except StaleElementReferenceException:
            print('弹框消失')
        else:
            raise customError('弹框没有消失,测试失败')

        # 查询列表数据
        data2 = collection.find({'shopId': '4', 'type': 1})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records2 = {}
        for i in data2:
            sub = dict(i)
            new = {cou: sub}
            records2.update(new)
            cou += 1
        # Check if the folder is deleted
        self.assertEqual(records[len(records)-1]['name'],records2[len(records2)-1]['name'])

        #第二种方式
        first_record = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record).perform()
        delete_button.click()
        cancel_button = self.obj.getElementObject(self.driver, 'filePage', 'deleteCancelButton')
        cancel_button.click()  # 点击取消按钮

        # 检查弹框是否显示
        try:
            delete_alert.is_displayed()
        except StaleElementReferenceException:
            print('弹框消失')
        else:
            raise customError('弹框没有消失,测试失败')

        # 查询列表数据
        data3 = collection.find({'shopId': '4', 'type': 1})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records3 = {}
        for i in data3:
            sub = dict(i)
            new = {cou: sub}
            records3.update(new)
            cou += 1
        # Check if the folder is deleted
        self.assertEqual(records[len(records) - 1]['name'], records3[len(records3) - 1]['name'])

    def test_6_delete_level1_dir_comfirm(self):
        '''
        Check if the delete funtion is available
        :return:
        '''
        # 连接 MongoDB 数据库
        client = MongoClient('000.000.000.000', 27017)
        db = client['xxxxx']
        db.authenticate("DB_User_Name", "DB_Password")  # 输入数据库的用户密码
        collection = db.folder  # 表名

        # 查询列表数据
        data = collection.find({'shopId': '4', 'type': 1})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records = {}
        for i in data:
            sub = dict(i)
            new = {cou: sub}
            records.update(new)
            cou += 1

        # Positioning the first record
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record).perform()  # move the mouse pointer on the record

        # Click delete button
        delete_button = self.obj.getElementObject(self.driver, 'filePage', 'deleteButton')
        delete_button.click()

        # Check if the content delete alert pop-up box is correct
        delete_alert = self.obj.getElementObject(self.driver, 'filePage', 'deleteAlert')
        delete_alert.is_displayed()  # 检查弹框是否显示

        # Click delete button
        confirm_delete_button = self.obj.getElementObject(self.driver,'filePage','deleteConfirmButton')
        confirm_delete_button.click()
        # time.sleep(2)

        # 验证弹框是否消失,数据是否删除
        from selenium.common.exceptions import StaleElementReferenceException
        try:
            delete_alert.is_displayed()
        except StaleElementReferenceException:
            print('弹框消失')
        else:
            raise customError('弹框没有消失,测试失败')

        # 查询列表数据
        data2 = collection.find({'shopId': '4', 'type': 1})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records2 = {}
        for i in data2:
            sub = dict(i)
            new = {cou: sub}
            records2.update(new)
            cou += 1
        # Check if the folder is deleted
        if records2[len(records2) - 1]['name'] == records[len(records) - 1]['name']:
            raise customError('删除一级目录失败了....')
        elif records2[len(records2) - 1]['name'] == records[len(records) - 2]['name']:
            print('删除成功')
        else:
            raise customError('删除成功了,但是数据不太对,请检查')

    def test_7_add_level2_dir_cancel(self):
        '''
        check add directory cancel funtion is available
        :return:
        '''
        #进入指定的一级目录下
        level1 = self.obj.getElementObject(self.driver, 'filePage', 'level1')
        level1.click()

        #click add directory button
        add_dir_button = self.obj.getElementObject(self.driver,'filePage','addDirButton')
        add_dir_button.click()

        #Type 'selenium' in the textbox and click cancel button
        add_dir_textbox = self.obj.getElementObject(self.driver,'filePage','addDirTextBox')
        add_dir_textbox.send_keys('selenium')
        cancel_add_button = self.obj.getElementObject(self.driver,'filePage','cancelAddButton')
        cancel_add_button.click()

        #positioning the name of first record
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record_name = models_list.find_element_by_xpath('div[1]/span[2]')

        #check if the cancelled add directory is saved.
        try:
            self.assertEqual(first_record_name.text,'selenium')
        except AssertionError:
            pass
        except Exception as e:
            print(traceback.print_exc())
        else:
            raise customError('放弃添加的文件夹竟然被保存了?')

    def test_8_add_level2_dir_confirm(self):
        '''
        check if the dirctory add funtion is available
        :return:
        '''

        # 进入指定的一级目录下
        level1 = self.obj.getElementObject(self.driver, 'filePage', 'level1')
        level1.click()

        # click add directory button
        add_dir_button = self.obj.getElementObject(self.driver, 'filePage', 'addDirButton')
        add_dir_button.click()

        # Type 'selenium' in the textbox and click confirm button
        add_dir_textbox = self.obj.getElementObject(self.driver, 'filePage', 'addDirTextBox')
        add_dir_textbox.send_keys('selenium')
        confirm_add_button = self.obj.getElementObject(self.driver, 'filePage', 'confirmAddButton')
        confirm_add_button.click()

        #Positioning the name of first record
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record_name = models_list.find_element_by_xpath('div[1]/span[2]')

        time.sleep(2)
        # Check if the directory has been created .
        try:
            self.assertEqual(first_record_name.text,'selenium')
        except AssertionError as e:
            print(traceback.print_exc())

    def test_9_rename_level2_dir_cancel(self):
        '''
        Check if rename of directory funtion is available
        :return:
        '''

        # 进入指定的一级目录下
        level1 = self.obj.getElementObject(self.driver, 'filePage', 'level1')
        level1.click()

        #Positioning the first record
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record_name = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record_name).perform() # move the mouse pointer on the record

        # Click Rename button
        rename_dir_button = self.obj.getElementObject(self.driver,'filePage','renameButton')
        rename_dir_button.click()

        #Type string 'selenium' in textbox
        rename_dir_textbox = self.obj.getElementObject(self.driver,'filePage','reNameTextBox')
        rename_dir_textbox.send_keys('rename')

        #Click cancel button to cancel the rename opera
        rename_dir_cancel = self.obj.getElementObject(self.driver,'filePage','cancelReNameButton')
        rename_dir_cancel.click()

        # check if the cancelled rename directory is saved.
        try:
            self.assertEqual(first_record_name.text, 'rename')
        except AssertionError:
            pass
        except Exception as e:
            print(traceback.print_exc())
        else:
            raise customError('放弃重命名的文件夹竟然被保存了?')

    def test_10_rename_level2_dir_confirm(self):
        '''
        Check if the rename directory funtion is available
        :return:
        '''

        # 进入指定的一级目录下
        level1 = self.obj.getElementObject(self.driver, 'filePage', 'level1')
        level1.click()

        # Positioning the first record
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record).perform()  # move the mouse pointer on the record

        # Click Rename button
        rename_dir_button = self.obj.getElementObject(self.driver, 'filePage', 'renameButton')
        rename_dir_button.click()

        # Type string 'selenium' in textbox
        rename_dir_textbox = self.obj.getElementObject(self.driver, 'filePage', 'reNameTextBox')
        rename_dir_textbox.send_keys('rename')

        # Click cancel button to cancel the rename opera
        rename_dir_confirm = self.obj.getElementObject(self.driver, 'filePage', 'confirmReNameButton')
        rename_dir_confirm.click()

        time.sleep(2)
        # Check if the directory has been renamed .
        first_record_name = first_record.find_element_by_xpath('//div[@class="ivu-checkbox-group"]/div[1]/span[2]')
        try:
            self.assertEqual(str(first_record_name.text), 'rename')
        except AssertionError:
            print(traceback.print_exc())

    def test_11_delete_level2_dir_cancel(self):
        '''
        Check if the delete cancel funtion is available
        :return:
        '''

        # 进入指定的一级目录下
        level1 = self.obj.getElementObject(self.driver, 'filePage', 'level1')
        level1.click()

        # 连接 MongoDB 数据库
        client = MongoClient('000.000.000.000', 27017)
        db = client['xxxxx']
        db.authenticate("DB_User_Name", "DB_Password")  # 输入数据库的用户密码
        collection = db.folder  # 表名

        # 查询列表数据
        data = collection.find({'shopId':'4','parentId':ObjectId("ObjectId")})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records = {}
        for i in data:
            sub = dict(i)
            new = {cou: sub}
            records.update(new)
            cou += 1

        # Positioning the first record
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record).perform()  # move the mouse pointer on the record

        # Click Rename button
        delete_button = self.obj.getElementObject(self.driver, 'filePage', 'deleteButton')
        delete_button.click()

        # Check if the content delete alert pop-up box is correct
        delete_alert = self.obj.getElementObject(self.driver, 'filePage', 'deleteAlert')
        delete_alert.is_displayed()  # 检查弹框是否显示

        delete_alert_title_range = self.obj.getElementObject(self.driver, 'filePage', 'deleteAlertTitle')
        delete_alert_title = delete_alert_title_range.find_element_by_xpath('s')
        self.assertEqual(delete_alert_title.text, '删除文件夹')  # 检查弹框标题是否正确

        # 检查弹出框的路径是否显示正确
        delete_alert_dir = self.obj.getElementObject(self.driver, 'filePage', 'deleteAlertDirectory')
        delete_alert_dir.is_displayed()  # 验证是否存在
        self.assertEqual(delete_alert_dir.find_element_by_xpath('span[1]').text, '全部>')  # 根目录验证
        self.assertEqual(delete_alert_dir.find_element_by_xpath('span[2]').text, 'Auto Test>')  # 一级目录验证
        self.assertEqual(delete_alert_dir.find_element_by_xpath('span[3]').text, 'rename')  # 二级目录验证


        delete_alert_text = self.obj.getElementObject(self.driver, 'filePage', 'deleteAlertText')
        self.assertEqual(delete_alert_text.text, '删除此(些)文件夹后，将无法恢复，文件夹内的所有内容会被一起删除，您是否确定删除？')  # 弹框文本校验

        # 第一种取消方式 : 点击关闭按钮
        close_button = delete_alert_title_range.find_element_by_xpath('span')
        close_button.click()
        # time.sleep(2)

        # 验证弹框是否消失,数据是否删除
        from selenium.common.exceptions import StaleElementReferenceException
        try:
            delete_alert.is_displayed()
        except StaleElementReferenceException:
            print('弹框消失')
        else:
            raise customError('弹框没有消失,测试失败')

        # 查询列表数据
        data2 = collection.find({'shopId':'4','parentId':ObjectId("ObjectId")})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records2 = {}
        for i in data2:
            sub = dict(i)
            new = {cou: sub}
            records2.update(new)
            cou += 1
        # Check if the folder is deleted
        self.assertEqual(records[len(records)-1]['name'],records2[len(records2)-1]['name'])

        #第二种方式
        first_record = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record).perform()
        delete_button.click()
        cancel_button = self.obj.getElementObject(self.driver, 'filePage', 'deleteCancelButton')
        cancel_button.click()  # 点击取消按钮

        # 检查弹框是否显示
        try:
            delete_alert.is_displayed()
        except StaleElementReferenceException:
            print('弹框消失')
        else:
            raise customError('弹框没有消失,测试失败')

        # 查询列表数据
        data3 = collection.find({'shopId':'4','parentId':ObjectId("ObjectId")})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records3 = {}
        for i in data3:
            sub = dict(i)
            new = {cou: sub}
            records3.update(new)
            cou += 1
        # Check if the folder is deleted
        self.assertEqual(records[len(records) - 1]['name'], records3[len(records3) - 1]['name'])

    def test_12_delete_level2_dir_comfirm(self):
        '''
        Check if the delete funtion is available
        :return:
        '''

        # 进入指定的一级目录下
        level1 = self.obj.getElementObject(self.driver, 'filePage', 'level1')
        level1.click()

        # 连接 MongoDB 数据库
        client = MongoClient('114.215.220.91', 27017)
        db = client['Bim-FM']
        db.authenticate("fmDevelop", "abcd1234!")  # 输入数据库的用户密码
        collection = db.folder  # 表名

        # 查询列表数据
        data = collection.find({'shopId':'4','parentId':ObjectId("ObjectId")})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records = {}
        for i in data:
            sub = dict(i)
            new = {cou: sub}
            records.update(new)
            cou += 1

        # Positioning the first record
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record).perform()  # move the mouse pointer on the record

        # Click delete button
        delete_button = self.obj.getElementObject(self.driver, 'filePage', 'deleteButton')
        delete_button.click()

        # Check if the content delete alert pop-up box is correct
        delete_alert = self.obj.getElementObject(self.driver, 'filePage', 'deleteAlert')
        delete_alert.is_displayed()  # 检查弹框是否显示

        # Click delete button
        confirm_delete_button = self.obj.getElementObject(self.driver,'filePage','deleteConfirmButton')
        confirm_delete_button.click()
        # time.sleep(2)

        # 验证弹框是否消失,数据是否删除
        from selenium.common.exceptions import StaleElementReferenceException
        try:
            delete_alert.is_displayed()
        except StaleElementReferenceException:
            print('弹框消失')
        else:
            raise customError('弹框没有消失,测试失败')

        # 查询列表数据
        data2 = collection.find({'shopId':'4','parentId':ObjectId("ObjectId")})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records2 = {}
        for i in data2:
            sub = dict(i)
            new = {cou: sub}
            records2.update(new)
            cou += 1
        # Check if the folder is deleted
        if records2[len(records2) - 1]['name'] == records[len(records) - 1]['name']:
            raise customError('删除一级目录失败了....')
        elif records2[len(records2) - 1]['name'] == records[len(records) - 2]['name']:
            print('删除成功')
        else:
            raise customError('删除成功了,但是数据不太对,请检查')


if __name__ == '__main__':
    unittest.main()

