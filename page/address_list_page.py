from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):

    # 新增地址 按钮
    add_address_button = By.ID, "com.yunmall.lc:id/address_add_new_btn"

    # 点击 新增地址
    def click_add_address(self):
        self.find_element_with_scroll(self.add_address_button).click()
