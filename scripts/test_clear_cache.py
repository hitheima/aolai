from base.base_driver import init_driver
from page.page import Page


class TestClearCache:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_clear_cache(self):
        # 如果没有登录，先登录
        self.page.home.login_if_not(self.page)
        # 我 - 点击 设置
        self.page.me.click_setting()
        # 设置 - 点击 关于
        self.page.setting.click_clear_cache()

        assert self.page.setting.is_toast_exist("清理成功")
