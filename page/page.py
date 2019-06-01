from page.about_page import AboutPage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MePage
from page.register_page import RegisterPage
from page.setting_page import SettingPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def register(self):
        return RegisterPage(self.driver)

    @property
    def me(self):
        return MePage(self.driver)

    @property
    def setting(self):
        return SettingPage(self.driver)

    @property
    def about(self):
        return AboutPage(self.driver)
