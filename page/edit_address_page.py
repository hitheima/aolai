import random
import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditAddressPage(BaseAction):

    # 收件人 输入框
    name_edit_text = By.ID, "com.yunmall.lc:id/address_receipt_name"

    # 手机号 输入框
    phone_edit_text = By.ID, "com.yunmall.lc:id/address_add_phone"

    # 详细地址 输入框
    info_edit_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"

    # 邮编 输入框
    post_code_edit_text = By.ID, "com.yunmall.lc:id/address_post_code"

    # 设为默认地址 按钮
    default_address_button = By.ID, "com.yunmall.lc:id/address_default"

    # 所在地区 按钮
    region_button = By.ID, "com.yunmall.lc:id/address_province"

    # 省市区的特征
    area_feature = By.ID, "com.yunmall.lc:id/area_title"

    # 保存 按钮
    save_button = By.ID, "com.yunmall.lc:id/button_send"

    # 输入 收件人
    def input_name(self, text):
        self.input(self.name_edit_text, text)

    # 输入 手机号
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    # 输入 详细地址
    def input_info(self, text):
        self.input(self.info_edit_text, text)

    # 输入 邮编
    def input_post_code(self, text):
        self.input(self.post_code_edit_text, text)

    # 点击 设为默认地址
    def click_default_address(self):
        self.click(self.default_address_button)

    # 点击 所在地区
    def click_region(self):
        self.click(self.region_button)

    # 进入 所在地区 并且选择一个随机的区域
    def choose_region(self):
        self.click_region()
        time.sleep(1)
        while True:
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            # 所有的可选你的省市区
            areas = self.find_elements(self.area_feature)
            # 所有的可选的个数
            areas_count = len(areas)
            # 随机数下标
            area_index = random.randint(0, areas_count - 1)
            # 获取随机的城市
            areas[area_index].click()

            time.sleep(1)

    # 点击 保存
    def click_save(self):
        self.click(self.save_button)

