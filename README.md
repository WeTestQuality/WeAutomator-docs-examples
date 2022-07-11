# WeAutomator-docs-examples

WeTest WeAutomator Documentation and Test Samples
## Documentation

- [概览](docs/overview.md)
- [版本更新](docs/changelog.md)
- [快速开始](docs/quick-start/quick_start.md)
    - [连接Android设备](docs/quick-start/android-connect.md)
    - [连接iOS设备](docs/quick-start/ios-connect.md)
    - [编写脚本](docs/quick-start/write-script.md)
    - [提交到云测平台-入手](docs/started.md)
- WeAutomator底层框架介绍   
WeAutomator是由腾讯推出的一款基于Python的、跨平台的UI自动化测试框架。WeAutomator提供超过50个API，能实现在Android和iOS上的自动化测试，其框架核心库uitrace通过封装opencv相关公共方法、ocr技术、智能录制截图相关方法和针对unity、ue游戏的GAutomator框架，提供了多种方式的定位技术，同时基于框架实现的功能拓展库advanced库，提供了QQ/微信登陆相关操作、基于规则或者强化学习的monkey（需安装uitrace文件夹中requirements列出的torch库）、SIFT等点特征匹配算法、边缘匹配等图像处理相关算法。
    - [WeAutomator框架介绍](docs/advance-topics/WeAutomator-structure.md)
    - [API文档](docs/advance-topics/api.md)
- 使用说明
    - [常用API](docs/advance-topics/api.md)
    - [原生控件录制](docs/advance-topics/record-app.md)
    - [坐标录制](docs/advance-topics/record-aixel.md")
    - [游戏控件录制](docs/advance-topics/record-game.md)
    - [执行脚本](docs/advance-topics/run-script.md)
    - [提交到wetest云测](docs/advance-topics/submit-script.md)
- 常见问题
    - [Android设备问题](docs/faq/android.md)
    - [iOS设备问题](docs/faq/ios.md)
    - [工具使用](docs/faq/ide.md)

## Examples

- [examples/test-mobile-browser](examples/test-mobile-browser/README.md)
- 更多例子待补充
