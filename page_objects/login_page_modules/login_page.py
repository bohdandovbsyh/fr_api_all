import allure

from page_objects.dashboard_page_modules.dashboard_page import DashboardPage
from page_objects.login_page_modules.login_page_locators import LoginPageLocators
from utilities.ui_utilities.base_page import BasePage

@auto_step
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__page_locators = LoginPageLocators()

    @allure.step
    def set_email(self, email_value):
        self.send_keys(self.__page_locators.email_input, email_value)
        return self

    @allure.step
    def set_password(self, password):
        self.send_keys(self.__page_locators.user_password_input, password)
        return self

    @allure.step
    def click_login(self):
        self.click(self.__page_locators.login_button)
        return DashboardPage(self._driver)
