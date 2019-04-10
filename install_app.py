from appium import webdriver


# server启动参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = '192.168.149.102:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 安装包路径安装
driver.install_app(r"D:\apk\iBiliPlayer-bili.apk")
# 包名卸载
# driver.remove_app("tv.danmaku.bili")
driver.quit()