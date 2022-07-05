# 常用API

WeAutomator 提供了约 50 个 API，如常用的点击、滑动、查找、等待、登录等，全部 API 文档详见 **工具**-**帮助**-**API**，有详细介绍。
- 连接设备

先将手机和电脑相连，连接方式如下
- [连接Android设备](../quick-start/android-connect.md)
- [连接iOS设备](../quick-start/ios-connect.md)


```python
from uitrace.api import *
# 连接设备
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
4
- 账号相关

```python
# QQ登录
from advanced.app.qq.login import login_qq
login_qq(acc='', pwd='', has_verify=False)
# acc(str): QQ账号
# pwd(str): QQ密码
# has_verify(bool): 是否存在滑动验证过程
# return(bool): 是否登陆成功

# 微信登录
from advanced.app.wechat.login import login_wechat
wechat_login(acc = '', pwd = '')
# acc(str): 微信账号
# pwd(str): 密码
# return->bool: 登陆是否成功
```
```python
# 选择使用QQ登陆
from advanced.app.qq.login import login_by_qq
login_by_qq(loc=None, acc="", pwd="", timeout=240, has_verify=False)
# loc(str): 使用QQ登陆的按钮图片，为None时默认当前已进入QQ界面
# acc(str): QQ账号
# pwd(str): 密码
# return->bool: 登陆是否成功
```
  
  [使用qq登陆QQ音乐](../../examples/demos/login_by_qq_or_wechat/README.md)
```python
# 选择使用微信登陆
from advanced.app.wechat.login import login_by_wechat
play_with_wechat_friends(locator = None, acc = '', pwd = '', timeout = 240)
# loc(str): 使用微信登陆的按钮图片，为None时默认当前已进入微信界面
# acc(str): 登陆的微信账号
# pwd(str): 微信密码
# return->: 登陆是否成功
```
  
  [使用微信登陆QQ音乐](../../examples/demos/login_by_qq_or_wechat/README.md)


- 设备相关

```python
# 获取具体类型的驱动，便于调用该框架的原生API
get_driver(by=DriverLib.WDA)
# by(DriverLib): 驱动类型，WDA为DriverLib.WDA, UIAutomator为DriverLib.UIA, GA Unity为DriverType.GA_UNITY, UIAutomator为DriverType.GA_UE
# return->DeviceEnv: 具体驱动类型

# 根据xpath获取元素列表
get_elements(xpath, by=DriverType.UI)
# xpath(str): 获取元素的xpath
# by(DriverType): 获取元素的类型，系统原生DriverType.UI, GA Unity为DriverTpe.GA_UNITY, GA UE为DriverType.GA_UE
# win_id(int): 窗口id，对于控件有多窗口的情况，可以指定具体窗口(Android)
# return->list: 元素对象的list

# 获取设备当前画面
get_img()
# return-> ndarray: 画面图像

# 获取图像中所有的文本
get_text(img, text_type="ch")
# img(str): 待识别的图像
# text_type(str): OCR识别的文本类型，"ch"为中英文，"en"为英文
# return->list: 查找到的文本结果，列表内容有如下形式
# [[[127.0, 242.0], [201.0, 242.0], [201.0, 261.0], [127.0, 261.0]], ['注册/登录', 0.96725357]]，分别为左上、右上、右下、左下点坐标及识别结果与匹配度

# 获取控件树
get_uitree(by=DriverType.UI)
# by(DriverType): 获取控件树的类型，系统原生DriverType.UI, GA Unity为DriverType.GA_UNITY, GA UE为DriverType.GA_UE
# all_wins(bool): 为True时获取所有窗口控件，为False时则自动判断当前窗口获取其控件
# return->dict: 控件树

# 手机截图
screenshot(label='screenshot', img_path=None, pos=None, pos_list=None)
# label(str): 图像存储的文件名
# img_path(str): 存储图像的路径，为None时则存到默认目录
# pos(tuple or list): 将坐标绘制在图像上
# pos_list(list): 将一组坐标绘制在图像上
# return->(str): 图像存储路径
```
- 坐标转换
```python
# 将绝对坐标转换成相对坐标
abs2rel(pt)
# pos(tuple or list): 相对坐标

# 将相对坐标转换成绝对坐标
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
