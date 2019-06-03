from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page

import pytest


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_add_address"))
    def test_add_address(self, args):

        name = args["name"]
        phone = args["phone"]
        info = args["info"]
        post_code = args["post_code"]
        toast = args["toast"]

        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 地址管理
        self.page.setting.click_address_list()
        # 地址管理 点击 新增地址
        self.page.address_list.click_add_address()
        # 新增地址 输入 收件人
        self.page.edit_address.input_name(name)
        # 新增地址 输入 电话
        self.page.edit_address.input_phone(phone)
        # 新增地址 输入 详细地址
        self.page.edit_address.input_info(info)
        # 新增地址 输入 邮编
        self.page.edit_address.input_post_code(post_code)
        # 新增地址 勾选 设为默认地址
        self.page.edit_address.click_default_address()
        # 新增地址 选择一个随机的区域
        self.page.edit_address.choose_region()
        # 新增地址 点击 保存
        self.page.edit_address.click_save()

        if toast is None:
            # "张三  18888888888"
            assert self.page.address_list.get_default_receipt_name_text() == "%s  %s" % (name, phone), "保存成功，默认的姓名和电话与输入的不符"
        else:
            assert self.page.edit_address.is_toast_exist(toast), "保存不成功，toast内容和预期不符"



