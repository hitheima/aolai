import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestVip:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_file("vip_data.yaml", "test_vip"))
    def test_vip(self, args):

        keyword = args["keyword"]
        expect = args["expect"]

        # 如果没有登录 去登陆
        self.page.home.login_if_not(self.page)
        # 我 点击 加入vip
        self.page.me.click_be_vip()
        # 切换 web环境
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        # vip 输入 邀请码
        self.page.vip.input_invite(keyword)
        # vip 点击 加入会员
        self.page.vip.click_be_vip()

        # 断言，"邀请码输入不正确" 是否在 page_source 中
        assert self.page.vip.is_keyword_in_page_source(expect), "%s不在page_source中" % expect

        # 切换 原生环境
        self.driver.switch_to.context("NATIVE_APP")


