# -*- coding: UTF-8 -*-
from uitrace.api import *
import pytest
import json 
# TODO: write your code

logger = get_logger()

class TestPhone(object):
    def setup_class(self):
        """
        每个测试类运行之前执行一次
        """
        #初始化设备驱动和环境，必填
        init_driver(workspace=os.path.dirname(__file__))
        #预先处理弹窗
        start_event_handler()
        #返回home页
        press(DeviceButton.HOME)

    def teardown_class(self):
        """
        每个测试类运行之后执行一次
        """
        time.sleep(1)
        press(DeviceButton.HOME)
        time.sleep(2)
        #生成报告
        stop_driver()
    
    def setup_method(self, method):
        """
        每个用例开始前初始化
        """
        #启动app
        pkg = "com.tencent.qqpimsecure"
        #uninstall_app(pkg)
        #install_app("/Users/quyuan/Downloads/demotest.apk")
        start_app(pkg, clear_data=True)
        #进入app腾讯管家首页
        exp_xpath = '//android.widget.Button[@text="马上体验"]'
        exp_res = double_click(loc=exp_xpath, by=DriverType.UI, timeout=5)
        assert exp_res == True
        agree_xpath = '//android.widget.TextView[@text="同意"]'
        click(loc=agree_xpath, by=DriverType.UI, timeout=3)
        time.sleep(3)
        ignore_xpath = '//android.widget.TextView[@text="忽略"]'
        click(loc=ignore_xpath, by=DriverType.UI, timeout=3)
        auth_xpath = '//android.widget.TextView[@text="去授权"]'
        click(loc=auth_xpath, by=DriverType.UI, timeout=3)
        allow_xpath = '//android.widget.Button[@text="始终允许"]'
        click(loc=allow_xpath, by=DriverType.UI, timeout=3)
        cancel_xpath = '//android.widget.Button[@text="取消"]'
        cancel_exist = find(cancel_xpath, timeout=20, by=DriverType.UI) is not None
        if cancel_exist:
            click(loc=cancel_xpath, by=DriverType.UI, timeout=3)

        return_ele = find('//android.widget.ImageView[@resource-id="com.tencent.qqpimsecure:id/mr"]', timeout=20, by=DriverType.UI) is not None
        if return_ele:
            click(loc='//android.widget.ImageView[@resource-id="com.tencent.qqpimsecure:id/mr"]', by=DriverType.UI, timeout=3)
    
    def teardown_method(self, method):
        """
        每个用例结束后执行
        """
        pass
    
    #@pytest.mark.skip()
    def test_fix_it_now(self):
        """
        立即修复
        """
        
        previous_score_list = ocr_driver.get_text(get_img())
        previous_score = previous_score_list[3][1][0]
        logger.warning(previous_score)
        logger.warning(json.dumps(previous_score_list, ensure_ascii=False))
        ele_exist = find('//android.widget.TextView[@text="立即修复"]', timeout=20, by=DriverType.UI) is not None
        if ele_exist:
            im_fix = double_click(loc='//android.widget.TextView[@text="立即修复"]', by=DriverType.UI, timeout=3)
            assert im_fix == True


        ele_exist = find('//android.widget.TextView[@text="继续优化"]', timeout=20, by=DriverType.UI) is not None
        time.sleep(60)
        if ele_exist:
            after_score_list = ocr_driver.get_text(get_img())
            after_score = after_score_list[2][1][0]
            logger.warning(after_score)
            logger.warning(json.dumps(after_score_list, ensure_ascii=False))
            assert int(previous_score) <= int(after_score)


    def test_detect_security(self):
        """
        安全检测
        """
        detect_ele = find('//android.widget.TextView[@text="安全检测"]', timeout=20, by=DriverType.UI) is not None
        if detect_ele:
            detect_ele_res = click(loc='//android.widget.TextView[@text="安全检测"]', by=DriverType.UI, timeout=3)
            assert detect_ele_res == True
        im_det = click('//android.widget.TextView[@text="立即检测"]', by=DriverType.UI, timeout=20)
        time.sleep(60)
        element = get_elements('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView', by=DriverType.UI)   
        logger.warning(element)
        res = element[0]["text"]
        assert res == "安全"


