from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    # 我
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    # 分类
    category_button = By.ID, "com.yunmall.lc:id/tab_category"

    # 点击 我
    def click_me(self):
        self.click(self.me_button)

    # 点击 分类
    def click_category(self):
        self.click(self.category_button)

    def login_if_not(self, page):
        # 判断登录状态
        self.click_me()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return

        # 没有登录，就去登录
        # 点击 已有账号
        page.register.click_login()
        # 输入 用户名
        page.login.input_username("itheima_test")
        # 输入 密码
        page.login.input_password("itheima")
        # 点击 登录
        page.login.click_login()
