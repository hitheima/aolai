from base.base_driver import init_driver
from page.page import Page


class TestVip:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_vip(self):
        # 如果没有登录 去登陆
        self.page.home.login_if_not(self.page)
        # 我 点击 加入vip
        self.page.me.click_be_vip()
        # 切换 web环境
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        # vip 输入 邀请码
        self.page.vip.input_invite("hello")
        # vip 点击 加入会员
        self.page.vip.click_be_vip()
        # 切换 原生环境
        self.driver.switch_to.context("NATIVE_APP")