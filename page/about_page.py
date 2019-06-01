from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AboutPage(BaseAction):

    # 版本更新 按钮
    update_button = By.XPATH, "//*[@text='版本更新']"

    # 点击 版本更新
    def click_update(self):
        self.click(self.update_button)

