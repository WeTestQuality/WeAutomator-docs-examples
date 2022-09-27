# Uitrace本地化部署

WeAutomator底层框架uitrace现已开源，使用者可以在本机python环境中安装uitrace相关wheel包，
编写相关脚本，实现对设备进行本地测试。  

## 安装  

可从uitrace官方仓库的release中下载paddleocronnx、uitrace和advanced的wheel包，或者联系相关人员获取。 

安装命令如下

```
python3 -m pip install paddleocronnx-2.5.0.3-py3-none-any.whl
python3 -m pip install uitrace-x.x.x-py3-none-any.whl
python3 -m pip install advanced-2.0.1-py3-none-any.whl
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

### 本地多机测试 

uitrace本地化部署后支持本机连接多台设备，用户可以在python脚本例接收命令行参数，完成对特定设备或多台设备的测试。

```python
# test.py
from uitrace.api import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--udid', '-u', help="device id")
args = parser.parse_args()

init_driver(workspace=os.path.dirname(__file__), udid=args.udid)
click('日历', by=DriverType.OCR, offset=None, timeout=30)
stop_driver()
```

用户可通过命令行运行python脚本，传入设备，完成对特定设备的测试。

```shell
# 指定一台设备
python3 test.py --udid=3debcc18

# 指定多台设备
python3 test.py --udid=3debcc18 & python3 test.py --udid=cea0a3ff
```
用户还可以通过以上方式传入多个参数，实现不同设备运行不通测试用例等复杂测试需求。

安装使用过程中遇到问题可联系相关人员或者在Github [issues](https://github.com/WeTestQuality/WeAutomator-docs-examples/issues)区提问。

