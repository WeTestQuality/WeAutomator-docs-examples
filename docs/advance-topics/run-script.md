# 执行脚本

## windows

### 老版本

请打开工具文件夹，点击 resources/app/uitraverse，该目录下有 WeTestUitracePython.exe。在该目录下执行以下命令

- 场景模式

```shell
$ WeTestUitracePython.exe run_probe -s ${deviceId} -r ${项目路径}
```

- 脚本模式

```shell
$ WeTestUitracePython.exe run_lyra -s ${deviceId} -r ${项目路径}`
```

参数解释

- `-s` 参数为设备串号，可从`adb devices`查看，不添加该参数则默认使用当前机器第一个设备
- `-r` 参数为项目文件夹路径

### 新版本

打开工具文件夹，点击 resources/app/uitraverse，该目录下有 WeTestUitracePython.exe，添加至环境变量。在项目目录下执行以下命令

```shell
$ WeTestUitracePython.exe --script main.py --mode 0
```

## Linux

### 老版本

先使用 UI 版本导出脚本功能导出可在 Linux 上执行的脚本，请自行在你的 Linux 主机上安装 python3.6.8，然后再安装以下依赖库。你可以通过一些环境管理方案来管理你的 python 环境，例如 virtualenv 等。

- 环境配置：python3.6.8
- 依赖库：
  ```python
  certifi==2020.4.5.1
  chardet==3.0.4
  idna==2.8
  lxml==4.5.0
  msgpack==0.6.1
  msgpack-numpy==0.4.4.3
  numpy==1.18.2
  opencv-python==4.2.0.34
  opencv-contrib-python==3.4.2.17
  Pillow==7.1.1
  pyzmq==18.0.1
  requests==2.21.0
  requests-toolbelt==0.9.1
  urllib3==1.24.3
  PCV==1.0
  ```

运行时先解压从工具中打包出的脚本文件，解压后目录为以下结构：

    .
    ├── adaptation
    ├── config
    ├── etcv
    ├── probe
    ├── runner
    ├── script
    ├── statics
    ├── thirdparty
    ├── runTest.sh
    └── endTest.sh

在该文件夹根目录下运行`./runTest.sh`, 或者执行以下命令:

- 场景模式

```shell
$ python3.6 runner/run_probe.pyc -s ${deviceId} -r ./script
```

- 脚本模式

```shell
$ python3.6 runner/run_lyra.pyc -s ${deviceId} -r ${项目路径}
```

参数解释

- `-s` 参数为设备串号，可从`adb devices`查看，不添加该参数则默认使用当前机器第一个设备
- `-r` 参数为项目文件夹路径
