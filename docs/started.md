# WeAutomator入手教程-以安卓系统、pytest框架为例
1. 连接安卓设备
![image](https://user-images.githubusercontent.com/102640628/175203791-4fb34bd7-31ab-4879-8afd-4e76773efc7a.png)
2. pytest组织用例
- 主脚本区域编写main.py，完成调试：
```python
# -*- coding: UTF-8 -*-
import pytest
from uitrace.api import *
import json
logger = get_logger()
class TestPhone(object):
    def setup_class(self):
        """
        每个测试类运行之前执行一次,初始化类
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
        press(DeviceButton.HOME)
        stop_driver()

    def setup_method(self, method):
        """
        每个用例开始前初始化
        """
        #启动app
        pkg = "com.tencent.qqpimsecure"
        uninstall_app(pkg)
        #安卓app,app_path填写app本地路径
        install_app(app_path)
        #启动app，清理上一次遗留的数据
        start_app(pkg, clear_data=True)

    def teardown_method(self, method):
        """
        每个用例结束后执行
        """
        pass

    def test_case_1(self):
        """
        测试case 1 
        """
        pass
        #打印日志
        logger.info(res)

    def test_case_2(self):
        """
        测试case 2
        """
        pass
pytest_main([os.path.join(os.path.dirname(__file__), "main.py")])
```
3. 新建测试文件，命名如test_phoneguard.py
- 将main.py的内容复制到test_phoneguard.py
![image](https://user-images.githubusercontent.com/102640628/175204165-6329fc0e-4018-486f-b642-1b51fc17bc7a.png)
4. 修改入口文件main.py
main.py的内容改为：
```python
# -*- coding: UTF-8 -*-
from uitrace.api import *
pytest_main([os.path.join(os.path.dirname(__file__), "test_phoneguard.py")])
```
5. 将调试通过的脚本后导出zip包，提交到用例管理
![image](https://user-images.githubusercontent.com/102640628/175204282-685eab55-29bd-4641-b836-37bfa9e5c1dc.png)

6. 参考的demo用例：
    https://github.com/WeTestQuality/WeAutomator-docs-examples/tree/main/examples/test-phone-guard

