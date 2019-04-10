## 概述
对哔哩哔哩安卓客户端进行简单的测试,编写测试用例表格，完成代码的编写。

## 测试环境
Android 8.0、哔哩哔哩版本 5.39

## 测试工具
appium、 PyCharm

## 测试策略
### 1.外部功能测试
  - 测试目标
安装、卸载、app图标、运行是否正常
  - 采用技术
手工测试

### 2.界面测试
  - 测试目标
app各个页面显示（视频、文字、图片、样式等）是否正常显示
  - 采用技术
手工测试

### 3.功能测试
  - 测试目标
app各个组件（搜索栏、动态、频道、登录、注销等）功能是否正常使用
  - 采用技术
黑盒测试方法、手工测试

### 4.兼容性测试
  - 测试目标
app与其他主流软件的兼容、Android版本的兼容、分辨率的兼容等
  - 采用技术
黑盒测试方法、手工测试

### 5.手机流量及电量测试
  - 测试目标
app在启动前后、使用功能前后的流量和电量情况
  - 采用技术
手工测试

### 6.自动化测试
1.在手机上安装app
```
# 安装包路径安装
driver.install_app(r"D:\apk\iBiliPlayer-bili.apk")
```

2.server启动参数
```
# init_driver.py

from appium import webdriver

def init_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = '192.168.149.104:5555'
    # app的信息
    desired_caps['appPackage'] = 'tv.danmaku.bili'
    desired_caps['appActivity'] = '.MainActivityV2'
    # 中文输入允许
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明driver对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
```

3.元素定位
```
# __init__.py

from selenium.webdriver.common.by import By


# 点击左边头像进入侧边栏
clk_sidebar = (By.ID, "avatar_layout")
# 点击头像登录
clk_avatar = (By.ID, "avatar_layout")
# 点击手机号/邮箱输入框
clk_username = (By.ID, "username")
# 点击密码框
clk_userpwd = (By.ID, "userpwd")
# 点击登录按钮
clk_login_btn = (By.ID, "btn_login")
```

4.登录类
```
# login.py

from base.base import Base
import packages

class Login(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    # 点击左边头像进入侧边栏
    def click_sidebar(self):
        self.click_element(packages.clk_sidebar)

    # 点击头像登录
    def click_avatar(self):
        self.click_element(packages.clk_avatar)

    # 登录
    def login(self, username, pwd):
        # 输入手机号/邮箱
        self.input_text(packages.clk_username, username)
        # 输入密码
        self.input_text(packages.clk_userpwd, pwd)
        # 点击登录按钮
        self.click_element(packages.clk_login_btn)
```

5.实现登录
```
# test_login.py

from base.init_driver import init_driver
import sys, os


# 加入当前目录
sys.path.append(os.getcwd())

class Test_Login:
    def setup(self):
        # 声明driver对象
        self.driver = init_driver()
        self.obj = Login(self.driver)
        # 点击左边头像进入侧边栏
        self.obj.click_sidebar()
        # 点击头像登录
        self.obj.click_avatar()

    # 退出测试
    def quit_test(self):
        self.driver.quit()

    # 对账号密码进行测试
    @pytest.mark.parametrize("username, pwd", [("Alcarin", "2333")])
    def test_login_1(self, username, pwd):
        self.obj.login(username, pwd)
```


