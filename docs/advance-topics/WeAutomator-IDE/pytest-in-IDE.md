# 在WeAutomator IDE中用pytest组织测试用例  
在IDE中，不仅可以编写简单的脚本去操作手机，还可以编写用pytest组织的测试用例，用于后续提交到终端云测平台，使用云真机测试。  
## 1. pytest框架介绍  
pytest是一个非常成熟的全功能的Python测试框架，主要特点有以下几点：  
- 非常容易上手，入门简单，文档丰富。文档中有很多实例可以参考
- 能够支持简单的单元测试和复杂的功能测试
- 支持参数化
- 执行测试过程中可以将某些测试跳过，或者对某些预期失败的case标记成失败
- 支持重复执行失败的case
- 支持运行由nose，unittset编写的测试case 
- 具有很多第三方插件，并且可以自定义扩展

详细的pytest学习资料可以参考[Pytest使用手册](https://learning-pytest.readthedocs.io/zh/latest/index.html) 
### 1) 默认的用例识别规则  
- 用例文件：所有文件名为`test_`开头或者`_test`开头的文件会被识别为用例文件 
- 用例类：测试文件中每个`Test`开头的类就是一个测试用例类
- 测试用例：测试类中每个`test`开头的方法就是一条测试用例，测试文件中每个`test`开头的函数也是一条测试用例
- pytest兼容unittest，以unittest规范编写的用例，pytest也可以识别。 

通过上述的了解，可以知道pytest支持函数形式和类形式的测试用例。 现分别做简单介绍。 

### 2）函数形式编写用例  
测试文件中的测试函数需要以`test`开头，不正确的命名会导致无法测试。  
```python
# \pytest-cases\test_demo1.py
import pytest

def test_case1():
    assert 1 == 2

def test_case2():
    assert 1 == 1

if __name__ == '__main__':
    pytest.main(['-v'])
```

我们可以在编译器里面直接运行，或者在命令行里面调用pytest命令运行。  
示例里涉及断言`assert`语句，在pytest中，`assert`是编写测试的最基础工具。如:  
```python
assert a == b
assert a <= b
```
`assert`的具体语法可以参考[assert statement](https://docs.python.org/3/reference/simple_stmts.html?highlight=assert#grammar-token-assert_stmt)  
示例中还涉及pytest的运行参数`-v`，更多参数可以通过`pytest -h`查看，或者参考[pytest运行参数](https://www.jianshu.com/p/979d68aee236)  

### 3) 以类的形式编写用例  
测试文件中的测试类需要以`Test`开头，类中的测试用例需要以`test`开头  
```python
# \test-cases\test_demo2.py
class TestClass:
    def test_func1(self):
        assert 1 == 1
    def test_func2(self):
        assert 2 == 1
```

在编写pytest测试用例时，经常会使用pytest中的`setup`和`teardown`测试固件, 去做一些初始化和清除工作，如：
```python
class TestClass:
    def setup(self):
        print('setup: 测试用例开始执行')

    def teardown(self):
        print('teardown: 测试用例结束执行')
    
    def test_func1(self):
        print('test_func1开始测试')
        assert 1 == 1
    
    def test_func2(self):
        print('test_func2开始测试')
        assert 2 == 1
```
在命令行运行
```
pytest test_demo2.py -s
```
执行结果简略展示如下。
```
setup: 测试用例开始执行
test_func1开始测试
.teardown: 测试用例结束执行
setup: 测试用例开始执行
test_func2开始测试
Fteardown: 测试用例结束执行
```
在该种情况下，每次执行类中的测试用例，都会在测试用例执行前、执行后分别调用类中定义的`setup()`和`teardown()`方法。上面显示的结果中，在`teardown()`方法输出语句前出现的`.`和`F`，是由当前
测试用例执行成功和失败引起的。  

更多的详情可参考[pytest测试用例之setup与teardown方法(一)](https://cloud.tencent.com/developer/article/1657959?from=10680)、[pytest测试用例之setup与teardown方法(二)](https://cloud.tencent.com/developer/article/1658959?from=article.detail.1657959)   


## 2. IDE中使用pytest组织测试用例  
WeAutomator IDE支持在工程内使用pytest形式编写测试脚本。  
我们打开WeAutomator IDE，选择代码模式，建立工程，进入IDE界面后，连接手机，得到如下初始化界面，我们将在主脚本区域编写pytest形式的脚本。  
![figure](image/pytest-init.png)  
初始化的主脚本如下。
```python
# -*- coding: UTF-8 -*-
from uitrace.api import *

init_driver(workspace=os.path.dirname(__file__))
# TODO: write your code

stop_driver()
```

我们可以在初始化脚本的基础上组织测试用例，IDE中使用pytest组织测试用例通常采用以下模式。
```python
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


pytest_main([os.path.join(os.path.dirname(__file__), "main.py")])
```
我们需要导入pytest第三方库，在编写脚本过程中可以充分利用IDE提供的功能，实现快速编写脚本。  
我们使用pytest组织测试类的时候，如上面的`TestClass`测试类，可以使用`setup_class()`方法进行测试类的初始化，包括初始化设备、处理系统弹窗等，使用`teardown_class()`方法
进行释放资源等操作。`setup_class()`方法会在每个测试类运行前执行一次，`teardown_class()`方法会在每个测试类结束运行后执行。运用好这两个方法可以帮助我们做好测试的初始化和清理工作。
示例中同样使用了`setup_method()`和`teardown_method()`方法，`setup_method()`方法会在执行类中每个测试用例之前执行一次，可以在每个测试用例运行前进行统一的操作，包括跳回到统一页面、
记录运行测试用例前的数据等等，`teardown_method()`方法会在测试类中每个测试用例结束后执行一次，可以在每个测试用例运行后进行统一操作，包括清理空间，记录数据，显示报告等。合理使用以上方法，
可以让我们写出逻辑清楚，结构明朗的测试用例。   
|        固件                       |               解释                  |
| :------------------------------: | :---------------------------------: |
| setup_module/teardown_module     | 用于模块的始末，只执行一次，是一个全局方法 |
| setup_function/teardown_function | 只对函数生效，不在类中使用              |
| setup_class/teardown_class       | 在类中使用，在类开始、结束时执行         |
| setup_method/teardown_method     | 在类中的方法开始和结束处执行            |
| setup/teardown                   | 在调用方法的前后执行                   |



接下来我们将通过示例来展示如何在IDE中使用pytest框架组织测试用例。  

### 示例1 
示例我们将展示如何在WeAutomator IDE中使用pytest组织测试用例，完成登录手机QQ的测试。在示例1中，我们
将展示**函数形式编写用例**和**类的形式编写用例**的常见思路，意在通过本示例帮助使用者了解构建测试用例的逻辑。
#### 1）函数形式组织测试用例
我们将展示如何使用函数形式组织测试用例，完成QQ的登录。*这里我们较多使用基于位置坐标的点击操作，不同的手机可能存在一定的差别，如果该程序在你的电脑上无法完成预期目标，
请考虑是不是由于手机设备型号版本不同造成的*。使用者可根据实际情况选择合适的点击操作，不做强求，同时要配合IDE强大的功能完成代码编写，提交效率，可参见[IDE主交互界面](IDE-interface.md)。
```python
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


def test_login_qq():
    '''
    测试用例：QQ登录
    '''

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
    time.sleep(2)
    # 登录完成，进入QQ界面，选择一个信息作为判断成功与否的依据，如判断页面是否出现“消息”这个文本信息
    content = '消息'

    # 获取当前页面中是否有相关字样，来判断登录是否成功
    content_res = ocr_driver.search_from_img(get_img(), content)
    # assert语句进行判断，如登录成功，不会抛出异常
    assert len(content_res) >= 1



pytest_main([os.path.join(os.path.dirname(__file__), "main.py")])
```
在用**函数形式组织测试用例**中，我们会常常使用到`setup_method()`、`teardown_method()`、`setup_function()`和`teardown_method()`方法，其中
`setup_method()`方法在整个文件执行前执行一次`teardown_method()`方法在整个文件结束的时候执行一次，`setup_function()`方法在每个测试函数执行前执行一次，
`teardown_function()`方法在每个测试函数执行后执行一次（本例中未展示后两种方法）。  
同时，在编写测试用例的时候需要注意：测试用例往往具有针对性，即对手机设备的型号和版本具有敏感性，如在iOS和Android设备中，QQ的包名就不一样，即使是同一个系统的
手机设备，不同版本下往往也存在一定差异，使用者需要注意这一点，来避免意想不到的错误。当然，我们在设计测试程序时候，也可以设置判断语句，为不同的设备提供不同的测试入口，
提高测试用例的适配性。  

#### 2）类的形式组织测试用例  
以类的方式组织测试用例需要声明以`Test`开头的测试类，上面的示例以类的方式组织测试用例如下：
```python
# -*- coding: UTF-8 -*-
from uitrace.api import *
import pytest

# TODO: write your code
class TestClass:

    def setup_class(self):
        '''
        在测试类开始时执行一次
        '''
        # 初始化设备驱动和环境
        init_driver(workspace=os.path.dirname(__file__))

        # 预先处理系统弹窗
        start_event_handler()

        # 按下Home键，让手机初始界面为Home页面
        press(DeviceButton.HOME)

    def teardown_class(self):
        '''
        在测试类结束后执行一次
        '''
        # 测试用例执行完后，回到初始手机界面--Home页面
        press(DeviceButton.HOME)
        time.sleep(2)

        # 释放驱动，生成报告
        stop_driver()

    def test_login_qq(self):
        '''
        测试用例：QQ登录
        '''

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
        time.sleep(2)
        # 登录完成，进入QQ界面，选择一个信息作为判断成功与否的依据，如判断页面是否出现“消息”这个文本信息
        content = '消息'

        # 获取当前页面中是否有相关字样，来判断登录是否成功
        content_res = ocr_driver.search_from_img(get_img(), content)
        # assert语句进行判断，如登录成功，不会抛出异常
        assert len(content_res) >= 1


pytest_main([os.path.join(os.path.dirname(__file__), "main.py")])
```
在用**类的形式组织测试用例**中，我们会常常使用`setup_class()`、`teardown_class()`、`setup_method()`和`teardown_method()`方法，
其中`setup_class()`方法在类执行前执行一次，`teardown_class()`方法在类执行后执行一次，`setup_method()`方法在类中每个测试方法执行前执行一次
，`teatdown_method()`方法在类中测试方法执行后执行一次（本例未展示后两种方法）。

### 示例2  
在示例1的基础上，本示例增加第二个测试用例——使用QQ登录QQ音乐。本示例以类的形式组织测试用例。  
```python
# -*- coding: UTF-8 -*-
from uitrace.api import *
import pytest

# TODO: write your code
class TestClass:

    def setup_class(self):
        '''
        在测试类开始时执行一次
        '''
        # 初始化设备驱动和环境
        init_driver(workspace=os.path.dirname(__file__))

        # 预先处理系统弹窗
        start_event_handler()

        # 按下Home键，让手机初始界面为Home页面
        press(DeviceButton.HOME)

    def teardown_class(self):
        '''
        在测试类结束后执行一次
        '''
        # 测试用例执行完后，回到初始手机界面--Home页面
        press(DeviceButton.HOME)
        time.sleep(2)

        # 释放驱动，生成报告
        stop_driver()

    def setup_method(self):
        '''
        每个测试用例前执行一次
        '''
        press(DeviceButton.HOME)
    
    def teardown_method(self):
        '''
        每个测试用例后执行一次
        '''
        pass

    def test_login_qq(self):
        '''
        测试用例：QQ登录
        '''

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
        time.sleep(2)
        # 登录完成，进入QQ界面，选择一个信息作为判断成功与否的依据，如判断页面是否出现“消息”这个文本信息
        content = '消息'

        # 获取当前页面中是否有相关字样，来判断登录是否成功
        content_res = ocr_driver.search_from_img(get_img(), content)
        # assert语句进行判断，如登录成功，不会抛出异常
        assert len(content_res) >= 1

    def test_music_login():
        '''
        测试用例：用QQ账号登录
        '''
        start_app("com.tencent.qqmusic")
        time.sleep(2)
        # 点击“我的”
        click("obj_1658128095776.jpg", by=DriverType.CV, timeout=30)
        # 点击“登录”
        click("obj_1658128118888.jpg", by=DriverType.CV, timeout=30)
        # 点击“用QQ”登录
        click([0.477, 0.773], by=DriverType.POS, duration=0.05)
        # 勾选“隐私条例”
        click([0.238, 0.523], by=DriverTypes.POS, duration=0.05)
        # 点击“同意”
        click("obj_1658128187147.jpg", by=DriverType.CV, timeout=30)
        # 点击“确认”
        click([0.562, 0.847], by=DriverType.POS, duration=0.05)
        time.sleep(2)
        # 设定完成登录判断标准
        content = '我的'
        content_res = ocr_driver.search_from_img(get_img(), content)
        assert len(content_res) >= 1


pytest_main([os.path.join(os.path.dirname(__file__), "main.py")])
```
pytest框架默认从上到下执行测试用例，本示例先测试QQ登录的测试用例，完成QQ登录，接着执行用QQ登录QQ音乐的测试用例，
由于此时QQ已经登录，QQ音乐可以直接使用已登录的QQ进行QQ登录。  
本示例使用了`setup_method()`和`teardown_method()`方法，可以在每个测试用例执行前、后执行一次。  

