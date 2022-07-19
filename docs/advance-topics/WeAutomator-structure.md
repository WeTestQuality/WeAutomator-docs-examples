# WeAutomator
WeAutomator是由腾讯推出的一款基于Python的、跨平台的UI自动化测试框架。WeAutomator提供丰富的功能，能实现在Android和iOS上的自动化测试。
### 代码目录结构
WeAutomator的框架核心库是uitrace库，该库通过封装opencv相关公共方法、ocr技术、智能录制截图相关方法和针对unity、ue游戏的GAutomator框架，提供了多种方式的定位技术，
同时基于框架实现的功能拓展库advanced库，提供了QQ/微信登陆相关操作、基于规则或者强化学习的monkey（需安装uitrace文件夹中requirements列出的torch库）、SIFT等点特征匹配算法、边缘匹配等图像处理相关算法。
#### uitrace 【框架核心库】

```
├── api.py 【用户API】  
├── cvlib 【cv相关功能】  
│  ├── cv_utils.py 【opencv相关公共方法】    
│  ├── ocr_match.py 【ocr匹配类】    
│  ├── ocrmodel 【ocr模型】    
│  ├── roi.py 【智能录制截图相关方法】    
│  └── tpl_match.py 【图像增强模板匹配方法】    
├── device 【设备相关功能】     
│  ├── android 【Android相关功能】    
│  │  ├── adb 【adb可执行程序】    
│  │  ├── dev_mgr.py 【Android设备相关类】    
│  │  ├── driver    
│  │  │  ├── adb    
│  │  │  │  └── adb_mgr.py 【adb操作手机类】    
│  │  │  ├── cloudtest    
│  │  │  │  ├── wt_mgr.py 【云测SDK操作手机类，用于平台执行任务】    
│  │  │  │  └── wtsdk 【云测SDK】    
│  │  │  ├── scrcpy    
│  │  │  │  ├── ffmpeg_wrapper.py 【ffmpeg解码相关定义】    
│  │  │  │  ├── scrcpy_mgr.py 【scrcpy操作手机类】    
│  │  │  │  └── scrcpy_protocol.py 【scrcpy协议定义】    
│  │  │  └── stf    
│  │  │    ├── minicap.py 【minicap获取图像类】    
│  │  │    ├── minitouch.py 【minitouch执行操作类】    
│  │  │    ├── rotation.py 【stf监控设备rotation类】    
│  │  │    └── stf_mgr.py 【stf管理类】    
│  │  ├── driver_mgr.py 【Android Driver管理类】    
│  │  ├── input    
│  │  │  ├── input_mgr.py 【Android输入文字类】    
│  │  └── ui    
│  │    ├── at    
│  │    │  ├── README.md 【at源码修改说明】    
│  │    │  └── at_mgr.py 【at管理类，用于获取控件树】    
│  │    ├── ui_mgr.py 【获取控件树管理类】    
│  │    └── uidump    
│  │      └── uidump_mgr.py 【获取控件树管理类】    
│  ├── ios 【iOS相关功能】    
│  │  ├── README.md    
│  │  ├── dev_mgr.py 【IOS设备相关类】    
│  │  ├── driver_mgr.py 【IOS Driver管理类】    
│  │  └── wda    
│  │    └── wda_mgr.py 【wda管理类】    
│  ├── game 【GAutomator相关功能，针对unity、ue游戏】    
│  │  └── ga    
│  │    ├── GAutomatorAndroid 【GA Android相关】    
│  │    ├── GAutomatorIOS 【GA IOS相关】    
│  │    ├── README 【GA源码修改说明】    
│  │    └── ga_mgr.py 【GA管理类】    
│  ├── driver_svr.py 【driver server用于与 ide 交互（socket 方式）】    
│  └── driver_http.py 【driver server用于与 ide 交互（http 方式，暂未使用）】    
├── requirements 【python环境依赖库】    
├── static 【生成测试报告相关静态文件】    
└── utils    
  ├── env.py 【全局变量类】    
  ├── log_handler.py 【日志类】    
  ├── param.py 【相关枚举类定义】    
  └── toolkit.py 【工具类】    
```
#### make 【工具框架打包构建】
```
├── ffmpeg  【ffmpeg相关库文件】    
├── app.spec 【pyinstall spec文件】    
├── make.py 【打包相关操作】    
└── logo.ico 【Windows下打包生成的exe图标文件】    
```
#### advance 【拓展功能库】
```
├── app    
│  ├── qq 【QQ登录相关方法】    
│  └── wechat 【微信登录相关方法】    
├── cvlib 【图像处理与识别相关扩展方法】    
└── monkey 【monkey相关扩展方法】    
```
#### ide_server.py

IDE 操作入口

#### venv 【部分python库源码修改】

#### api_doc 【API页面生成】    