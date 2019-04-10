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