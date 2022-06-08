# 常用API

WeAutomator 提供了约 50 个 API，如常用的点击、滑动、查找、等待、登录等，全部 API 文档详见 **工具**-**帮助**-**API**，有详细介绍。

- 点击

  ```
  # 点击图片
  click(loc=None, by=DriverType.CV, offset=None, timeout=30, duration=0.05, times=1)
  # 点击控件
  click(loc=None, by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
  # 点击文字
  click(loc=None, by=DriverType.OCR, offset=None, timeout=30, duration=0.05, times=1)
  # 点击坐标
  click(loc=None, by=DriverType.POS, offset=None, timeout=30, duration=0.05, times=1)
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
