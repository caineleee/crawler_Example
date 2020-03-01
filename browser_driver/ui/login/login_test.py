#!/usr/bin/python
#coding=utf-8

import unittest
from browser_driver.ui.call.public.loginAndout import logout,login
class haha(unittest.TestCase):
    def setUp(self):
        login(self)

    def test_hehe(self):
        logoTop = self.obj.getElementObject(self.driver, 'login', 'logoTop')
        logoTop.is_displayed()


    def tearDown(self):
        logout(self)
