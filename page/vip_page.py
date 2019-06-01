from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class VipPage(BaseAction):

    # 邀请码 输入框
    invite_edit_text = By.XPATH, "//input[@type='tel']"

    # 立即成为会员 按钮
    be_vip_button = By.XPATH, "//input[@value='立即成为会员']"

    def input_invite(self, text):
        self.input(self.invite_edit_text, text)

    def click_be_vip(self):
        self.click(self.be_vip_button)