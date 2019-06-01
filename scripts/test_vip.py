import time

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

        # 断言，"邀请码输入不正确" 是否在 page_source 中
        assert self.is_can_not_be_vip()

        # 切换 原生环境
        self.driver.switch_to.context("NATIVE_APP")

    def is_can_not_be_vip(self, timeout=10, poll=0.1):
        """
        如果不能成为会员，有"邀请码输入不正确"字符串，返回True
        :return:
        """

        # 结束时间
        end_time = time.time() + timeout

        while True:
            # 如果结束时间大于当前时间，那么就认为超时了
            if end_time < time.time():
                return False
            if "邀请码输入不正确" in self.driver.page_source:
                return True

            time.sleep(poll)
