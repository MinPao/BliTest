import pytest
from packages.login import Login
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

