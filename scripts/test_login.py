import time

from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_login(self):
        self.page.home.click_me()
        self.page.register.click_login()
        self.page.login.input_username("itheima_test")
        self.page.login.input_password("itheima")
        self.page.login.click_login()

        assert self.page.me.get_nick_name_text() == "itheima_test", "登录后的用户名和输入的用户民不一致"


