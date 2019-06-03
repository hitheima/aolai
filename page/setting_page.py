from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):

    # 关于百年奥莱 按钮
    about_button = By.XPATH, "//*[@text='关于百年奥莱']"

    # 清理缓存 按钮
    clear_cache_button = By.XPATH, "//*[@text='清理缓存']"

    # 地址管理 按钮
    address_list_button = By.XPATH, "//*[@text='地址管理']"

    # 点击 关于百年奥莱
    def click_about(self):
        self.find_element_with_scroll(self.about_button).click()

    # 点击 清理缓存
    def click_clear_cache(self):
        self.find_element_with_scroll(self.clear_cache_button).click()

    # 点击 地址管理
    def click_address_list(self):
        self.find_element_with_scroll(self.address_list_button).click()