# 常用API

WeAutomator 提供了约 50 个 API，如常用的点击、滑动、查找、等待、登录等，全部 API 文档详见 **工具**-**帮助**-**API**，有详细介绍。

## 连接设备
**先将手机和电脑相连，连接方式如下**
- [连接Android设备](../quick-start/android-connect.md)
- [连接iOS设备](../quick-start/ios-connect.md)

## API介绍
- 连接设备
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
- 断开连接
```python
# 结束驱动
stop_driver()
# 脚本运行结束后调用，会释放相关驱动，生成报告等
```
- 设备功能键操作
```python
press(name)
# name(DeviceButton):   
class DeviceButton{
  HOME = 3
  VOLUME_UP = 24
  VOLUME_DOWN = 25
  
  # for Android special
  BACK = 4
  POWER = 26
  DEL = 67
  MENU = 82
  PECENt_APP = 187
  SLEEP = 223
  WAKE_UP = 224

  # for IOS special
  LOCK = 1000
  UNLOCK = 1001
}
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
stop_app(pkg)
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
```python
# 获取设备中安装的app
app_list()
# return->list: app名字
```


- 点击

WeAutomator提供多种方式的点击操作，通过设置参数**by**来切换不同的点击方式。

  ```python
  # 点击图片,loc为图像路径或ndarray形式
  click(loc=img, by=DriverType.CV, offset=None, timeout=30, duration=0.05, times=1)
  # return->bool: 点击是否成功
  # 示例：点击登陆按钮位置，loc为登陆按钮截图
  click(loc='登陆.jpg', by=DriverType.CV)

  # 点击控件，loc为点击的Xpath
  click(loc=Xpath, by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
  # return->bool: 点击是否成功
  # 示例：通过Xpath的方式点击登陆按钮,Xpath可以使用WeAutomator IDE录制功能获得
  click('//android.widget.LinearLayout[@resource-id="com.tencent.mobileqq:id/ac1"]/android.widget.Button[@text="登录" and @resource-id="com.tencent.mobileqq:id/btn_login"]', by=DriverType.UI, timeout=20)
  
  # 点击文字，loc为待点击的文字信息
  click(loc=text, by=DriverType.OCR, offset=None, timeout=30, duration=0.05, times=1)
  # return->bool: 点击是否成功
  # 示例：通过OCR技术点击登陆按钮，loc为待点击的文本信息
  click(loc='登陆', by=DriverType.OCR)

  # 点击坐标, loc为点击的坐标信息
  click(loc=pos, by=DriverType.POS, offset=None, timeout=30, duration=0.05, times=1)
  # return->bool: 点击是否成功
  # 示例：点击屏幕上的特定坐标位置,可以通过WeAutomator IDE得出目标位置的坐标
  click(loc=[200, 200], by=DriverType.POS)

  #上述4中点击方式，最后都是通过调用 click_pos 实现
  click_pos(pos, duration=0.05, times=1)
  # return->bool: 点击是否成功
  #pos的计算方式由click()中的参数by决定。

  # 长按
  long_click(loc=None, by=DriverType.POS, offset=None, timeout=30, duration=1, **kwargs)
  # loc和by的设置与click方法一致
  # offset(list or tuple): 偏移，元素定位位置加上偏移为实际操作位置
  # timeout(int): 定位元素的超时时长
  # duration(float): 点击的按压时长
  # **kwargs: 基于不同的查找类型，需要其他的参数，具体参见各find函数
  # return->bool: 是否操作成功

  # 双击
  double_click(loc=None, by=DriverType.POS, offset=None, timeout=30, duration=0.05, **kwargs)
  # loc和by的设置和click方法一致
  # offset(list or tuple): 偏移，元素定位位置加上偏移为实际操作位置
  # timeout(int): 定位元素的超时时间
  # duration(float): 点击的按压时长，以实现长按
  # **kwargs：基于不同的查找类型，其他需要的参数，具体参见各find函数
  # return->bool: 操作是否成功
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
# by=DriverType.UI, loc: 目标控件的Xpath， 调用find_ui方法
# by=DriverType.CV, loc: 图片路径名，调用find_cv方法
# by=DriverType.OCR, loc：目标位置的文本信息，调用find_ocr方法
# by=DriverType.POS, loc: 坐标
# by=DriverType.GA_UNITY or by=DriverType.GA_UE, loc: 目标控件的Xpath，调用find_ga方法
# return: 查找到返回坐标，否则返回None
# 说明：find方法会根据不同的by参数，调用不同的查找方法，查找方法包括：find_cv, find_ocr, find_ui, find_ga

# 基于多尺寸模版匹配的图像查找
find_cv(tql, img=None, timeout=30, threshold=0.8, pos=None, pos_weight=0.05, ratio_lv=21, is_translucent=False, tpl_l=None, deviation=None, time_interval=0.5)
# tql(ndarray or str): 待匹配查找的目标图像
# img(ndarray or str): 在该图上进行查找，为None时则获取当前设备画面
# timeout(int): 查找超时时间
# threshold(float): 匹配阈值
# pos(tuple or list): 目标图像的坐标，以辅助定位图像位置
# pos_weight(float): 坐标辅助定位的权重
# tpl_l(ndarray or str): 备选的尺寸更大的目标图像，以辅助定位
# deviation(tuple or list): 偏差，目标及备选目标间的偏差
# ratio_lv(int): 缩放范围，数值越大则进行更大尺寸范围的匹配查找
# is_translucent(bool): 目标图像是否为半透明，为True则会进行图像预处理
# time_interval(float): 循环查找的时间间隔，默认为0.5s
# return->list: 查找到的坐标，未找到则返回None

# 基于OCR文字识别的查找
find_ocr(word, timeout=30, is_regular=True)
# word(str): 待查找的文字，支持正则
# timeout(int): 查找超时时间
# is_regulaar(bool): 为True时进行正则查找
# return->lsit: 查找到的中心点坐标

# 基于控件查找
find_ui(xpath, timeout=30, **kwargs)
# xpath(str): 控件xpath
# timeout(int): 查找超时时间
# return->list: 查找到的中心点坐标

# 基于GA控件的查找
find_ga(xpath, by=DriverType.GA_UNITY, timeout=30)
# xpath(str): 元素路径或者路径+id的组合，如：/test[@id=1]
# by(DriverType): 查找类型。GA Unity为DriverType.GA_UNITY, GA UE 为DriverType.GA_UE
# timeout(int): 查找超时时间
# return->list: GA控件的中心点坐标

# 综合查找
multi_find(ctrl="", img=None, pos=None, by=DriverType.UI, ctrl_timeout=30, img_timeout=10, **kwargs)
# 优先基于控件定位，未查找到则基于图片匹配+坐标定位，仍未找到则返回传入坐标
# ctrl(str): 待查找的控件
# img(ndarray or str): 待匹配查找的图像
# pos(list or tuple): 目标图像的坐标，以辅助定位图像位置
# by(DriverType): ctrl的控件类型，原生控件DriverType.UI, GA Unity为DriverType.GA_UNITY, GA UE为DriverType.GA_UE
# ctrl_timeout(int): 基于控件查找的超时时间
# img_timeout(int): 基于图像匹配查找的超时时间
# **kwargs: 不同查找类型需要设置参数，具体见各find函数
```

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
  
```python
# 选择使用微信登陆
from advanced.app.wechat.login import login_by_wechat
play_with_wechat_friends(locator = None, acc = '', pwd = '', timeout = 240)
# loc(str): 使用微信登陆的按钮图片，为None时默认当前已进入微信界面
# acc(str): 登陆的微信账号
# pwd(str): 微信密码
# return->bool: 登陆是否成功
```
  


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
- 文本输入
```python
# 文本输入
input_text(text, xpath=None, timeout=30, depth=10, ime=IMEType.ADBKEYBOARD)
# text(str): 待输入的文本
# xpath(xpath): iOS要基于控件输入，xpath形式定位
# timeout(int): 超时时间
# depth(int): source tree的最大深度值，部分应用深度值设置过大会导致操作不稳定，过小可能导致输入失败
# ime(IMEType): Android文本输入采用的方式
```
- 坐标转换
```python
# 将绝对坐标转换成相对坐标
abs2rel(pt)
# pos(tuple or list): 绝对坐标，如(0.2, 0.3)
# return->tuple: 相对坐标, 即(int(0.2*w), int(0.3*h)), (w, h)为当前手机屏幕尺寸
# 示例：
abs_pos = abs2rel(pos=(0.23, 0.6))

# 将相对坐标转换成绝对坐标
rel2abs(pt)
# pos(tuple or list): 相对坐标
# return->tuple: 绝对坐标
# 示例：
rel_pos = rel2abs((100, 200))
```
- 功能模块初始化
```python
# 初始化OCR框架， 为初始化则将在第一次调用相关功能时自动初始化
init_ocr(text_type='ch')
# text_type(str): 初始化语言类型，默认为'ch', 用于识别中文

# 初始化Android_UiAutomator框架，未初始化则将在第一次调用相关功能时自动初始化
init_ui()

# 初始化Android文本输入框架， 未初始化则将在第一次调用相关功能时自动初始化
init_input()

# 初始化GAutomator框架， 未初始化则将在第一次调用相关功能时自动初始化
init_ga(engine_type=DriverType.GA_UNITY, port=None)
# engine_type(DriverType): 初始化引擎类型， Unity为DriverType.GA_UNITY, UE为DriverType.UE
# port(int): 连接端口

# 初始化可选框架，以节省调用时初始化的时间
init_env(ocr=True, input=True, ui=True, **kwargs)
# ocr(bool): 初始化OCR文字识别框架
# input(bool): 初始化Android文本输入框架， 需为Android时才会执行
# ui(bool): 初始化Android UIAutomator控件识别框架，需为Android时才会运行
# **kwargs：初始化框架可传入的参数
```

- IOS special API
```python
# 执行操作
perform(actions)
# actions(list): 操作序列。如[pf_down(pos), pf_wait(0.1), pf_up()];
# 多指操作为[[指1操作序列]，[指2操作序列]]，如[[pf_down(pos1), pf_wait(0.1), pf_up()], [pf_down(pos2), pf_wait(0.1), pf_up()]]
# actions内的元素会返回对应的操作协议，perform会将这些协议传达到IOS设备，执行对应的操作

# 按下操作的协议
pf_down(pos)
# pos(tuple or list): 按下位置的坐标
# return->dict: 按下操作的协议

# 等待操作的协议
pf_wait(duration)
# duration(int or float): 等待时间（s）
# return->dict: 等待操作的协议

# 移动操作的协议
pf_moveto(pos)
# pos(tuple or list): 移动到的位置的坐标
# return->dict: 移动操作的协议

# 抬起操作的协议
pf_up()
# return->dict: 抬起操作的协议
```
- Android special API  
**slide_track(track)需要补充示例**
```python
# 初始化Android_UiAutomator框架，未初始化则将在第一次调用相关功能时自动初始化
init_ui()

# 初始化Android文本输入框架， 未初始化则将在第一次调用相关功能时自动初始化
init_input()

# 轨迹滑动
slide_track(track)
# track(str or list): 轨迹坐标点文件
# slide_track方法内部通过调用touch_down, touch_move和touch_up方法实现功能。

# Android按下操作
touch_down(pos, id=0, pressure=50)
# pos(tuple or list): 按下位置的坐标
# id(int): 操作id，不同id以实现多点操作
# pressure(int): 操作压力

# Android移动操作
touch_move(pos, id=0, pressure=50)
# pos(tuple or list): 移动到的位置坐标
# id(int): 操作id，不同id以实现多点操作
# pressure(int): 操作压力

# Android 抬起操作
touch_up(pos=None, id=0, pressure=50)
# pos(tuple or list): 抬起的位置坐标
# id(int): 操作id，不同id以实现多点操作
# pressure(int): 操作压力

# 获取当前的activity
current_activity()
# return->str: 当前的activity

# 获取屏幕分辨率
screen_size()
# return->list: 屏幕分辨率
```

- 其他
```python
# 记录报告
record_report(func, args=None, kwargs=None)
# func(func or str): 操作函数名或者操作名
# args：操作相关函数
# kwargs：操作相关函数

# 日志装饰器
log_deco(report=True)
# return->bool: 为True时自动截图记录在报告中，为False则只打印

# 高亮装饰器
highlight_line()

# 生成报告
generate_report(report_dir=None)
# report_dir(str): 报告生成路径
# 说明：stop_driver方法会默认调用该方法，如可能异常导致无法正常结束，可主动调用该函数
```
- 事件处理
```python
# 说明：此类API专门用来处理Android/IOS一些常见的系统弹窗事件(注：当前不支持app内的弹窗，只支持系统级别弹窗)
# Android设备预设事件
EVENT_RULE = [
    r'^(完成|关闭|关闭应用|好|允许|始终允许|好的|确定|确认|安装|下次再说|知道了|同意)$',
    r'^((?<!不)(忽略|允(\s){0,2}许|同(\s){0,2}意)|继续|清理|稍后|稍后处理|暂不|暂不设置|强制|下一步)$',
    r'^((?i)allow|Sure|SURE|accept|install|done|ok)$',
    ('(建议.*清理)', '(取消|以后再说|下次再说)'),
    ('(发送错误报告|截取您的屏幕|是否删除)', '取消'),
    ('(隐私)', '同意并继续'),
    ('(隐私)', '同意'),
    ('(残留文件占用|网络延迟)', '取消'),
    ('(更新|游戏模式)', '取消'),
    ('(账号密码存储)', '取消'),
    ('(出现在其他应用上)', '关闭'),
    ('(申请获取以下权限)', '(允许|同意)'),
    ('(获取此设备)', '(仅在使用该应用时允许|允许|同意)'),
    ('(以下权限|暂不使用)', r'^同[\s]{0,2}意'),
    ('(立即体验|立即升级)', '稍后处理'),
    ('(前往设置)', '暂不设置'),
    ('(我知道了)', '我知道了'),
    ('(去授权)', '去授权'),
    ('(看看手机通讯录里谁在使用微信.*)', '是'),
    ('(默认已允许以下所有权限|以下不提示|退出)', '确定'),
    ('(仅充电|仅限充电|传输文件)', '取消')
]

# IOS设备预设事件
EVENT_RULE_IOS = [
    r'^(完成|关闭|关闭应用|好|允许|始终允许|好的|以后|确定|确认|安装|下次再说|知道了|同意|无线局域网与蜂窝数据|以后再说)$',
    r'^((?<!不)(忽略|允(\s){0,2}许|同(\s){0,2}意)|继续|清理|稍后|稍后处理|暂不|暂不设置|强制|下一步)$',
    r'^((?i)allow|Sure|SURE|accept|install|done|ok)$',
    ('位置', '^(始终|使用App时允许)$'),
    ('更新', '^关闭$'),
    ('访问', '^(好|始终|使用App时允许|允许访问所有照片)$'),
    ('删除', '^取消$')
]

# 启动预设事件自动处理
start_event_handler()
# 说明：该方法将根据当前设备的类型(Android or IOS),选择对应的预设事件(EVENT_RULE or EVENT_RULE_IOS),然后通过调用load_default_handler方法，将预设事件加载


# 批量加载事件自动处理规则
load_default_handler(rule)
# rule(list): 事件正则规则。list元素可为str、list、tuple
# 说明：如果希望加载预设事件，则直接调用start_event_handler方法即可。如果想另外批量增加事件自动处理规则，可使用该方法。该方法内部通过循环的方式调用add_event_handler方法，将批量事件逐个加载，进行处理。


# 添加事件自动处理规则，并运行
add_event_handler(match_element, action_element=None)
# match_element(str): 判断目标的正则匹配，存在则进行action_element匹配并点击
# action_element(str): 点击目标的正则匹配，为None时则点击match_element规则匹配结果

# 事件自动处理立即生效
sync_event_handler()

# 清除事件自动处理规则
clear_event_handler()

# 以上handler系列事件处理api现支持对系统级别的弹窗处理，如果当前弹窗事件在预设事件中，可直接调用start_event_handler方法，如果当前弹窗时间不在预设时间内，可先调用add_event_handler方法，如add_event_handler("忽略", "忽略")，将预设之外的事件加载，再调用start_event_handler方法处理

```

- 图像算法  
```python
# 边缘匹配
edge_match(tpl, scene)
# tpl(ndarray or str): 待匹配查找的目标图像
# scene(ndarray or str): 在该图上进行查找
# return->list: 匹配结果，中心点坐标，未找到则返回None

# 特征点匹配
f = FeatureMatch()
f.init_matcher(detector=MatchAlogo.SIFT, matcher=MatchAlogo.FLANN)
rect = f.match(tpl, scene, **kwargs)
# init_matcher：初始化匹配
# match：图像匹配
# detector（MatchAlogo）：特征描述子，支持SIFT、SURF、ORB、AKAZE
# matcher(MatchAlogo): 搜索方法，支持FLANN、BF
# tpl(ndarray or str): 待匹配查找的目标图像
# scene(ndarray or str): 在该图上进行查找
# **kwargs: filter_thresh剔除特征点的阈值等
# return->list: 匹配结果，左上角点的坐标及区域宽、高，未找到则返回None

# 滑动检测
slide_verify(slider)
# slider(ndarray or str): 滑块图像

# 黑白屏检查
screen_check(img, pct_thresh=0.95, is_black=True, gray_thresh=30)
# img(ndarray): 待判断的图像
# pct_thresh(double): 判断阈值，占比超过了该比例则认为该图像为黑屏或白屏
# is_black (bool): True则判断是否为黑屏，False则判断是否为白屏
# gray_thresh (int): 灰度阈值，判断该像素点是否为黑屏区域或白屏区域
# return->bool: 检测结果
```
- 智能 monkey

```python
# 进行智能探索（Android）
ai_monkey(pkg=None, explore_type=ExploreType.CTRL, timeout=-1, pre_exec=None, web_check=True, keyboard_check=True, restart_interval = 900, other_data=[], qq_data=[], wechat_data=[])
# 进行智能探索（iOS）
ai_monkey(pkg=None, explore_type=ExploreType.UI, timeout=3600, pre_exec=None)
# 停止智能探索（Android）
stop_monkey(ai_key)
```
