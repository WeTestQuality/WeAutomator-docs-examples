# -*- coding: UTF-8 -*-
from uitrace.api import *
import pytest

# TODO: write your code
class TestClass:
    def setup_class(self):
        '''
        在测试类执行之前执行一次
        '''
        # 初始化设备驱动和环境
        init_driver(workspace=os.path.dirname(__file__))

        # 预先处理系统弹窗
        start_event_handler()

        # 按下Home键，让手机测试前的初始化界面为Home页面
        press(DeviceButton.HOME)

    def teardown_class(self):
        '''
        在测试类运行结束后运行
        '''
        # 退回到手机的Home页面
        press(DeviceButton.HOME)

        # 释放驱动，生成报告
        stop_driver()

    def setup_method(self):
        '''
        类中每个测试用例开始前执行
        '''
        pass
    
    def teardown_method(self):
        '''
        类中每个测试用例结束后执行
        '''
        pass
    
    def test_case1(self):
        '''
        测试用例1
        '''
        pass
    
    def test_case2(self):
        '''
        测试用例2
        '''
        pass