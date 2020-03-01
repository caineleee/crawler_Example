#!/usr/bin/python
#coding=utf-8

from browser_driver.ui.call.public.loginAndout import *
from browser_driver.ui.call.public.upload_model import upload_file
from browser_driver.ui.call.public.enter_test_dir import *
from browser_driver.ui.call.public.custom_error import customError
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from pymongo import MongoClient
from bson.objectid import ObjectId
import unittest,random,os,time


'''
test scripts of directories operation 
'''


class file_opera(unittest.TestCase):

    def setUp(self):

        '''
        1. login to seleinum3_UI_test by call login() method
        2. choose '优服内测' project for data source by call project_choose() method
        :return:
        '''

        login(self)
        project_choose(self)

    def tearDown(self):

        '''
        logout the system by call logout() method
        :return:
        '''

        logout(self)

    def test_1_upload(self):

        '''
        enter 'auto test -> Ranamed1' directory and then call the upload() method
        to upload a random rvt model in the system to  if test the upload funtion is available
        :return:
        '''

        #进入到指定目录
        enter_test_dir(self)

        #调用上传模型函数
        upload_file.upload(self)


    def test_2_upload_cancel(self):

        '''
        check if the cancel upload funtion is available
        :return:
        '''
        enter_test_dir(self)

        # 文件路径
        path = '/Users/billylee/Documents/rvt'

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
        file = files[choose]
        print('文件名是:  ', file)

        # 上传上面选取的文件
        uploadButton = self.obj.getElementObject(self.driver, 'filePage', 'uploadButton')
        uploadButton.send_keys(path + '/' + file)  # 上传随机的一个文件

        # 显示等待模型上传中组件
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.obj.getElementObject(self.driver,'filePage','uploadingFile')))

        # 定位模型上传统计组件
        uploadingCount = self.obj.getElementObject(self.driver, 'filePage', 'uploadingCount')

        # 判断当前模型上传的状态是否正确,如果正确就点击取消上传按钮,否则报错
        if uploadingCount.text == '正在上传：1':

            #点击取消上传按钮
            cancel_upload = self.obj.getElementObject(self.driver, 'filePage', 'cancelUpload')
            cancel_upload.click()
            print('当前上传总数是:  ',uploadingCount.text)
            time.sleep(2)

            #检查是否取消成功
            self.assertTrue(uploadingCount.text,'正在上传：0')
            EC.invisibility_of_element_located(upload_file)

        elif uploadingCount.text == '正在上传：0':
            print('当前上传总数是:  ', uploadingCount.text)
            raise customError('上传的模型数据哪儿去了? ')
        else:
            print('当前模型上传的个数是: ', uploadingCount.text)
            raise customError('为什么不是一条数据? 哪儿来的数据?')


    def test_3_rename_model_cancel(self):

        '''
        check if the rename cancecl funtion is available
        :return:
        '''

        # 连接 MongoDB 数据库
        client = MongoClient('000.000.000.000', 27017)
        db = client['xxxxx']
        db.authenticate("DB_User_Name", "DB_Password")  # 输入数据库的用户密码
        collection = db.FmFile  # 表名

        # 查询列表数据
        data = collection.find({'folderId': ObjectId("ObjectId"),
                                'url': {'$exists': 'true'}, 'deleted': 0})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records = {}
        for i in data:
            sub = dict(i)
            new = {cou: sub}
            records.update(new)
            cou += 1

        #进入指定测试路径
        enter_test_dir(self)

        #鼠标悬浮在第一条数据上
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record).perform()

        #第一条数据的文件名
        first_file_name = first_record.find_element_by_xpath('span[2]')

        #检查重命名按钮是否出现
        rename_button = self.obj.getElementObject(self.driver,'filePage','renameButton')
        rename_button.is_displayed()

        #点击重命名按钮
        rename_button.click()

        #验证组件是否存在并输入修改的内容
        reNameTextBox = self.obj.getElementObject(self.driver,'filePage','reNameTextBox')
        reNameTextBox.is_displayed()
        reNameTextBox.clear()
        reNameTextBox.send_keys('ReNamed')

        #点击取消修改按钮
        cancel_rename_button = self.obj.getElementObject(self.driver,'filePage','cancelReNameButton')
        cancel_rename_button.click()

        #验证数据是否显示一致
        self.assertTrue(first_file_name,records[len(records)-1]['name'])

    def test_4_rename_model_confirm(self):
        '''
        check if the rename funtion is available
        :return:
        '''

        # 进入指定测试路径
        enter_test_dir(self)

        # 鼠标悬浮在第一条数据上
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record).perform()

        # 第一条数据的文件名
        first_file_name = first_record.find_element_by_xpath('span[2]')

        # 检查重命名按钮是否出现
        rename_button = self.obj.getElementObject(self.driver, 'filePage', 'renameButton')
        rename_button.is_displayed()

        # 点击重命名按钮
        rename_button.click()

        # 验证组件是否存在并输入修改的内容
        reNameTextBox = self.obj.getElementObject(self.driver, 'filePage', 'reNameTextBox')
        reNameTextBox.is_displayed()
        reNameTextBox.clear()
        reNameTextBox.send_keys('ReNamed')

        # 点击取消修改按钮
        confirm_rename_button = self.obj.getElementObject(self.driver, 'filePage', 'confirmReNameButton')
        confirm_rename_button.click()

        # 连接 MongoDB 数据库
        client = MongoClient('000.000.000.000', 27017)
        db = client['xxxx']
        db.authenticate("DB_User_Name", "DB_Password")  # 输入数据库的用户密码
        collection = db.FmFile  # 表名

        # 查询列表数据
        data = collection.find({'folderId': ObjectId("ObjectId"),
                                'url': {'$exists': 'true'}, 'deleted': 0})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records = {}
        for i in data:
            sub = dict(i)
            new = {cou: sub}
            records.update(new)
            cou += 1

        # 验证数据是否显示一致
        self.assertTrue(first_file_name, 'ReNamed')
        self.assertTrue(records[len(records) - 1]['name'],'ReNamed')

    def test_5_delete_model_cancel(self):
        '''
        check if the cancel delete funtion is available
        :return:
        '''

        # 连接 MongoDB 数据库
        client = MongoClient('000.000.000.000', 27017)
        db = client['xxxxxx']
        db.authenticate("DB_User_Name", "DB_Password")  # 输入数据库的用户密码
        collection = db.FmFile  # 表名

        # 查询列表数据
        data = collection.find({'folderId': ObjectId("ObjectId"),
                                'deleted': 0})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records = {}
        for i in data:
            sub = dict(i)
            new = {cou: sub}
            records.update(new)
            cou += 1

        # 进入指定测试路径
        enter_test_dir(self)

        # 鼠标悬浮在第一条数据上
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record).perform()

        # 检查删除按钮是否出现
        delete_button = self.obj.getElementObject(self.driver, 'filePage', 'deleteButton')
        delete_button.is_displayed()

        # 点击删除按钮
        delete_button.click()

        # 检查删除弹框内容是否显示正确
        delete_alert = self.obj.getElementObject(self.driver, 'filePage', 'deleteAlert')
        delete_alert.is_displayed()   #检查弹框是否显示

        delete_alert_title_range = self.obj.getElementObject(self.driver,'filePage','deleteAlertTitle')
        delete_alert_title = delete_alert_title_range.find_element_by_xpath('s')
        self.assertEqual(delete_alert_title.text,'删除文件') #检查弹框标题是否正确

        #检查弹出框的路径是否显示正确
        delete_alert_dir = self.obj.getElementObject(self.driver,'filePage','deleteAlertDirectory')
        delete_alert_dir.is_displayed() #验证是否存在
        self.assertEqual(delete_alert_dir.find_element_by_xpath('span[1]').text,'全部>') #根目录验证
        self.assertEqual(delete_alert_dir.find_element_by_xpath('span[2]').text, 'Auto Test>') #一级目录验证
        self.assertEqual(delete_alert_dir.find_element_by_xpath('span[3]').text, 'ReNam1>') #二级目录验证
        self.assertEqual(delete_alert_dir.find_element_by_xpath('span[4]').text, 'ReNamed.rvt')  #文件名验证

        delete_alert_text = self.obj.getElementObject(self.driver,'filePage','deleteAlertText')
        self.assertEqual(delete_alert_text.text,'删除此(些)文件后，将无法恢复，您是否确定删除？') #弹框文本校验

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

        data2 = collection.find({'folderId': ObjectId("ObjectId"),
                                'deleted': 0})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records2 = {}
        for i in data2:
            sub = dict(i)
            new = {cou: sub}
            records2.update(new)
            cou += 1
        self.assertEqual(len(records2),len(records))  #检查数据是否被删除


        #第二种取消方式

        # 点击删除按钮
        first_record = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record).perform()
        delete_button.click()
        cancel_button = self.obj.getElementObject(self.driver,'filePage','deleteCancelButton')
        cancel_button.click()  #点击取消按钮

        #检查弹框是否显示
        try:
            delete_alert.is_displayed()
        except StaleElementReferenceException:
            print('弹框消失')
        else:
            raise customError('弹框没有消失,测试失败')

        #验证数据是否发生变化
        data3 = collection.find({'folderId': ObjectId("ObjectId"),
                                'deleted': 0})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records3 = {}
        for i in data3:
            sub = dict(i)
            new = {cou: sub}
            records3.update(new)
            cou += 1
        self.assertEqual(len(records3),len(records))  #检查数据是否被删除

    def test_6_delete_model_confirm(self):
        '''
        check if the delete funtion is available
        :return:
        '''

        # 连接 MongoDB 数据库
        client = MongoClient('000.000.000.000', 27017)
        db = client['XXXXX']
        db.authenticate("DB_User_Name", "DB_Password")  # 输入数据库的用户密码
        collection = db.FmFile  # 表名

        # 查询列表数据
        data = collection.find({'folderId': ObjectId("ObjectId"),
                                'deleted': 0})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records = {}
        for i in data:
            sub = dict(i)
            new = {cou: sub}
            records.update(new)
            cou += 1

        # 进入指定测试路径
        enter_test_dir(self)

        # 鼠标悬浮在第一条数据上
        models_list = self.driver.find_element_by_xpath('//div[@class="ivu-checkbox-group"]')
        first_record = models_list.find_element_by_xpath('div[1]')
        ActionChains(self.driver).move_to_element(first_record).perform()

        # 检查删除按钮是否出现
        delete_button = self.obj.getElementObject(self.driver, 'filePage', 'deleteButton')
        delete_button.is_displayed()

        # 点击删除按钮
        delete_button.click()

        # 检查删除弹框内容是否显示正确
        delete_alert = self.obj.getElementObject(self.driver, 'filePage', 'deleteAlert')
        delete_alert.is_displayed()  # 检查弹框是否显示

        confirm_button = self.obj.getElementObject(self.driver, 'filePage', 'deleteConfirmButton')
        confirm_button.click()  # 点击取消按钮

        # 检查弹框是否显示
        from selenium.common.exceptions import StaleElementReferenceException
        try:
            delete_alert.is_displayed()
        except StaleElementReferenceException:
            print('弹框消失')
        else:
            raise customError('弹框没有消失,测试失败')

        time.sleep(5) #等几秒,让数据库反映反映....

        # 验证数据是否发生变化
        data2 = collection.find({'folderId': ObjectId("ObjectId"),
                                 'deleted': 0})

        # 把数据库查询结果转换成字典形式
        cou = 0
        records2 = {}
        for i in data2:
            sub = dict(i)
            new = {cou: sub}
            records2.update(new)
            cou += 1

        #打印数据库两次的查询结果的遍历对比
        print('records : '+str(len(records)),' ======>records2 : '+str(len(records2)))
        for i in range(len(records)-1):
            print('Records %d : '%(i),records[i])
            try:
                print('Records2 %d : '%(i), records2[i])
            except Exception:
                print('Records2 已经没有更多的数据了')


        try:
            self.assertEqual(len(records2), len(records))  # 检查数据是否被删除
        except AssertionError:
            print('数据发生变化,验证通过')
        else:
            raise customError('数据没有发生变化,有问题需要检查')

        #由于每次删除的都是第一条(修改文件名后的文件都教 ReNamed),
        #一般情况只要 ReNamed文件名不存在数据库中就算是删除成功了
        if 'ReNamed' in records2.values():
            raise customError('rename 文件依然存在,请检查数据是否被删除')
        else:
            print('The rvt file has been deleted!')



if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    #
    # suite.addTest(file_opera('test_upload'))
    # suite.addTest(file_opera('test_cancel_upload'))
    # suite.addTest(file_opera('test_rename_model_cancel'))
    # suite.addTest(file_opera('test_rename_model_confirm'))
    # suite.addTest(file_opera('test_delete_model_cancel'))
    # suite.addTest(file_opera('test_delete_model_confirm'))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)