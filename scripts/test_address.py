from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_add_address(self):
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 地址管理
        self.page.setting.click_address_list()
        # 地址管理 点击 新增地址
        self.page.address_list.click_add_address()
        # 新增地址 输入 收件人
        self.page.edit_address.input_name("张三")
        # 新增地址 输入 电话
        self.page.edit_address.input_phone("18888888888")
        # 新增地址 输入 详细地址
        self.page.edit_address.input_info("三单元 504")
        # 新增地址 输入 邮编
        self.page.edit_address.input_post_code("100000")
        # 新增地址 勾选 设为默认地址
        self.page.edit_address.click_default_address()


