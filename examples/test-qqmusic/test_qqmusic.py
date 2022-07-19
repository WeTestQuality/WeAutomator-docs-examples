# -*- coding: UTF-8 -*-
# test_simple.py

import pytest
# 提交pytest功能测试必须用try-except
try:
    from uitrace.api import *
except:
    print("cannot import module runner")

qq_pkg = "com.tencent.mobileqq"
qq_music_pkg = "com.tencent.mobileqq"

class TestMusic:
    def setup_class(self):
        '''
        测试类开始执行前执行一次
        '''
        # 初始化设备驱动和环境
        init_driver(workspace=os.path.dirname(__file__))
        # 预先处理系统弹窗
        start_event_handler()
        # 初始界面为手机Home界面
        press(DeviceButton.HOME)
        # 登录手机QQ
        self.qq_login()
        press(DeviceButton.HOME)
    
    def teardown_class(self):
        '''
        测试类结束执行时执行一次
        '''
        # 回到初始界面
        press(DeviceButton.HOME)
        # 关闭相关应用
        stop_app(qq_pkg)
        stop_app(qq_music_pkg)

        time.sleep(2)
        # 释放相关驱动，生成报告
        stop_driver()
    
    def setup_method(self):
        '''
        每个测试用例执行前执行一次
        '''
        # 打开应用
        start_app(qq_music_pkg)

        # 点击“首页”选项
        click([0.112, 0.956], by=DriverType.POS, duration=0.05)
        time.sleep(2)
    
    def teardowm_method(self):
        '''
        每个测试用例执行后执行一次
        '''
        time.sleep(2)

    def test_login_by_qq(self):
        '''
        使用qq登录qq音乐
        '''
        # 点击“我的”选项
        click("obj_1658128095776.jpg", by=DriverType.CV, timeout=30)
        # 点击“登录”
        click("obj_1658128118888.jpg", by=DriverType.CV, timeout=30)
        # 点击“用QQ”登录
        click("obj_1658213995181.jpg", by=DriverType.CV, timeout=30)
        # 勾选“隐私条例”
        click([0.238, 0.523], by=DriverTypes.POS, duration=0.05)
        # 点击“同意”
        click([0.462, 0.232], by=DriverType.POS, duration=0.05)
        # 点击“确认”
        click([0.562, 0.847], by=DriverType.POS, duration=0.05)
        time.sleep(2)
        # 设定完成登录判断标准
        content = '我的'
        content_res = ocr_driver.search_from_img(get_img(), content)
        assert len(content_res) >= 1
    
    def test_search_for_music(self):
        '''
        使用搜索栏搜索
        '''
        # 点击“搜索栏”
        click([0.45, 0.131], by=DriverType.POS, duration=0.05)
        input_text("周杰伦")
        # 点击“播放”
        click("obj_1658214638460.jpg", by=DriverType.CV, timeout=30)
        ele_exit = find("obj_1658214638460.jpg", by=DriverType.CV, timeout=20) is not None
        assert ele_exit == True
        time.sleep(10)
        stop_play_path = '//android.widget.RelativeLayout[@resource-id="com.tencent.qqmusic:id/dtm"]/android.widget.FrameLayout[@resource-id="com.tencent.qqmusic:id/fc0"]'
        # 暂停播放
        click(stop_play_path, by=DriverType.UI, timeout=20)
        back_path = '//android.widget.LinearLayout[@resource-id="com.tencent.qqmusic:id/ad9"]/android.widget.RelativeLayout[@resource-id="com.tencent.qqmusic:id/csb"]'
        # 回到qq音乐主界面
        click(back_path, by=DriverType.UI, timeout=20)

    def test_clear_data(self):
        '''
        测试qq音乐清除缓存
        '''
        # 点击“我的”选项
        click("obj_1658128095776.jpg", by=DriverType.CV, timeout=30)
        setting_path = '//android.view.ViewGroup[@resource-id="com.tencent.qqmusic:id/ejv"]/android.widget.ImageView[@resource-id="com.tencent.qqmusic:id/ad2"]'
        # 点击“设置”
        click(setting_path, by=DriverType.UI, timeout=20)
        # 点击“清理占用控件”
        click('//android.widget.RelativeLayout[15]/android.widget.LinearLayout[@resource-id="com.tencent.qqmusic:id/doy"]', by=DriverType.UI, timeout=20)
        # 等待缓存计算
        time.sleep(5)
        # 点击“一键清理”
        data_clear = click("obj_1658215687122.jpg", by=DriverType.CV, timeout=30)
        assert data_clear == True
        # 等待清理完毕
        time.sleep(10)
        # 回到qq音乐主界面
        click('//android.widget.RelativeLayout[@resource-id="com.tencent.qqmusic:id/csb"]/android.widget.ImageView[@resource-id="com.tencent.qqmusic:id/pr"]', by=DriverType.UI, timeout=20)
        
    def qq_login(self):
        # 启动QQ
        start_app("com.tencent.mobileqq")
        # 点击“登录”，进入输入账号密码界面
        click("obj_1658115076269.jpg", by=DriverType.CV, timeout=30)
        time.sleep(2)
        # 点击“输入账号”输入框
        click([0.514, 0.285], by=DriverType.POS, duration=0.05)
        # 输入QQ账号
        input_text("QQ账号")
        time.sleep(1)
        # 点击“输入密码”输入框
        click([0.526, 0.33], by=DriverType.POS, duration=0.05)
        # 输入密码
        input_text("QQ密码")
        # 勾选相关隐私选项
        click([0.231, 0.397], by=DriverType.POS, duration=0.05)
        # 验证登录
        click([0.498, 0.495], by=DriverType.POS, duration=0.05)

