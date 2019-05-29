from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    # 昵称
    nick_name_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    def get_nick_name_text(self):
        return self.find_element(self.nick_name_text_view).text