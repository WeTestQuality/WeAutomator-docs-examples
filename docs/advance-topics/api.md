# 常用API

WeAutomator 提供了约 50 个 API，如常用的点击、滑动、查找、等待、登录等，全部 API 文档详见 **工具**-**帮助**-**API**，有详细介绍。
- 连接设备

先将手机和电脑相连，连接方式如下
- [连接Android设备](../quick-start/android-connect.md)
- [连接iOS设备](../quick-start/ios-connect.md)


```python
from uitrace.api import *
init_driver(os_type=None, udid=None, max_size=800, bundle_id="com.watest.WebDriverAgentRunner.xctrunner", screen_port=None, ctrl_port=None, mode=RunMode.SINGLE, driver_lib=None, adb_path="", **kwargs):
# os_type(OSType): 设备系统，安卓为OSType.ANDROID, iOS为OSType.IOS
# udid(str): 设备ID，不填则自动获取连接设备的id
# max_size(int): 传输画面的最大边长
# bundle_id(str): 设备为iOS时，WDA的bundle id
# screen_port(int): 获取画面服务的端口，不指定则使用闲置端口
# ctrl_port(int): 操作服务的端口，不指定则使用闲置端口
# mode(RunMode)：运行模式，一般使用默认即可
# driver_lib(DriverLib): 底层驱动使用的框架
# adb_path(str): adb路径，用户可进行配置以避免adb冲突；为None时则使用工具中自带的adb文件
# **kwargs：脚本执行产出路径的修改等

```    

- 应用操作

`可以通过WeAutomator IDE获取手机应用的package name(pkg)`

WeAutomator提供了针对应用的多种操作，包括：

```python
#安装应用
install_app(app_path)
# app_path(str): 安装包路径
# return->bool: 安装是否成功
# 示例： 安装指定包
install_app('com.sohu.inputmethod.sogou.apk')
```
```python
#卸载应用
uninstall_app(pkg)
# pkg(str):IOS系统为卸载应用的bundle id
# return->bool: 卸载是否成功
# 示例: 卸载指定应用
uninstall_app('com.sohu.inputmethod.sogou')
```
```python
#启动应用
start_app(pkg, clear_data=False)
# pkg(str): IOS为应用的bundle id， Android为包名
# clear_data: 清除应用数据（Android）默认为False
# return->bool: 启动是否成功
# 示例：启动手机设置（不同手机的同一应用的package name(pkg)可能不同
start_app('com.android.settings')
```
```python
#重启应用
restart_app(pkg, **kwargs)
# pkg(str): IOS系统为被重启应用的bundle id， Android为包名
# return->bool: 卸载是否成功
# 示例: 重启手机qq
restart_app('com.tencent.mobileqq')
```
```python
# 结束应用
stop_app(pkg))
# pkg(str): IOS系统为应用的bundle id， Android为应用包名
# return->bool: 结束是否成功
# 示例：关闭手机qq
stop_app('com.tencent.mobileqq')
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
  # 示例：点击登陆按钮位置，loc为登陆按钮截图
  click(loc='登陆.jpg', by=DriverType.CV)

  # 点击控件，loc为点击的Xpath
  click(loc=Xpath, by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
  # 示例：通过Xpath的方式点击登陆按钮,Xpath可以使用WeAutomator IDE录制功能获得
  click('//android.widget.LinearLayout[@resource-id="com.tencent.mobileqq:id/ac1"]/android.widget.Button[@text="登录" and @resource-id="com.tencent.mobileqq:id/btn_login"]', by=DriverType.UI, timeout=20)
  
  # 点击文字，loc为待点击的文字信息
  click(loc=text, by=DriverType.OCR, offset=None, timeout=30, duration=0.05, times=1)
  # 示例：通过OCR技术点击登陆按钮，loc为待点击的文本信息
  click(loc='登陆', by=DriverType.OCR)

  # 点击坐标, loc为点击的坐标信息
  click(loc=pos, by=DriverType.POS, offset=None, timeout=30, duration=0.05, times=1)
  # 示例：点击屏幕上的特定坐标位置,可以通过WeAutomator IDE得出目标位置的坐标
  click(loc=[200, 200], by=DriverType.POS)

  #上述4中点击方式，最后都是通过调用 click_pos 实现
  click_pos(pos, duration=0.05, times=1)
  #pos的计算方式由click()中的参数by决定。
  ```

- 滑动

WeAutomator提供了多种方式的滑动操作，通过设置参数**by**来切换不同的滑动方式
```python
# 滑动操作
slide(loc_from=None, loc_to=None, loc_shift=None, by=DriverType.CV, timeout=30, duration=None)
# by(DriverType),为滑动操作的查找方式，根据不同的by，loc_from和loc_to的选择也不一样
# by=DriverType.CV, loc_from：要滑动的图像；Loc_to: 滑动的终点位置图像
# by=DriverType.UI, loc_from: 要滑动的控件Xpath； loc_to：滑动的终点位置的Xpath
# by=DriverType.POS, loc_from: 要滑动的起点坐标；loc_to: 滑动的终点坐标
# by=DriverType.OCR,loc_from: 要滑动位置的文本信息； loc_to: 滑动的终点的文本信息
# return->bool: 操作是否成功
# slide()方法根据不同的by，采用不同的方式计算出滑动起点和终点的坐标，并调用slide_pos方法进行滑动

# 根据坐标滑动
slide_pos(pos_from, pos_to=None, pos_shift=None, duration=0)
# 以上滑动操作最后都是调用slide_pos方法，从起始位置滑到目标位置
```

- 查找

WeAutomator提供了多种方式的查找操作，通过设置参数**by**来切换不同的查找方式
```python
# 查找
find(loc, by=DriverType.CV, timeout=30)
# by(DriverType),为查找方式设定。根据不同的by，loc参数设定也不一样
# by=DriverType.UI, loc: 目标控件的Xpath
# by=DriverType.CV, loc: 图片路径名
# by=DriverType.OCR, loc：目标位置的文本信息
# by=DriverType.POS, loc: 坐标
# by=DriverType.GA_UNITY or by=DriverType.GA_UE, loc: 目标控件的Xpath
# return: 查找到返回坐标，否则返回None

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

```python
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
