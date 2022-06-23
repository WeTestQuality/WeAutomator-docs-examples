# 常用API

WeAutomator 提供了约 50 个 API，如常用的点击、滑动、查找、等待、登录等，全部 API 文档详见 **工具**-**帮助**-**API**，有详细介绍。
- 连接设备

先将手机和电脑相连，连接方式如下
- [连接Android设备](../quick-start/android-connect.md)
- [连接iOS设备](../quick-start/ios-connect.md)


```python
from uitrace.api import *
init_driver(os_type=None, udid=None, max_size=800, bundle_id="com.watest.WebDriverAgentRunner.xctrunner",
            screen_port=None, ctrl_port=None, mode=RunMode.SINGLE, driver_lib=None, adb_path="", **kwargs):
    """  
        Args:
        os_type (OSType): 设备系统，安卓为OSType.ANDROID，iOS为OSType.IOS
        udid (str): 设备ID,不填则自动获取连接的设备id
        max_size (int): 传输画面的最大边长
        bundle_id (str): 设备为iOS时，WDA的bundle id
        screen_port (int): 获取画面服务的端口，不指定则使用闲置端口
        ctrl_port (int): 操作服务的端口，不指定则使用闲置端口
        mode (RunMode): 运行模式，一般使用默认即可
        driver_lib (DriverLib): 底层驱动使用的框架
        adb_path (str): adb路径，用户可进行配置以避免adb冲突；为None时则使用工具中自带的adb文件
        **kwargs: 脚本执行产出路径的修改等

    """
```    

- 应用操作

WeAutomator提供了针对应用的多种操作，包括：

```python
#安装应用
install_app(app_path)
# app_path(str): 安装包路径
# return->bool: 安装是否成功
```
```python
#卸载应用
uninstall_app(pkg)
# pkg(str):IOS系统为卸载应用的bundle id
# return->bool: 卸载是否成功
```
```python
#启动应用
start_app(pkg, cl)
# pkg(str): IOS为应用的bundle id， Android为包名
# return->bool: 卸载是否成功
```
```python
#重启应用
restart_app(pkg, **kwargs)
# pkg(str): IOS系统为被重启应用的bundle id， Android为包名
# return->bool: 卸载是否成功
```
```python
#获取当前应用
current_app():
# return->str: 应用的bundle id
```

- 点击

WeAutomator提供多种方式的点击操作，通过设置参数**by**来切换不同的点击方式。

  ```python
  # 点击图片,loc为图像路径或ndarray形式
  click(loc=img, by=DriverType.CV, offset=None, timeout=30, duration=0.05, times=1)
  # 点击控件，loc为点击的Xpath
  click(loc=Xpath, by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
  # 点击文字，loc为待点击的文字信息
  click(loc=text, by=DriverType.OCR, offset=None, timeout=30, duration=0.05, times=1)
  # 点击坐标, loc为点击的坐标信息
  click(loc=pos, by=DriverType.POS, offset=None, timeout=30, duration=0.05, times=1)
  ```

- 滑动

  ```
  # 根据坐标滑动
  slide_pos(pos_from, pos_to=None, pos_shift=None, duration=0)
  # 根据图像滑动
  slide(loc_from=None, loc_to=None, loc_shift=None, by=DriverType.CV, timeout=30, duration=None)
  # 根据控件滑动
  slide(loc_from=None, loc_to=None, loc_shift=None, by=DriverType.UI, timeout=30, duration=None)
  # 根据文字滑动
  slide(loc_from=None, loc_to=None, loc_shift=None, by=DriverType.OCR, timeout=30, duration=None)
  ```

- 查找

  ```
  # 根据图像查找（查找到返回坐标，未查找到返回None）
  find(loc, by=DriverType.CV, timeout=30)
  # 根据控件查找（查找到返回坐标，未查找到返回None）
  find(loc, by=DriverType.UI, timeout=30)
  # 根据文字查找（查找到返回坐标，未查找到返回None）
  find(loc, by=DriverType.OCR, timeout=30)
  ```

- 等待（3.2.0 及以后版本移除）

  ```
  # 在指定的时间等待图像出现（如果没有出现则抛出异常TimeOutError）
  wait(locator=None, timeout=20, by=DriverType.CV)
  # 在指定的时间等待控件出现（如果没有出现则抛出异常TimeOutError）
  wait(locator=None, timeout=20, by=DriverType.UI)
  # 在指定的时间等待文字出现（如果没有出现则抛出异常TimeOutError）
  wait(locator=None, timeout=20, by=DriverType.OCR)
  # 在指定的时间等待图片消失（如果仍然存在则抛出异常TargetStillExistError）
  wait_vanish(locator=None, timeout=20, by=DriverType.CV)
  # 在指定的时间等待控件出现（如果没有出现则抛出异常TargetStillExistError）
  wait_vanish(locator=None, timeout=20, by=DriverType.UI)
  # 在指定的时间等待文字出现（如果没有出现则抛出异常TargetStillExistError）
  wait_vanish(locator=None, timeout=20, by=DriverType.OCR)
  ```

- 判断存在（3.2.0 及以后版本移除）

  ```
  # 在指定的时间等待图像出现（存在返回True，不存在返回False）
  exists(locator=None, timeout=20, by=DriverType.CV)
  # 在指定的时间等待控件出现（存在返回True，不存在返回False）
  exists(locator=None, timeout=20, by=DriverType.UI)
  # 在指定的时间等待文字出现（存在返回True，不存在返回False）
  exists(locator=None, timeout=20, by=DriverType.OCR)
  ```

- 账号相关

  ```
  # QQ登录
  qq_login(acc='', pwd='')
  # 微信登录
  wechat_login(acc = '', pwd = '')
  # 选择和QQ好友一起玩
  play_with_qq_friends(locator=None, acc='', pwd='', timeout=240)
  # 选择和微信好友一起玩
  play_with_wechat_friends(locator = None, acc = '', pwd = '', timeout = 240)
  ```

- 设备相关

  ```
  # 获取远程数据（苹果设备无此功能）
  get_data(platform = PlatformType.OUTER, name="", default_data={})
  # 根据xpath获取元素列表
  get_elements(xpath, by=DriverType.UI)
  # 获取设备当前画面
  get_img()
  # 获取控件树
  get_uitree(by=DriverType.UI)
  # 将绝对坐标转换成相对坐标
  ratio_transfer(pt)
  # 将相对坐标转换成绝对坐标
  win_transfer(pt)
  # 手机截图
  screenshot(label='screenshot', img_path=None, pos=None)
  # 获取脚本目录
  script_dir()
  # 执行adb shell命令
  shell(cmd)
  # 执行adb shell命令不显示窗口
  shell_noshow(cmd)
  # 苹果设备将绝对坐标转换成相对坐标
  abs2rel(pt)
  # 苹果设备将相对坐标转换成绝对坐标
  rel2abs(pt)
  ```

- 智能 monkey

  ```
  # 进行智能探索（Android）
  ai_monkey(pkg=None, explore_type=ExploreType.CTRL, timeout=-1, pre_exec=None, web_check=True, keyboard_check=True, restart_interval = 900, other_data=[], qq_data=[], wechat_data=[])
  # 进行智能探索（iOS）
  ai_monkey(pkg=None, explore_type=ExploreType.UI, timeout=3600, pre_exec=None)
  # 停止智能探索（Android）
  stop_monkey(ai_key)
  ```
