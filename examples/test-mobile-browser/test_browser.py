# -*- coding: UTF-8 -*-
try:
    from uitrace.api import *
    import time
except:
    print("cannot import module runner")
    
logger = get_logger()


class TestGuard(object):
    def setup_class(self):
        """
        初始化
        """
        init_driver(workspace=os.path.dirname(__file__))
        start_event_handler()
        press(DeviceButton.HOME)

    def teardown_class(self):
        """
        stop driver
        """
        time.sleep(1)
        press(DeviceButton.HOME)
        time.sleep(2)
        stop_driver()

    def clear_data(self):
        start_app("com.android.settings")
        slide([0.459, 0.788], [0.52, 0.337], by=DriverType.POS)
        slide([0.459, 0.788], [0.52, 0.337], by=DriverType.POS)
        slide([0.459, 0.788], [0.52, 0.337], by=DriverType.POS)
        time.sleep(0.2)
        click('//android.widget.TextView[@text="应用管理"]', by=DriverType.UI, timeout=20)
        click('//android.widget.TextView[@text="应用列表"]', by=DriverType.UI, timeout=20)
        click('//android.widget.ImageView[@resource-id="com.android.settings:id/animated_search_icon"]', by=DriverType.UI, timeout=20)
        if find('//android.widget.ImageView[@resource-id="com.android.settings:id/search_close_btn"]', timeout=3, by=DriverType.UI) is not None:
            click(loc='//android.widget.ImageView[@resource-id="com.android.settings:id/search_close_btn"]', by=DriverType.UI, timeout=3)
        input_text("浏览器")
        click('//android.widget.TextView[@text="浏览器"]', by=DriverType.UI, timeout=20)
        click('//android.widget.TextView[@text="存储占用"]', offset=(0.4, 0.001), by=DriverType.UI, timeout=20)
        click('//android.widget.Button[@text="清除数据"]', by=DriverType.UI, timeout=5)
        if find('//android.widget.Button[@text="确定"]', by=DriverType.UI, timeout=5):
            click('//android.widget.Button[@text="确定"]', by=DriverType.UI, timeout=5)

    def setup_method(self, method):
        """
        用例开始前初始化
        """
        apps = app_list() 
        pkg = "com.heytap.browser"
        for app in apps:
            if app.find(pkg) < 0:
                print ("pkg not support")
        print ("pkg name", pkg)
        self.clear_data()

        start_app(pkg)
        time.sleep(2)
        if find('//android.widget.Button[@text="同意并使用"]', by=DriverType.UI, timeout=5):
            click('//android.widget.Button[@text="同意并使用"]', by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        else:
            pass

    def teardown_method(self, method):
        """
        用例结束后执行
        """
        pass

    def test_keyword_search(self):
        """
        关键字搜索
        """
        content = "oppo"
        self.enter_search(content)
        time.sleep(3)
        content_res = ocr_driver.search_from_img(get_img(), "OPPO")
        logger.warning(content_res)
        time.sleep(5)
        assert len(content_res) >= 1    

    def test_article_detail(self):
        """
        文章详情页
        """
        content = "https://open-hl.toutiao.com/a7094573200079716898/?utm_campaign=open&utm_medium=webview&utm_source=o_llq_api&req_id=202205201753430102100370241922B891&device_brand=&dt=PEMT00&gy=6d5fd107ea2c7a1371141e7c2dd3cbc09f1a04b0bccacf04657dea4c9de70a44c235e861850540cc665b1b67844dfdccba52f26272ef09ae4af8678aab0920a86ed3edf4b691355fd0de3836fdfa95dc89d26ead48725533b6926e02e757d62fbd255ca165fa63ff85e0d80601cea4281362c41cfad9ca0c17c108c05d80dbcc83bb03d01944eddd2575f0010c19ea45416bc7d130eea099045e9c24db57c7a9&crypt=1225&label=oppo_safe_channel&a_t=ALCgvvr9b5NLbjsE7c2dRHxz2Ed9p1Z8Z9qpRjwPCss1JYsQvHm1HfYGESfpKWHEpKihvpMen&item_id=7094573200079716898&__docId__=7094573200079716898&__barStyle__=1_1&__statParams__=sourceMedia&__fromId__=oppo_safe_channel&__source__=toutiao&sourceMedia=toutiao&__cmtCnt__=16&__styleType__=" 

        self.enter_search(content)
        
        #回复功能不可用
        # while True:       
        #     if find("回复", by=DriverType.OCR, timeout=2, is_regular=True):
        #        print ("回复功能不可用")
        #        break
        #   else:
        #        slide([0.483, 0.843], [0.541, 0.178], by=DriverType.POS)

    def test_reverso_video(self):
        """
        沉浸式视频
        """
        while True:
            ele_exist = find('//android.widget.TextView[@resource-id="com.heytap.browser:id/video_duration"]', timeout=20, by=DriverType.UI) is not None

            play_xpath = '//android.widget.ImageView[@resource-id="com.heytap.browser:id/icon_play"]'
            logger.warning(ele_exist)
            time.sleep(2)
            if ele_exist:
                video_button = click(play_xpath, by=DriverType.UI, timeout=20)      
                time.sleep(5) 
                assert video_button == True
                break
            else:
                slide(loc_from=(0.541, 0.43), loc_to=(0.541, 0.222), loc_shift=None, by=DriverType.POS, timeout=30, down_duration=0, up_duration=0, velocity=0.05)
                time.sleep(2)

        autor_xpath = '//android.widget.LinearLayout[@resource-id="com.heytap.browser:id/layout_publisher_view"]/android.widget.TextView[@resource-id="com.heytap.browser:id/tv_media_name"]'
        name_attr = get_elements(autor_xpath, by=DriverType.UI)
        name = ""
        while True: 
            if len(name_attr) > 0:
                name = name_attr[0]["text"]
                more_xpath = '//android.widget.LinearLayout[2]/android.widget.ImageButton[@resource-id="com.heytap.browser:id/btn_immersive_more"]'
                top_res = click(more_xpath, by=DriverType.UI, timeout=20)
                assert top_res == True
                not_interest = click('//android.view.ViewGroup[@resource-id="com.heytap.browser:id/GridView"]/android.widget.LinearLayout[@resource-id="com.heytap.browser:id/small_more_dislike"]', by=DriverType.UI, timeout=20)
                assert not_interest == True
                res = click('//android.widget.LinearLayout[@resource-id="com.heytap.browser:id/text_wrapper"]/android.widget.TextView[@text="不想看该作者" and @resource-id="com.heytap.browser:id/text1"]', by=DriverType.UI, timeout=20)
                assert res == True
                time.sleep(2)
                autor_name_xpath = '//android.widget.TextView[@text="%s" and @resource-id="com.heytap.browser:id/tv_media_name"]' % name
                autor_name_res = find(autor_name_xpath, timeout=20, by=DriverType.UI) is not None    
                logger.warning(autor_name_xpath)
                logger.warning(autor_name_res)
                assert autor_name_res != True
                break
            else:
                slide(loc_from=(0.541, 0.551), loc_to=(0.541, 0.222), loc_shift=None, by=DriverType.POS, timeout=30, down_duration=0, up_duration=0, velocity=0.5)
                time.sleep(2)

    def test_change_channel(self):
        """
        频道切换
        """
        rec_xpath = '//android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.TextView[@text="推荐"]'
        rec_res = click(rec_xpath, duration=2, by=DriverType.UI)
        assert rec_res == True
        time.sleep(3)
        pos_from = [0.236, 0.186]
        slide_pos(pos_from=pos_from, pos_to=[0.650, 0.186], pos_shift=None, down_duration=0,   up_duration=0, velocity=0.01)
        top_xpath = '//android.widget.TextView[@text="置顶"]'
        time.sleep(2)
        top_article = find(top_xpath, timeout=20, by=DriverType.UI) is not None
        if top_article:
            top_res = click(loc=top_xpath, by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
            assert top_res == True
        

    def test_video_detail(self):
        """
        视频详情
        """
        url = "https://opdwz.cn/AjqUzuy?from=videoDetail"
        self.enter_search(url)
        time.sleep(3)
        #暂停
        click_pos((0.505, 0.156), duration=0.1, times=2)
        time.sleep(1)
        #恢复播放
        click_pos((0.505, 0.156), duration=0.1, times=1)
        time.sleep(2)
        #进入倍度
        click_pos((0.505, 0.156), duration=0.1, times=2)
        #点击倍速
        speed_xpath = '//android.widget.TextView[@text="倍速" and @resource-id="com.heytap.browser:id/portrait_panel_text"]'
        while True:
            speed_flag = find(speed_xpath, timeout=20, by=DriverType.UI) is not None    
            if speed_flag:
                speed_res = click(speed_xpath, by=DriverType.UI, timeout=30)
                assert speed_res == True
                # 1.5倍速
                half_res = click('//android.widget.FrameLayout[@resource-id="com.heytap.browser:id/portrait_play_speed"]/android.widget.TextView[@text="1.5X" and @resource-id="com.heytap.browser:id/portrait_panel_text"]', by=DriverType.UI, timeout=20)
                assert half_res == True
                #2.0倍速
                two_res = click('//android.widget.FrameLayout[@resource-id="com.heytap.browser:id/portrait_play_speed"]/android.widget.TextView[@text="2.0X" and @resource-id="com.heytap.browser:id/portrait_panel_text"]', by=DriverType.UI, timeout=20)
                assert  two_res == True
                #1.0倍速
                xpath = '//android.widget.FrameLayout[@resource-id="com.heytap.browser:id/portrait_play_speed"]/android.widget.TextView[@text="1.0X" and @resource-id="com.heytap.browser:id/portrait_panel_text"]'
                one_res = find_ui(xpath, timeout=30)
                print("one_res", one_res)
                assert len(one_res) != 0
                break
            else:
                click_pos((0.505, 0.156), duration=0.1, times=2)


    def enter_search(self, content):
        """
        进入搜索
        """
        enter_search = click('//android.widget.ImageView[@resource-id="com.heytap.browser:id/search_icon"]', duration=2, by=DriverType.UI)
        assert enter_search == True
        time.sleep(1)
        res = cmd_adb("shell \"am broadcast -a ADB_INPUT_TEXT --es msg '%s'\"" % content)
        logger.warning(res)
        time.sleep(5)
        press(66)
        time.sleep(5)
