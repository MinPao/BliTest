from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, location, timeout=10, poll=0.5):
        """
        :param location:By.ID之类的属性
        :param timeout:超时时间
        :param poll:调用until或until_not的间隔时间
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_element(*location))

    def find_elements(self, location, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_elements(*location))

    # 点击操作
    def click_element(self, location):
        self.find_element(location).click()

    # 输入操作
    def input_text(self, location, text):
        input = self.find_element(location)
        input.clear()
        input.send_keys(text)