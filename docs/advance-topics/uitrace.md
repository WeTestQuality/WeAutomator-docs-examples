# Uitrace本地化部署

WeAutomator底层框架uitrace现已开源，使用者可以在本机python环境中安装uitrace相关wheel包，
编写相关脚本，实现对设备进行本地测试。  

## 安装  

可从uitrace官方仓库的release或者相关微盘中下载paddleocronnx、uitrace和advanced的wheel包，或者联系相关人员获取。 

安装命令如下

```
python3 -m pip install paddleocronnx-2.5.0.3-py3-none-any.whl
python3 -m pip install uitrace-x.x.x-py3-none-any.whl
python3 -m pip install advanced-x.x.x-py3-none-any.whl
```

运行以下命令验证是否安装成功

```
pip show paddleocronnx
pip show uitrace
pip show advanced
```

使用者需要根据具体的版本号来调整安装命令。

## Uitrace本地化使用指引

### 本地测试脚本编写 

提供简单样例如下

```python
from uitrace.api import *

def test():
    init_driver(os.path.dirname(__file__))
    pos = find('obj_1663242961.jpg', by=DriverType.CV)
    click(pos, by=DriverType.POS)
    stop_driver()

if __name__ == '__main__':
    test()
```

其他api的使用方式可参考[API文档](./api.md)

### 本地指定运行设备 

uitrace本地化部署后支持本机连接多台设备，用户可以在python脚本例接收命令行参数，完成对特定设备或多台设备的测试，同时脚本中也能从当前设备信息中获取设备的信息。

用户可以指定单台或者多台设备，运行同一脚本。

```python
# test.py
from uitrace.api import *


init_driver(workspace=os.path.dirname(__file__))
click('日历', by=DriverType.OCR, offset=None, timeout=30)
stop_driver()
```

```shell
# 命令行
# 指定一台设备
python3 test.py --udid=3debcc18

# 指定多台设备
python3 test.py --udid=3debcc18 & python3 test.py --udid=cea0a3ff
```

用户可以指定单台或者多台设备，运行同一pytest组织的用例 

```python
# main.py
from uitrace.api import *

pytest_main([os.path.join(os.path.dirname(__file__), 'test_case1.py')])
```

```python
# test_case1.py
from uitrace.api import *

def test_1():
    init_driver(workspace=os.path.dirname(__file__))
    start_app("com.tencent.mobileqq")
    click([0.1, 0.1], by=DriverType.CV, offset=None, timeout=30, duration=0.05)
    stop_driver()
```

```shell
# 命令行
# 指定单台设备
python3 main.py --udid=3debcc18

# 指定多台设备
python3 main.py --udid=3debcc18 & python3 main.py --udid=cea0a3ff

```

### 脚本中获取设备id等信息

用户可参考`uitrace/utils/toolkit.py`中的`parse_args()`函数，里面列举了可以获取到的信息，如想在脚本中获取设备id，可按以下方式：

```python
from uitrace.utils.toolkit import parse_args() as args

udid = args.udid

```

用户可以根据不同的设备id，在脚本里指定不同的测试场景

安装使用过程中遇到问题可联系相关人员或者在Github [issues](https://github.com/WeTestQuality/WeAutomator-docs-examples/issues)区提问。

