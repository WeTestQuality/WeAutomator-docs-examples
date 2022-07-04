# 如何在Android设备上进行自动化测试

## 1. 介绍
本示例包含以下内容：
- 如何在WeAutomator IDE中连接Android设备
- 

## 2. IDE中连接Android手机
使用WeAutomator IDE对Android进行自动化测试时，首先要连接Android设备。WeAutomator IDE不仅支持连接Android真机，还支持连接WeTest云真机。
连接Android手机前的配置信息请参考 [连接Android设备](docs/quick-start/android-connect.md)，本示例默认相关配置已正确设置

### 1）在IDE中连接Android真机
- 使用USB连接Android手机
- 点击IDE中的连接设备

    ![figure](images/1.png)

- 连接目标设备

    ![figure](images/2.png)

- 连接成功，IDE成功加载Android手机

    ![figure](images/3.png)


### 2) 在IDE中连接Android云真机

WeAutomator IDE可以连接WeTest云真机平台的云真机设备。WeTest云真机平台提供流畅无延时的云手机/定制手机，可通过实时日志、截图等功能快速进行问题定位/复现。

外部用户可以访问[WeTest云真机外部站](https://wetest.qq.com/products/cloud-phone)  
内部用户可以访问[WeTest云真机内部站](https://cloudtest.woa.com/introduce/test-lab?from=home)

登陆进入云真机平台后，可以根据自己的需求选择想要测试的设备，本示例以外部站为例

- 选择目标设备，点击**开始调试**，进入设备界面
- 点击**远程调试**，根据当前电脑系统选择调试工具，复制连接命令

    ![figure](images/4.png)
- 打开电脑命令行，将复制的连接命令粘贴进去，运行
- 通过命令行查看是否连接成功，或者使用`adb devices`查看连接设备

    ![figure](images/)
- 点击IDE中的连接设备
- 连接目标设备
- 连接成功，IDE成功加载Android手机
