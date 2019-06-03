from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):

    # 新增地址 按钮
    add_address_button = By.ID, "com.yunmall.lc:id/address_add_new_btn"

    # 默认的姓名和电话的信息的特征
    default_receipt_name_text_view = By.ID, "com.yunmall.lc:id/receipt_name"

    # 点击 新增地址
    def click_add_address(self):
        self.find_element_with_scroll(self.add_address_button).click()

    # 获取 默认的姓名和电话的文字信息
    def get_default_receipt_name_text(self):
        return self.get_text(self.default_receipt_name_text_view)
