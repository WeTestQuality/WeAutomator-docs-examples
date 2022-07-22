# -*- coding: UTF-8 -*-
from uitrace.api import *
import pytest

# TODO: write your code
def setup_module():
    '''
    在整个文件开始前执行一次
    '''
    # 初始化设备驱动和环境
    init_driver(workspace=os.path.dirname(__file__))

    # 预先处理系统弹窗
    start_event_handler()

    # 按下Home键，让手机初始界面为Home页面
    press(DeviceButton.HOME)

def teardown_module():
    '''
    在整个文件执行后执行一次
    '''
    # 测试用例执行完后，回到初始手机界面--Home页面
    press(DeviceButton.HOME)
    time.sleep(2)

    # 释放驱动，生成报告
    stop_driver()


def setup_function():
    '''
    每个测试函数执行前执行一次
    '''
    pass

def teardown_function():
    '''
    每个测试函数执行后执行一次
    '''
    pass

def test_case1():
    '''
    测试用例1
    '''

def test_case2():
    '''
    测试用例2
    '''
    pass
